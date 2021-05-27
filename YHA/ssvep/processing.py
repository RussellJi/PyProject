from brainflow.data_filter import DataFilter
from mne.decoding import UnsupervisedSpatialFilter
import numpy as np
from sklearn.decomposition import PCA, FastICA
import scipy.signal as signal

# 预处理步骤1
class step_1(object):
    def __init__(self):
        super().__init__()
        self.step_1_list = []
        self.list_1()

    def low_pass(self, data, parameter_list):
        filter_data = []
        for i in range(parameter_list[-1]):
            DataFilter.perform_lowpass(data[i], parameter_list[1], parameter_list[2], parameter_list[3],
                                       parameter_list[4], 3)
            filter_data.append(data[i])
        filter_data = np.array(filter_data)
        return filter_data

    def band_pass(self, data, parameter_list):
        filter_data = []
        for i in range(parameter_list[-1]):
            DataFilter.perform_bandpass(data[i], parameter_list[1], parameter_list[2], parameter_list[3],
                                        parameter_list[4], parameter_list[5], 3)
            filter_data.append(data[i])
        filter_data = np.array(filter_data)
        return filter_data

    def high_pass(self, data, parameter_list):
        filter_data = []
        for i in range(parameter_list[-1]):
            DataFilter.perform_highpass(data[i], parameter_list[1], parameter_list[2], parameter_list[3],
                                        parameter_list[4], 3)
            filter_data.append(data[i])
        filter_data = np.array(filter_data)
        return filter_data

    def trca_pass(self,data,parameter_list,axis=-1):
        # wn1=2*freq0/srate
        # wn2=2*freq1/srate
        # % 通带的截止频率为2.75 hz - -75hz, 有纹波
        fs = parameter_list[1]/parameter_list[2]
        Wp = np.array([3, 100]) / (fs / 2)
        #  % 阻带的截止频率
        Ws = np.array([(3 - 2), (100 + 2)]) / (fs / 2)
        # % 通带允许最大衰减为 db
        alpha_pass = 3

        #  % 阻带允许最小衰减为  db
        alpha_stop = 25
        # % 获取阶数和截止频率
        N, Wn = signal.cheb1ord(Wp, Ws, alpha_pass, alpha_stop)

        b, a = signal.cheby1(N, 0.5, Wn, 'bandpass')
        filter_data = signal.filtfilt(b, a, data, axis=axis)
        return filter_data


    def list_1(self):
        self.step_1_list.append(self.low_pass)
        self.step_1_list.append(self.band_pass)
        self.step_1_list.append(self.high_pass)
        self.step_1_list.append(self.trca_pass)



# 预处理步骤2
class step_2(object):
    def __init__(self):
        super().__init__()
        self.step_2_list = []
        self.list_2()

    def wavelet_filter(self, data, parameter_list):
        filter_data = []
        for i in range(parameter_list[-1]):
            # print(parameter_list[-1])
            # print(i)
            DataFilter.perform_wavelet_denoising(data[i], parameter_list[1], parameter_list[2])
            filter_data.append(data[i])
        filter_data = np.array(filter_data)
        return filter_data

    def rolling_filter(self, data, parameter_list):
        filter_data = []
        for i in range(parameter_list[-1]):
            DataFilter.perform_rolling_filter(data[i], parameter_list[1], parameter_list[2])
            filter_data.append(data[i])
        filter_data = np.array(filter_data)
        return filter_data

    def pca_filter(self, data, parameter_list):
        pca = UnsupervisedSpatialFilter(PCA(parameter_list[-1]), average=False)
        data = data[0:parameter_list[-1], :]
        print(data.shape)
        eeg_data = np.array([data])
        pca_data = pca.fit_transform(eeg_data)
        filter_data = pca_data[0]
        return filter_data

    def ica_filter(self, data, parameter_list):

        pca = UnsupervisedSpatialFilter(FastICA(parameter_list[-1], tol=1), average=False)
        data = data[0:parameter_list[-1], :]
        # print(data.shape)
        eeg_data = np.array([data])
        ica_data = pca.fit_transform(eeg_data)
        filter_data = ica_data[0]
        """
        ica = FastICA(n_components=parameter_list[-1], tol=0.1)
        # print(ica.n_iter_)
        data = data[0:parameter_list[-1], :].T
        filter_data = ica.fit_transform(data)
        print(ica.tol)
        print(ica.n_iter_)
        filter_data = filter_data.T
        """
        return filter_data

    def kong_filter(self, data,parameter_list):
        filter_data =data
        return filter_data

    def list_2(self):
        self.step_2_list.append(self.wavelet_filter)
        self.step_2_list.append(self.rolling_filter)
        self.step_2_list.append(self.pca_filter)
        self.step_2_list.append(self.ica_filter)
        self.step_2_list.append(self.kong_filter)
