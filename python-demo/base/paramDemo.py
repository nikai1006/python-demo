"""
python变量基础知识
"""
import sys
import io
# 基本数据类型
name = "nikai" ###字符串
age = 20 #整型
sex = True #布尔类型
weight = 71.4 #浮点型
datas = [90, 30, 60] ###list数组
my_tuple = (2, 3, 4, 5) ###元组
#########################################
age_dict = {'nikai':20,'lucy':30} ###字典
print(age_dict)
# print(age_dict.popitem())
del age_dict['nikai']
print(age_dict)
age_dict2 = age_dict.copy() ###字典copy
print(age_dict2)
print('lucy' in age_dict2)
print('nikai' in age_dict2)
print(age_dict2.keys())
print(age_dict2.values())
print(age_dict2.popitem()) ##弹出所有