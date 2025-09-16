def caesar_decrypt(ciphertext, shift):
    """使用指定偏移量解密Caesar密码"""
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # 判断是大写字母还是小写字母
            ascii_offset = ord('A') if char.isupper() else ord('a')
            # 解密并保持大小写
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            # 非字母字符保持不变
            decrypted_text += char
    return decrypted_text


def try_all_shifts(ciphertext):
    """尝试所有可能的偏移量（1-25）"""
    print(f"密文: {ciphertext}\n")
    print("所有可能的解密结果:")
    print("-" * 50)

    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"偏移量 {shift:2d}: {decrypted}")


# 示例用法
if __name__ == "__main__":
    # 输入要解密的文本
    ciphertext = "oknqdbqmoq{kag_tmhq_xqmdzqp_omqemd_qzodkbfuaz}"

    # 尝试所有偏移量
    try_all_shifts(ciphertext) # 偏移量 12: cyberpeace{you_have_learned_caesar_encryption}
