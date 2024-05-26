import random
import string


def generate_bank_card_number():
    # 生成一个随机的16位银行卡号
    return ''.join(random.choices(string.digits, k=16))


# 设定要生成的字典数量
num_dicts = 1000

# 使用列表来存储每个生成的字典
bank_card_dicts = []

for _ in range(num_dicts):
    # 在每次循环中生成一个新的银行卡号
    card_number = generate_bank_card_number()
    # 创建一个包含新银行卡号和固定密码的字典
    bank_card_dict = {'card_number': card_number, 'password': '000000'}
    # 将字典添加到列表中
    bank_card_dicts.append(bank_card_dict)

# 打印生成的字典列表
for index, bank_card_dict in enumerate(bank_card_dicts):
    print(f"Dictionary {index + 1}: {bank_card_dict}")