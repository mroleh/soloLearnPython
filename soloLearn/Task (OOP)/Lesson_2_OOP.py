class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def about_me(self):
        print(f'Hi! My name is {self.first_name} {self.last_name} and I am {self.age} years old.')

    @staticmethod
    def is_able():
        print("I can do everything")


person = Person('Oleh', 'Ivaniv', '25')


# person.is_able()
# person.about_me()


class Student(Person):
    @staticmethod
    def learn():
        print("I can learn")


student = Student("Petro", "Makar", '22')
# student.about_me()
# student.learn()

is_instance = isinstance(student, Student)
# print(is_instance)  # return True if student is instance of Student

is_subclass = issubclass(Student, Person)


# print(is_subclass)  # return True if Student is subclass of Person


# In Python we can do multiple inheritance (множинне наслідування)
class FirstWorker(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def is_able(self):
        print("I'm first worker and I can do this")


class SecondWorker(Person):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)

    def is_able(self):
        print("I'm second worker and I can't do this")


class Workers(FirstWorker, SecondWorker):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        pass


workers = Workers("Stepan", "Giga", "26")
workers.is_able()

# In case if we inherit two classes, the first one would be main (new class will take methods from first)
# We call .is_able(), If it won't find .is_able() in FirstWorker class, it will try to find .is_able() in SecondWorker
# if it won't find there, it will try to find in class which was Base for FirstWorker -> Person


