import threading
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from pylsl import StreamInfo,StreamOutlet
import time
from brainflow.data_filter import DataFilter
ADS1299_Vref = 4.5  #reference voltage for ADC in ADS1299.  set by its hardware
ADS1299_gain = 24.0  #assumed gain setting for ADS1299.  set by its Arduino code
scale_fac_uVolts_per_count = ADS1299_Vref/float((pow(2,23)-1))/ADS1299_gain*1000000.
def gen_EEG_wifi_LSL(lslname='eeg1A'):

        args = {
            "ip_port": 2190,
            "serial_port": "",
            "mac_address": "",
            "other_info": "",
            "serial_number": "",
            "ip_address": "192.168.4.1",#这个ip地址需要查看openbci板子的ip
            "ip_protocol": 2,
            "timeout": 0,
            "file": "",
            "log": True,
            "streamer_params": "",
            "board_id": -1,
        }
        args['board_id'] = 5
        eegchannelsnums = 8

        params = BrainFlowInputParams()
        params.ip_port = args['ip_port']
        params.serial_port = args['serial_port']
        params.mac_address = args['mac_address']
        params.other_info = args['other_info']
        params.serial_number = args['serial_number']
        params.ip_address = args['ip_address']
        params.ip_protocol = args['ip_protocol']
        params.timeout = args['timeout']
        params.file = args['file']
        # self.str.set("ss" + self.eegserialport)
        if (args['log']):
            BoardShim.enable_dev_board_logger()
        else:
            BoardShim.disable_board_logger()

        eegboard = BoardShim(args['board_id'], params)

        eegboard.prepare_session()
        # eegboard.config_board('~6')
        sample = eegboard.get_sampling_rate(eegboard.get_board_id())
        #print('sample:',sample)
        eegboard.start_stream(45000, "")
        lslinfo = StreamInfo(lslname, 'EEG', eegchannelsnums, sample,
                                  'float32',
                                  'brain01')
        lsloutlet = StreamOutlet(lslinfo)
        sendeegThead = SendData(eegboard,lsloutlet)
        sendeegThead.start()

class SendData(threading.Thread):
    def __init__(self,parent,lsloutlet):
        super(SendData,self).__init__()
        self.parent = parent
        self.lsloutlet = lsloutlet
    def run(self):
        # 重写线程执行的run函数
        # 触发自定义信号
        eegchannel = self.parent.get_eeg_channels(self.parent.get_board_id())
        timechannel = self.parent.get_timestamp_channel(self.parent.get_board_id())
        print(timechannel)
        get_sample_count = 1000
        delaytime = 1.0*get_sample_count/self.parent.get_sampling_rate(self.parent.get_board_id())
        while(1):

            #data = self.parent.get_current_board_data(get_sample_count)
            count = self.parent.get_board_data_count()*1.2
            data = self.parent.get_board_data()
            delaytime = 1.0 * count / self.parent.get_sampling_rate(self.parent.get_board_id())
            showdata = data[eegchannel[0]:eegchannel[-1]+1,:]#*scale_fac_uVolts_per_count
            print(showdata)
            # timedata = data[timechannel:, :]
            # iddata = data[:1, :]
            # savedata = np.concatenate((showdata, timedata), axis=0)
            # savedata = np.concatenate((iddata, savedata), axis=0)

            for k in range(len(showdata)):
                 #print(showdata[k].shape)
                 DataFilter.perform_bandstop(showdata[k],get_sample_count,50,4.0,2,0,0)
                 DataFilter.perform_bandpass(showdata[k],get_sample_count,25,40,2,0,0)
            datat = showdata.T

            #datat *= -scale_fac_uVolts_per_count

            self.lsloutlet.push_chunk(datat.tolist())
            # for k in range(len(datat)):
            #     self.lsloutlet.push_sample(datat[k])
            #time.sleep(delaytime)
# eeg()
gen_EEG_wifi_LSL()