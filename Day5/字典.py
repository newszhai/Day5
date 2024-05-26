import csv

# 假设CSV文件路径和文件名
csv_filename = 'C:/Users/Administrator/Desktop/attack.csv'
output_unique_ips_filename = 'C:/Users/Administrator/Desktop/unique_ips.csv'
output_duplicate_ips_filename = 'C:/Users/Administrator/Desktop/duplicate_ips.csv'

# 初始化字典来记录IP的出现次数
ip_counts = {}

# 打开CSV文件并读取内容
with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        ip = row[0]  # 假设IP地址在第一列
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

# 创建一个列表来存储未重复的IP地址
unique_ips = [ip for ip, count in ip_counts.items() if count == 1]

# 提取重复的IP地址及其计数
duplicate_ips = {ip: count for ip, count in ip_counts.items() if count > 1}

# 对重复的IP地址按照出现次数进行降序排序
duplicate_ips_sorted = sorted(duplicate_ips.items(), key=lambda item: item[1], reverse=True)

# 记录并输出重复和未重复IP的个数
print("\n重复的IP地址个数：", len(duplicate_ips_sorted))
print("未重复的IP地址个数：", len(unique_ips))

# 输出未重复的IP地址到CSV文件
with open(output_unique_ips_filename, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['IP地址'])  # 写入标题行
    for ip in unique_ips:
        writer.writerow([ip])  # 写入未重复的IP地址

# 输出排序后的重复的IP地址及其出现的次数到CSV文件
with open(output_duplicate_ips_filename, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['IP地址', '次数']) # 写入标题行
    for ip, count in duplicate_ips_sorted:
        writer.writerow([ip, count])  # 写入重复的IP地址及其计数

# 打印信息提示文件已保存
print(f"未重复的IP地址已保存到 {output_unique_ips_filename}")
print(f"重复的IP地址及其次数已保存到 {output_duplicate_ips_filename}")