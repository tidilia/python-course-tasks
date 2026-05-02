from datetime import datetime


class CreatedAtMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["created_at"] = datetime.now()
        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=CreatedAtMeta):
    pass


print(MyClass.created_at)  # Дата и время создания класса MyClass
