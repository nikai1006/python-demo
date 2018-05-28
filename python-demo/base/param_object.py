"""
变量也是对象，有属性和方法
"""

var = "kaini"
age = 30
my_list = [39, 30, 12, 34]
my_tuple = (2, 3, 4, 5, 1)
my_dict = {'tom': 32, 'lucy': 33}
my_set = set([1, 3, 4, 5, 8])
print(var.__class__)  ##取出变量类型
print(age.__class__)
print(my_list.__class__)
print(my_tuple.__class__)
print(my_dict.__class__)
print(my_set.__class__)

print(var.__hash__())
print(age.__hash__())
