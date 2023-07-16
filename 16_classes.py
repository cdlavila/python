import datetime

# Classes
print('\nClasses')
class Person:
    def __init__(self, name, birth_date, job):
        self.name = name
        self.birth_date = datetime.datetime.strptime(birth_date, '%d/%m/%Y').date()
        self.job = job

    def say_hello(self):
        print(f'Hello, my name is {self.name}')

    def say_birthdate(self):
        print(f'I was born on {self.birth_date}')

    def say_job(self):
        print(f'I am a {self.job}')

    def calculate_age(self):
        today = datetime.date.today()
        return today.year - self.birth_date.year

person_example = Person('Carlos', '10/08/2001', 'Software developer')
person_example.say_hello()
person_example.say_birthdate()
person_example.say_job()
print('Age calculation:', person_example.calculate_age())

# Inheritance
print('\nInheritance')
class Student(Person):
    def __init__(self, name, birth_date, job, university, grade):
        super().__init__(name, birth_date, job)
        self.university = university
        self.grade = grade

    def say_university(self):
        print(f'I study at {self.university}')

    def say_grade(self):
        print(f'My grade is {self.grade}')

student_example = Student('Santiago', '31/03/2000', 'Software developer', 'Technological University of Pereira', '9')
student_example.say_hello()
student_example.say_birthdate()
student_example.say_job()
student_example.say_university()
student_example.say_grade()
print('Age calculation:', student_example.calculate_age())