# 已有的联系人字典
contacts = {
    '张三': {'职位': '销售经理', '电话': '1234567890'},
    '李四': {'职位': '技术支持', '电话': '0987654321'},
    '王五': {'职位': '运营策划', '电话': '1234567891'},
    '赵六': {'职位': '技术支持', '电话': '0987654322'}  # 修改了赵六的电话，以避免与李四重复
}


# 添加新联系人的功能
def add_new_contact():
    # 获取新联系人的姓名
    new_name = input("请输入新联系人的姓名：")

    # 检查该姓名是否已存在于字典中
    if new_name in contacts:
        print(f"{new_name} 已存在于联系人列表中。")
    else:
        # 获取新联系人的职位
        new_position = input(f"请输入 {new_name} 的职位：")
        # 获取新联系人的电话
        new_phone = input(f"请输入 {new_name} 的电话：")
        # 将新联系人的信息添加到字典中
        contacts[new_name] = {'职位': new_position, '电话': new_phone}
        print(f"{new_name} 的信息已成功添加。")

    # 查询联系人的功能


def query_contact():
    # 使用input函数提示用户输入姓名，并将输入的值赋给name变量
    name = input('请输入姓名：')

    # 检查用户输入的姓名是否在contacts字典中
    if name in contacts:
        contact_info = contacts[name]  # 索引到用户输入姓名的信息
        print(f"{name} 的信息是：{contact_info}")  # 输出对应的信息
    else:
        print(f"找不到名为 {name} 的联系人信息。")

    # 调用添加新联系人的功能（可选，根据实际需求决定是否调用）


add_new_contact()

# 调用查询联系人的功能
query_contact()