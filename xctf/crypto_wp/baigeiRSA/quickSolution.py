import libnum

# 快速解决方案（已知CTF常见分解）
n = 88503001447845031603457048661635807319447136634748350130947825183012205093541
# ciphertext
c = 40876621398366534035989065383910105526025410999058860023908252093679681817257
e = 65537

# 通过计算或查询已知的分解结果
p = 274539690398523616505159415195049044439
q = 322368694010594584041053487661458382819

# 验证
assert p * q == n

# 解密
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
# message
m = pow(c, d, n)
# Number to string (big endian).
flag = libnum.n2s(m)

print(f"p = {p}")
print(f"q = {q}")
print(f"Flag: {flag}")
print(f"Flag: {flag.decode()}") #HSCTF{@Zh3n_Ba1_G3i!@}