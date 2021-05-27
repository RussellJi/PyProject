import math
import numpy as np


def buffer(data, duration, data_overlap):
    """
    Returns segmented data based on the provided input window duration and overlap.

    Args:
        data (numpy.ndarray): array of samples.
        duration (int): window length (number of samples).
        data_overlap (int): number of samples of overlap.

    Returns:
        (numpy.ndarray): segmented data of shape (number_of_segments, duration).
    """
    # 向上取整（分段数），data_overlap代表相邻时间窗之间的重叠部分
    number_segments = int(math.ceil((len(data) - data_overlap) / (duration - data_overlap)))
    # 按时间窗获取数据（一时间窗为宽度的数据段组）
    temp_buf = [data[i:i + duration] for i in range(0, len(data), (duration - int(data_overlap)))]
    # 补全最后一个数据段
    temp_buf[number_segments - 1] = np.pad(temp_buf[number_segments - 1],
                                           (0, duration - temp_buf[number_segments - 1].shape[0]), 'constant')
    # 按顺序堆叠数据形成（数据段的数组）
    segmented_data = np.vstack(temp_buf[0:number_segments])

    return segmented_data


def get_segmented_epochs(data, window_len, shift_len, sample_rate):
    """
    Returns epoched eeg data based on the window duration and step size.

    Args:
        data (numpy.ndarray): array of samples.
        window_len (int): window length (seconds).
        shift_len (int): step size (seconds).
        sample_rate (float): sampling rate (Hz).

    Returns:
        (numpy.ndarray): epoched eeg data of shape.
        (num_classes, num_channels, num_trials, number_of_segments, duration).
    """

    num_classes = data.shape[0]
    num_chan = data.shape[1]
    num_trials = data.shape[3]

    duration = int(window_len * sample_rate)
    data_overlap = (window_len - shift_len) * sample_rate
    # 分段数目
    number_of_segments = int(math.ceil((data.shape[2] - data_overlap) /
                                       (duration - data_overlap)))

    segmented_data = np.zeros((data.shape[0], data.shape[1],
                               data.shape[3], number_of_segments, duration))

    for target in range(0, num_classes):
        for channel in range(0, num_chan):
            for trial in range(0, num_trials):
                segmented_data[target, channel, trial, :, :] = buffer(data[target, channel, :, trial],
                                                                      duration, data_overlap)

    return segmented_data
