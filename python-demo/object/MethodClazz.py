"""
常用方法定义：

"""


class MethodClazz(object):
    hobby = 'Eat'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight  # 私有变量

    def add(self):
        pass

    def _minu(self):
        pass

    def __multiply(self):
        pass

    @classmethod
    def get_hobby(cls):
        """
        使用classmethod修饰器的方法，可以直接使用类名来调用
        :return:
        """
        return cls.hobby

    @property
    def get_weight(self):
        """
        使用property修饰器的方法，可以像访问属性一样调用方法
        :return: 
        """
        return self.__weight



if __name__ == '__main__':
    clazz = MethodClazz('nikai',23,57)
    print(dir(clazz))
    print(MethodClazz.get_hobby())
    print(clazz.get_weight)
    clazz.add()
