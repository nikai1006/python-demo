"""
运算符自定义
"""


class Operator(object):

    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __cmp__(self, other):
        """
        比较
        :param other:
        :return:
        """
        pass

    def __eq__(self, other):
        """
        等于
        :param other:
        :return:
        """
        if isinstance(other, Operator):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be Operator')

    def __lt__(self, other):
        """

        :param other:
        :return:
        """
        pass

    def __gt__(self, other):
        pass

    # ----------------------------------------

    def __add__(self, other):
        if isinstance(other, Operator):
            return self.age + other.age
        else:
            raise Exception("the type of other must be operator")

    def __sub__(self, other):
        super(Operator, self, other)

    def __mul__(self, other):
        pass

    def __divmod__(self, other):
        pass

    # --------------------------------------------

    def __or__(self, other):
        pass

    def __and__(self, other):
        pass


if __name__ == '__main__':
    operator = Operator('nikai', 23)
    lucy = Operator('lucy', 34)
    nikai = Operator('hello', 23)
    print(operator + lucy)
    print(operator == lucy)
    print(operator == nikai)
