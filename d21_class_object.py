class Person:
    def __init__(self, firstname='Air', lastname='Keith', age=25, country='Finland'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country


    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.country}'


p1 = Person()
print(p1.person_info())
p2 = Person('Bell', 'Motu', 30, 'Japan')
print(p2.person_info())


# Inheritance & Overriding
class Student(Person):
    def __init__(self, firstname='Air', lastname='Keith', age=25, country='Finland', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.country}'


s1 = Student('Laura', 'Pan', 30, 'Britain', 'female')
s2 = Student('Ketolin', 'Ben', 40, 'Spain', 'male')
print(s1.person_info())
print(s2.person_info())
