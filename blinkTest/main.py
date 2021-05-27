import pandas as pd

import matplotlib.pyplot as plt



def write(y1,y2,writer):
    
    # list转dataframe
    df = pd.DataFrame(y1, columns=['y1'])

    # 保存到本地excel
    df.to_excel(writer)

    # list转dataframe
    df2 = pd.DataFrame(y2, columns=['y2'])

    # 保存到本地excel
    df2.to_excel(writer)

if __name__ == '__main__':
    filename = "F:\DeviceData\\blink.xlsx"
    df = pd.read_excel("F:\DeviceData\\blink.xlsx")
    print(df.columns)
    print(df.shape)
    print(df)

    # 读取第一列数据
    x1 = []
    x1 = df["x1"].values
    print("x1:")
    print("size:",x1.size)
    print(x1)

    # 转为字符串格式
    x1 = [str(i) for i in x1]
    # 分割
    y1 = []
    y2 = []
    # print(x1[0][:12])
    # print(x1[0][-6:])
    for i in x1:
        y1.append(i[6:11])
        y2.append(i[-6:-3])
    print(y1[0])
    print(y2[0])

    plt.plot(y1,y2,label='blink data',linewidth=3,color='r',marker='o',
markerfacecolor='blue',markersize=12)
    plt.xlabel('time')
    plt.ylabel('A0 data')
    plt.show()

