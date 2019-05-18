class Man(object):
    hobby = 'Eat'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight #私有变量

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
        man = Man('nikai', 23, 80)
        print(man.hobby)
        print(man.name)
        print(man._age)
        print(man.get_weight())
        print(dir(man))
