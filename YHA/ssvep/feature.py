import warnings

import scipy
from brainflow.data_filter import DataFilter
import numpy as np
from scipy.stats import pearsonr
from sklearn.cross_decomposition import CCA


# 特征提取
class extration(object):
    def __init__(self):
        super().__init__()
        self.list()

    # 滤波器组
    def filter_bank(self,eeg, fs, idx_fb):
        if idx_fb == None:
            warnings.warn('stats:filterbank:MissingInput ' \
                          + 'Missing filter index. Default value (idx_fb = 0) will be used.')
            idx_fb = 0
        elif (idx_fb < 0 or 9 < idx_fb):
            raise ValueError('stats:filterbank:InvalidInput ' \
                             + 'The number of sub-bands must be 0 <= idx_fb <= 9.')

        Nq = fs / 2

        passband = [6, 14, 22, 30, 38, 46, 54, 62, 70, 78]
        stopband = [4, 10, 16, 24, 32, 40, 48, 56, 64, 72]
        Wp = [passband[idx_fb] / Nq, 90 / Nq]
        Ws = [stopband[idx_fb] / Nq, 100 / Nq]
        [N, Wn] = scipy.signal.cheb1ord(Wp, Ws, 3, 40)  # band pass filter StopBand=[Ws(1)~Ws(2)] PassBand=[Wp(1)~Wp(2)]
        [B, A] = scipy.signal.cheby1(N, 0.5, Wn, 'bandpass')  # Wn passband edge frequency

        y = np.zeros(eeg.shape)
        for ch_i in range(eeg.shape[0]):
            # apply filter, zero phass filtering by applying a linear filter twice, once forward and once backwards.
            # to match matlab result we need to change padding length
            y[ch_i, :] = scipy.signal.filtfilt(B, A, eeg[ch_i, :], padtype='odd',
                                               padlen=3 * (max(len(B), len(A)) - 1))

        return y

    # fb_cca参考信号
    def cca_reference(self, target_freq, fs, sample_num, num_harms=3):

        num_freqs = len(target_freq)

        tidx = np.arange(1, sample_num + 1) / fs  # time index

        y_ref = np.zeros((num_freqs, 2 * num_harms, sample_num))
        for freq_i in range(num_freqs):
            tmp = []
            for harm_i in range(1, num_harms + 1):
                stim_freq = target_freq[freq_i]  # in HZ
                # Sin and Cos
                tmp.extend([np.sin(2 * np.pi * tidx * harm_i * stim_freq),
                            np.cos(2 * np.pi * tidx * harm_i * stim_freq)])
            y_ref[freq_i] = tmp  # 2*num_harms because include both sin and
        return y_ref


    # 计算皮尔逊相关系数
    def corr2(self, A, B):
        #  mean of input arrays & subtract from input arrays themeselves
        A_mA = A - np.mean(A, keepdims=True)
        B_mB = B - np.mean(B, keepdims=True)
        numerator = np.sum(A_mA * B_mB)
        # Sum of squares
        ssA = (A_mA ** 2).sum()
        ssB = (B_mB ** 2).sum()

        denominator = np.sqrt(ssA * ssB)

        # Finally get corr coeff
        return numerator / denominator

    # 定义四次谐波参考信号矩阵
    def reference_signals(self, target_freq, sample_num, step_num):
        reference_signals = []
        # t从0到（数据段长度/采样率），间隔为1/256
        t = np.arange(step_num/sample_num, step_num+step_num/sample_num, step=step_num/sample_num)

        reference_signals.append(np.sin(np.pi * 2 * 1 * target_freq * t))
        reference_signals.append(np.cos(np.pi * 2 * 1 * target_freq * t))
        reference_signals.append(np.sin(np.pi * 2 * 2 * target_freq * t))
        reference_signals.append(np.cos(np.pi * 2 * 2 * target_freq * t))
        reference_signals.append(np.sin(np.pi * 2 * 3 * target_freq * t))
        reference_signals.append(np.cos(np.pi * 2 * 3 * target_freq * t))
        """ 1j."""
        reference_signals = np.array(reference_signals)

        return reference_signals

    # welch谱估计
    def psd_welch(self, data, parameter_list):
        feature_data = []
        for i in range(parameter_list[-1]):
            DataFilter.detrend(data[i], 1)
            DataFilter.detrend(data[i], 2)
            new_data = DataFilter.get_psd_welch(data[i], parameter_list[1], parameter_list[2], parameter_list[3],
                                                parameter_list[4])
            feature_data.append(new_data[0])
        feature_data = np.array(feature_data)
        return feature_data

    # 傅里叶变换
    def fft(self, data, parameter):
        fft_data = DataFilter.perform_fft(data, parameter)
        return fft_data

    # 复杂光谱特征
    def complex_spectrum(self, data, parameter_list):
        feature_data = []
        for i in range(parameter_list[-1]):
            fft_data = self.fft(data[i], parameter_list[1])
            real_part = np.real(fft_data)
            imag_part = np.imag(fft_data)
            feature = np.concatenate((real_part, imag_part), axis=0)
            feature_data.append(feature)
        feature_data = np.array(feature_data)
        return feature_data

    # 幅度谱特征
    def magnitude_spectrum(self, data, parameter_list):
        feature_data = []
        for i in range(parameter_list[-1]):
            fft_data = self.fft(data[i], parameter_list[1])
            feature = 2 * np.abs(fft_data)
            feature_data.append(feature)
        feature_data = np.array(feature_data)
        return feature_data

    # cca特征
    def cca_feature(self, data, parameter_list):
        cca = CCA(1)
        result = []
        for i in range(parameter_list[-1]):
            # reference_signals = self.reference_signals(parameter_list[1][i], parameter_list[2], parameter_list[3])
            reference_signals = self.reference_signals(parameter_list[1][i], parameter_list[2], parameter_list[3])
            cca.fit(data.T, reference_signals.T)
            x, y = cca.transform(data.T, np.squeeze(reference_signals).T)
            corr = np.corrcoef(x[:, 0], y[:, 0])[0, 1]
            result.append(corr)
        return result

    # trca特征
    def trca_feature(self, data, parameter_list):
        template = np.load('my_template.npy')
        features = np.load('my_feature.npy')
        result = []
        for i in range(parameter_list[-1]):
            # reference_signals = self.reference_signals(parameter_list[1][i], parameter_list[2], parameter_list[3])
            corr = self.corr2(np.transpose(template[i]).dot(features), np.transpose(data).dot(features))
            result.append(corr)
        return result

    # fb_cca
    def fbcca_feature(self,eeg, parameter_list, num_harms=3, num_fbs=10):
        fs = parameter_list[2] / parameter_list[3]
        fb_coefs = np.power(np.arange(1, num_fbs + 1), (-1.25)) + 0.25
        num_targs = len(parameter_list[1])
        y_ref = self.cca_reference(parameter_list[1], fs, parameter_list[2], num_harms)
        cca = CCA(n_components=1)  # initilize CCA
        # result matrix
        r = np.zeros((num_fbs, num_targs))
        for fb_i in range(num_fbs):  # filter bank number, deal with different filter bank
            testdata = self.filter_bank(eeg, fs, fb_i)  # data after filtering
            for class_i in range(num_targs):
                refdata = np.squeeze(y_ref[class_i, :, :])  # pick corresponding freq target reference signal
                test_C, ref_C = cca.fit_transform(testdata.T, refdata.T)
                # len(row) = len(observation), len(column) = variables of each observation
                # number of rows should be the same, so need transpose here
                # output is the highest correlation linear combination of two sets
                r_tmp, _ = pearsonr(np.squeeze(test_C),
                                    np.squeeze(ref_C))  # return r and p_value, use np.squeeze to adapt the API
                r[fb_i, class_i] = r_tmp

        results = np.dot(fb_coefs, r)  # weighted sum of r from all different filter banks' result
        print("fb_cca:",results)
        return results




    def list(self):
        self.feature_list = []
        self.feature_list.append(self.psd_welch)
        self.feature_list.append(self.complex_spectrum)
        self.feature_list.append(self.magnitude_spectrum)
        self.feature_list.append(self.cca_feature)
        self.feature_list.append(self.trca_feature)
        self.feature_list.append(self.fbcca_feature)
