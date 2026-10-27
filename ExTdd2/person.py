class Person:
    def __init__(self, id: int, name: str, age: int, emails=None):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails if emails else []