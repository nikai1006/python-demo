"""
常用方法定义：

"""


class MethodClazz(object):
    hobby = 'Eat'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight #私有变量

    def add(self):
        pass

    def _minu(self):
        pass

    def __multiply(self):
        pass

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
       return self.__weight



if __name__ == '__main__':
    clazz = MethodClazz('nikai',23,57)
    print(dir(clazz))
    print(MethodClazz.get_hobby())
    print(clazz.get_weight)
    clazz.add()
