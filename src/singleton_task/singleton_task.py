from singleton_for_import import instance


# синглтон с метаклассом
class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class SingletonWithMeta(metaclass=SingletonMeta):
    pass


# синглтон с методом __new__
class SingletonWithNewMethod:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# синглтон с помощью импорта
b = instance
c = instance
