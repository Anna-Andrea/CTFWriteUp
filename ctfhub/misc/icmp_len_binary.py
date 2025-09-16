import pyshark

# Assume con1 and con2 are binary strings like '01100001...'
def binary_to_ascii(binary_str):
    chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)

cap = pyshark.FileCapture('icmp_len_binary.pcap', display_filter='icmp && icmp.type==8')
cap.load_packets()
flag = ''
# test two binary code method and check which one is right.
con1 = ""
con2 = ""
for i in range(0, len(cap)):
    if cap[i].icmp.data_len == '32':
        con1 += '0'
        con2 += '1'
    elif cap[i].icmp.data_len == '64':
        con1 += '1'
        con2 += '0'

ascii_con1 = binary_to_ascii(con1) # this one is the flag
ascii_con2 = binary_to_ascii(con2)

print(ascii_con1)
print(ascii_con2)
