# Classes

class Cat:
    legs = 4

    def __init__(self, color, name):
        self.color = color
        self.legs = name

    def bark(self):
        print("Woof!")


felix = Cat("ginger", "Felix")
print(felix.bark())
# Classes can have other methods defined to add functionality to them.
f_legs = felix.legs
# Classes can also have class attributes, created by assigning variables within the body of the class.
# These can be accessed either from instances of the class, or the class itself.

rover = Cat("black", "Rover")
stumpy = Cat("brown", "Stumpy")


# Inheritance
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def mouw(self):
        print("meouw")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("fido", "black")
print(fido.color)
fido.bark()


# The function super is a useful inheritance-related function that refers to the parent class.
class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):  # here we overload the method
        print(2)
        super().spam()  # here we call the parent  method


B().spam()


# Magic Methods
# They are used to create functionality that can't be represented as a normal method.
# One common use of them is operator overloading.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)


# More magic methods for common operators:
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |

# Python also provides magic methods for comparisons.
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=

# There are several magic methods for making classes act like containers.
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g., in for loops)
# __contains__ for in

# Weakly private methods and attributes have a single underscore at the beginning.
# In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
# The __repr__ magic method is used for string representation of the instance.
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)


# Strongly private methods and attributes have a double underscore at the beginning of their names.
# This causes their names to be mangled, which means that they can't be accessed from outside the class.

class Test:
    __egg = 7


t = Test()
# Example how to access to strongly private vars
print(t._Test__egg)


# Class Methods
# Class methods are different - they are called by a class, which is passed to the cls parameter of the method.
# A common use of these are factory methods, which instantiate an instance of a class,
# using different parameters than those usually passed to the class constructor.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())


# Static Methods
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples")
        else:
            return True


ingredients = ["cheese", "onion", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


# Properties
# Properties provide a way of customizing access to instance attributes.
# One common use of a property is to make an attribute read-only.

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True


# The setter function sets the corresponding property's value.
# The getter gets the value.

class Test:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

# @pineapple_allowed.setter
#     def pineapple_allowed(self, value):
#         if value:
#             password = input("Enter the password: ")
#             if password == "Sw0rdf1sh!":
#                 self._pineapple_allowed = value
#             else:
#                 raise ValueError("Alert! Intruder!")
