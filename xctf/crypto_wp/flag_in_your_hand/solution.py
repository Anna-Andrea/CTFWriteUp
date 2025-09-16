# 计算正确的token
a = [118, 104, 102, 120, 117, 108, 119, 124, 48, 123, 101, 120]
token = ''.join([chr(x - 3) for x in a])
print(f"正确的token: {token}") # token: security-xbu

# 验证这个token
# a[i] - token.charCodeAt(i) = 3
for i in range(len(a)):
    print(f"a[{i}] = {a[i]}, token[{i}] = '{token[i]}' (ASCII {ord(token[i])}), 差值 = {a[i] - ord(token[i])}")