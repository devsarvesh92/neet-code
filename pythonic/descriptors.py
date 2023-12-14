class AgeDescriptor:
    def __get__(self, instance, owner):
        print("Getting age")
        return instance._age

    def __set__(self, instance, value):
        if value < 5:
            raise ValueError("You're under age")
        instance._age = value


class Person:
    age = AgeDescriptor()

    def __init__(self, name, age) -> None:
        self.name = name
        self._age = age


if __name__ == "__main__":
    p = Person(name="Sarvesh", age=40)
    p.age = 44
    x = p.age
    p.age = 4
