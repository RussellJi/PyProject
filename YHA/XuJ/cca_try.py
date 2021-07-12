import time
import socket
import numpy as np
import pandas as pd
from sklearn.cross_decomposition import CCA
from brainflow.data_filter import DataFilter, FilterTypes
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from sklearn.decomposition import FastICA,PCA
from mne.decoding import UnsupervisedSpatialFilter

global index
index=0
global all_data
all_data = pd.DataFrame()


#获取脑电信号
def eeg_signals():
    #获取原始数据，根据采样率大小取出1s的数据
    eeg_data = board.get_current_board_data(sampling_rate)[0:9]
    # 带通滤波处理（0.5-50），中心频率25.25，带宽49.5
    eeg_channels = BoardShim.get_eeg_channels(0)
    for count, channel in enumerate(eeg_channels):
        eeg_data[channel]=eeg_data[channel]-np.average(eeg_data[channel])
        DataFilter.perform_bandpass(eeg_data[channel], BoardShim.get_sampling_rate(2), 25.25, 49.5, 3,FilterTypes.BESSEL.value, 0)
    eeg_data=eeg_data[1:9]
    eeg_data = np.array([eeg_data])
    pca = UnsupervisedSpatialFilter(PCA(8), average=False)
    eeg_data = pca.fit_transform(eeg_data)
    eeg_data=eeg_data[0]
    return eeg_data


#得到刺激块闪烁频率相对应的参考信号
def frequency_signals():
    reference_signals = []
    #刺激块闪烁频率
    flicker_freq = np.array([6, 7, 8, 9, 10])
    #计算与刺激频率相对应的参考信号
    for fr in range(0, len(flicker_freq)):
        reference_signal = []
        t = np.arange(0, 1, step=1.0 / (sampling_rate))
        #sin(2*PI*k*fi*t),k为谐波数，fi为频率值
        reference_signal.append(np.sin(np.pi * 2 * 1 * flicker_freq[fr] * t))
        reference_signal.append(np.cos(np.pi * 2 * 1 * flicker_freq[fr] * t))
        reference_signal.append(np.sin(np.pi * 2 * 2 * flicker_freq[fr] * t))
        reference_signal.append(np.cos(np.pi * 2 * 2 * flicker_freq[fr] * t))
        reference_signal.append(np.sin(np.pi * 2 * 3 * flicker_freq[fr] * t))
        reference_signal.append(np.cos(np.pi * 2 * 3 * flicker_freq[fr] * t))
        reference_signal = np.array(reference_signal)
        reference_signals.append(reference_signal)
    reference_signals = np.array(reference_signals, dtype='float32')
    return reference_signals


#运用CCA算法计算脑电信号X和频率信号Yi之间的相关性
def cca_classify(X_eeg_signals, Yi_frequency_signals):
    cca = CCA(1)
    corr_results = []
    for fr in range(0, Yi_frequency_signals.shape[0]):
        X = X_eeg_signals
        Yi =Yi_frequency_signals[fr, :, :]
        #计算X与Yi之间的相关性
        cca.fit(X.T, np.squeeze(Yi).T)
        X_train_r, Yi_train_r = cca.transform(X.T, np.squeeze(Yi).T)
        corr = np.corrcoef(X_train_r[:, 0], Yi_train_r[:, 0])[0, 1]
        #得出X与每个Yi的相关性
        corr_results.append(corr)
    if corr_results[np.argmax(corr_results)]>0.50:
        #设置阈值
        global index
        global all_data
        classify_result = np.argmax(corr_results)+1
        print(corr_results)
        index+=1
        #保存数据
        TT = pd.DataFrame(X_eeg_signals)
        all_data = all_data.append(np.transpose(TT[1:9]))
        if index==50:
            #保存数据
            all_data=pd.DataFrame(all_data)
            all_data.to_csv('./j_8_all_data.csv',index=False)
        return classify_result
    else:
        return -1


#配置OpenBCI相关参数并启用
BoardShim.enable_dev_board_logger ()
params = BrainFlowInputParams ()
board = BoardShim (0, params)
sampling_rate = BoardShim.get_sampling_rate(0)
board.prepare_session ()


#配置TCP/IP协议
'''HOST ='192.168.3.46'
PORT = 8085
ADDR = (HOST, PORT)
print('Server IP :',HOST)
#TCP传输协议
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print('waiting for connection...')
tcpCliSock, addr = tcpSerSock.accept()
print('connnecting from:', addr)'''
board.start_stream ()
time.sleep(2)

corrcounta=0
corrcountb=0
corrcountc=0
corrcountd=0
corrcountq=0
#线程1：得到脑电信号分类结果并转换为控制命令
while 1:
    time.sleep(1)
    #得出脑电信号的分类结果
    result = cca_classify(eeg_signals(), frequency_signals())
    #将分类结果转换为控制命令
    if result ==1:
        corrcounta += 1
        result_tcp = 'A'
        #tcpCliSock.send(result_tcp.encode('utf-8'))
        print(result_tcp)
    elif result ==2:
        corrcountb += 1
        result_tcp = 'B'
        #tcpCliSock.send(result_tcp.encode('utf-8'))
        print(result_tcp)
    elif result ==3:
        corrcountc += 1
        result_tcp = 'C'
       # tcpCliSock.send(result_tcp.encode('utf-8'))
        print(result_tcp)
    elif result ==4:
        corrcountd += 1
        result_tcp = 'D'
        #tcpCliSock.send(result_tcp.encode('utf-8'))
        print(result_tcp)
    elif result ==5:
        corrcountq += 1
        result_tcp = 'K'
        #tcpCliSock.send(result_tcp.encode('utf-8'))
        print(result_tcp)
    if(index==50):
        acc=corrcountc/index
        print('准确率：',acc)
        board.stop_stream()
        board.release_session()
        break