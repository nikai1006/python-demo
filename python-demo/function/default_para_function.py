"""
参数默认值
当不指定参数时使用默认参数，指定参数时使用指定值

必须给无默认值的参数赋值，且保证顺序
"""


def welcom(who, staate='is', action='sleeping'):
    print(who, staate, action)


welcom('lucy', 'was')

welcom('tom', action='eating')
