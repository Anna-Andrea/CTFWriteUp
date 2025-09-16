import libnum
from Crypto.Util import number
import math

# 给定参数
n = 88503001447845031603457048661635807319447136634748350130947825183012205093541
c = 40876621398366534035989065383910105526025410999058860023908252093679681817257
e = 65537


def factorize_with_fermat(n):
    """使用费马因式分解法（对于接近的素数更有效）"""
    a = math.isqrt(n)
    b2 = a * a - n
    while not math.isqrt(b2) ** 2 == b2:
        a += 1
        b2 = a * a - n
    b = math.isqrt(b2)
    p = a + b
    q = a - b
    return p, q


def factorize_with_pollard_rho(n):
    """使用Pollard Rho算法进行因式分解"""
    if n % 2 == 0:
        return 2, n // 2

    x = 2
    y = 2
    d = 1
    f = lambda x: (x * x + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)

    return d, n // d


# 尝试多种因式分解方法
print("尝试因式分解 n...")

# 方法1: 直接试除（对于小数字有效）
try:
    from sympy import factorint

    factors = factorint(n)
    p = list(factors.keys())[0]
    q = n // p
    print(f"使用sympy分解: p={p}, q={q}")
except:
    # 方法2: 费马分解
    try:
        p, q = factorize_with_fermat(n)
        print(f"使用费马分解: p={p}, q={q}")
    except:
        # 方法3: Pollard Rho
        try:
            p, q = factorize_with_pollard_rho(n)
            print(f"使用Pollard Rho分解: p={p}, q={q}")
        except:
            # 方法4: 在线数据库或预计算
            # 对于CTF题目，通常数字是精心选择的，可以在factordb.com查询
            print("需要手动分解或查询因子数据库")
            exit()

# 验证分解结果
if p * q == n and number.isPrime(p) and number.isPrime(q):
    print("分解验证成功!")

    # 计算私钥和解密
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    m = pow(c, d, n)
    flag = libnum.n2s(m)

    print(f"私钥 d = {d}")
    print(f"解密消息 m = {m}")
    print(f"Flag: {flag.decode()}")
else:
    print("分解验证失败")