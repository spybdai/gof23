"""
singleton and monostate/borg
"""


class Singleton(object):

    # if it is thread safe?
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance


class LazySingleton(object):
    """
    this stupid code
    """
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            print 'not yet'
        else:
            print 'already %s' % self.get_instance()

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

    def test(self):
        print 'fuck stupid code'


class Monostate(object):

    __shared_state = {
        'x': 1,
        'y': 2
    }

    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state


class Monostate2(object):

    _shared_states = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_states
        return obj


# implementation with metaclass, use the special method of __call__
# question: how this method keep thread safe??
# this is the prefer solution for singleton pattern in Python

# note:
# __call__ in a class will make the object of this class callable.
# same, __call__ in a metaclass will make a class with it as metaclass callable

# more readings:
# https://stackoverflow.com/questions/6966772/using-the-call-method-of-a-metaclass-instead-of-new
# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__()
        return cls._instances[cls]


class MySingleton(object):
    __metaclass__ = MetaSingleton


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print id(obj1)
    print id(obj2)

    obj3 = LazySingleton()
    obj3.test()
    # a = LazySingleton.get_instance()
    # print a
    # obj4 = LazySingleton()
    # print obj3, obj4
    # print 'test'

    # test Monostate
    m1 = Monostate()
    m2 = Monostate()
    print m1.x, m2.x
    m1.x = 2
    print m1.x, m2.x

    # test Monostate2
    m3 = Monostate2()
    m4 = Monostate2()
    m3.x = 1
    print m3.x, m4.x


    # test meta singleton

    m5 = MySingleton()
    m6 = MySingleton()

    print m5, m6