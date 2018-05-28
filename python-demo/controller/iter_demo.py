"""
iter迭代器
"""

obj = range(5)
iterator = iter(obj) ###
try:
    while True:
        print(iterator.__next__())
except StopIteration:  ###当迭代器中无元素时候，抛出异常
    pass