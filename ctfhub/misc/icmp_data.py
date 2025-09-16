import pyshark

cap = pyshark.FileCapture('icmp_data.pcap', display_filter='icmp && icmp.type== 8')
# cap 打开名字为 data的，然后过滤掉 icmp 和icmp中type 为 8 的
flag = ''
for i in range(0, 25):  # 人工数出来flag有25长度 所以循环0到25
    flag += chr(int((cap[i].icmp.data_data)[24:26], 16))
    # 打开cap中第i个，然后打开他icmp中data中data
    # 数字为十进制 所以转换为16进制，并且占俩空，数一下能发现为24到26
    # int（x,16） 是将x变为16进制，然后chr是把他进行ascii编码
print(flag)
cap.close()