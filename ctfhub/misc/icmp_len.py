import pyshark
cap = pyshark.FileCapture('icmp_len.pcap', display_filter='icmp && icmp.type==8')
#过滤icmp流量
flag = ''
for i in range(0,18):
    flag+=chr(int(cap[i].icmp.data_len))
    #访问的是第i个cap中icmp数据包的data中的len
print(flag)

# test int to ascii code
flag = ''
result = [99, 116, 102, 104, 117, 98, 123, 97, 99, 98, 54, 53, 57, 102, 48, 50, 51, 125]
for i in range(len(result)):
    flag += chr(result[i])
print(flag)
