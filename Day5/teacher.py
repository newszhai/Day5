'''
无参数无返回值的函数
无参数有返回值的函数
有参数无返回值的函数
有参数有返回值的函数
'''
import random
# def cards():
#   card =[''.join(random.choices('0123456789', k=16)) for _ in range(1000)]
#   password=['000000' for _ in range(1000)]
#   dic=dict(zip(card,password))
#   print(dic.keys())#获取字典中所有键
#   print(dic.values())#获取字典中所有值
#   print(dic.items())#获取字典中所有键值对
#
# cards()


def cards(c,p) ->int:
  dic=dict(zip(c,p))
  print(dic.keys())#获取字典中所有键
  print(dic.values())#获取字典中所有值
  print(dic.items())#获取字典中所有键值对


  return 'str'
card =[''.join(random.choices('0123456789', k=16)) for _ in range(1000)]
password=['000000' for _ in range(1000)]
num=cards(card,password)#实际参数
print(num)
name=input('请输入您的名字：')
print(name)
