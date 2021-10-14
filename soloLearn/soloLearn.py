nameOld = input("Enter your name: ")
print("Hello, " + nameOld)

age = int(input("Enter your age "))
age += 10
print("The " + nameOld + " age is: " + str(age))

# Введення даних в Python

# Ініціалізуємо змінну і присвоюємо значення методу який дає введення з кончолі.
# Введені значення завжди String
x = input()

# Можна додати коментар який буде показуватись в консолі. Для цього в душках вводимо текст в лапках.
newX = input("Enter your name: ")

# Перетворення даних в Python
# Для перетворння типу даних використ int(), str(), float().
# При використанні print("This is:" + ) потріно використ тільки String після +.
age = int(input("Enter your age "))
print("The age is: " + str(age))

# In-Place Operators
# Для додавання числя до значення замість x=x+3
age += 3
# Можна використовувати для додавання двох Стрінгів
name = "Oleh"
name += "Ivaniv"

# Walrus operator
# Використовується для присвоєння значення для змінної
num = int(input())
print(num)
# Замість цього можемо виконати наступне
# print(numOne := int(input()))

# Booleans
myBoolean = True
print(myBoolean)

print(2 == 3)
# Return False
print("Oleh" == "Oleh")
# Return True

# Comparison
# For comparison we use == or !=
print(2 != 3)
# Also for compilation we can use > or <
# Different numeric types can also be compared, for example, integer and float.
print(7 > 5)
print(2 > 6)
# Also for compilation we can use >= or <=
print(3 >= (2 + 1))
print(2 <= 1)
# Greater than and smaller than operators can also be used to compare strings lexicographically
# (the alphabetical order of words is based on the alphabetical order of their component letters).
print(Olha > Oleh)

# if Statements
# Python uses indentation (white space at the beginning of a line) to delimit blocks of code.
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print("Var 1 is bigger")
print("Program ended")
print("Program ended")
# Here is the example of if/else statement. In Python we use indentation to show the if/else level.
# This example will check for all possible cases.
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print("Var 1 is bigger")
if var1 < var2:
    print("Var 2 is bigger")
if var1 == var2:
    print("Var 1 and Var 2 are equal")
print("Program ended")
# To perform more complex checks, if statements can be nested, one inside the other.
# This example will check only var1>var2, if no it will close if statement.
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print("Var 1 is bigger")
    if var1 < var2:
        print("Var 2 is bigger")
        if var1 == var2:
            print("Var 1 and Var 2 are equal")
print("Program ended")

# else Statements
var1 = int(input())
var2 = int(input())
if var1 >= var2:
    print("Var 1 is bigger or equal")
else:
    print("Var 2 is bigger")
# In order to make multiple checks, you can chain if and else statements.
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print("Var 1 is bigger")
else:
    if var1 < var2:
        print("Var 2 is bigger")
    else:
        if var1 == var2:
            print("Var1 and Var2 are equal")

# The elif (short for else if) statement is a shortcut to use when chaining if and else statements,
# making the code shorter.
# else: вкінці покажеться якщо жодна з умов не буде виконана.
var1 = int(input())
var2 = int(input())
if var1 > var2:
    print("Var 1 is bigger")
elif var1 < var2:
    print("Var 2 is bigger")
elif var1 == var2:
    print("Var1 and Var2 are equal")
else:
    print("Wrong input")

# Boolean logic is used to make more complicated conditions for if statements that rely on more than one condition.
# We can use next: and, or, not
var1 = int(input())
var2 = int(input())
if var1 == 10 and var2 == 10:
    print("It is 10 for both")
# not example, will return false
print(not 1 == 1)

# Operator Precedence
# The below code shows that == has a higher precedence than or
print(False == False or True)

# Chaining Multiple Conditions
grade = int(input())
if (grade >= 70 and grade <= 100):
    print("Passed")

# List
# A list is created using square brackets with commas separating items.
words = ["Hello", "world", "!"]
print((words[0]) + words[1] + words[2])
print((words[1]))
print((words[2]))
# An empty list is created with an empty pair of square brackets.
emptyList = []
print(emptyList)
# it is also possible to include several different types
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things)
print(things[0])
print(things[2][2])
# Nested lists can be used to represent 2D grids, such as matrices.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Some types, such as strings, can be indexed like lists.
example = "Hello world!"
print(example[3])

# List Operations
# The item at a certain index in a list can be reassigned.
numbers = [7, 7, 7, 7, 7, 7]
numbers[2] = 5
print(numbers)
# Lists can be added and multiplied in the same way as strings.
numbers = [7, 7, 7]
print(numbers + [1, 2, 3])
print(numbers * 3)
# To check if an item is in a list, the in operator can be used.
numbers = [1, 2, 3, 4, 5, 6, 4]
print(1 in numbers)
print(0 in numbers)
# The in operator is also used to determine whether or not a string is a substring of another string.
example = "Hello world!"
print("!" in example)
# To check if an item is not in a list, you can use the not operator in one of the following ways:
example = "Hello world!"
print("#" not in example)

# List Functions
# The append method adds an item to the end of an existing list.
numbers = [1, 2, 3, 4, 5, 6, 4]
numbers.append(0)
# To get the number of items in a list, you can use the len function.
numbers = [1, 2, 3, 4, 5, 6, 4]
print(len(numbers))
example = "Hello world!"
len(example)
# Allows you to insert a new item at any position in the list, as opposed to just at the end.
numbers = [1, 2, 3, 4, 5, 6, 4]
numbers.insert(0, 100)
# The index method finds the first occurrence of a list item and returns its index.
numbers.index(6)

# Returns the list item with the maximum value
max(numbers)
# Returns the list item with minimum value
min(numbers)
# Returns a count of how many times an item occurs in a list
numbers.count(1)
# Removes an object from a list
numbers.remove(5)
# Reverses items in a list.
numbers.reverse()

# The range() function returns a sequence of numbers.
# Example 1 (start from 0 by default)
numbers = list(range(10))
print(numbers)
# Example 2 (with defined range)
numbers = list(range(2, 10))
print(numbers)
# Example 3 (2 types of the same range)
print(range(20) == range(0, 20))
# Example 4 (with step)
numbers = list(range(1, 20, 3))
print(numbers)

# while Loops
# Example 1
i = 5
while i <= 5:
    print(i)
    i += 1
print(i)
# Example 2 (while + if)
x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1
# Example 3 (with brake)
# while True is a short and easy way to make an infinite loop
i = 0
while True:
    print(i)
    i += 1
    if i > 5:
        print("Braking")
        break
print("Finished")
# Example 4 (with continue)
i = 0
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print("Skipping")
        continue

# for Loop
# Example 1 (here i is the iterator, to assign the value for it for one iteration)
words = ["hello", "world", "spam", "eggs"]
for i in words:
    print(i + "!")
# The for loop can be used to iterate over strings.
str = "this is string test"
count = 0

for x in str:
    if x == "t":
        count += 1

print(count)

# Example 2 (for loop with range())
for i in range(5):
    print("Hello!")


# It is common to use the for loop when the number of iterations is fixed.
# The while loop is used in cases when the number of iterations is not known and depends on some calculations
# and conditions in the code block of the loop.

# Functions
# Using the def statement to create own function. Function name should be lower case only.
# After function should be 2 lines.
def print_oleh():
    print("Oleh")
    print("Oleh")
    print("Oleh")


print_oleh()


# Function with arguments example
def print_word(word, second_word):
    """
    This method is the test method
    :param word: is the first word
    :param second_word: is the second
    :return: sum of 2 words
    """
    print(word + "!" + second_word)


print_word("oleh", "hello")


# Once you return a value from a function, it immediately stops being executed.

# Function can be assigned and reassigned to variables, and later referenced by those names.
def multiply(x, y):
    return x * y


a = 4
b = 5
operation = multiply
print(operation(a, b))


# Functions can also be used as arguments of other functions.
def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10

print(do_twice(add, a, b))

# Modules
# The basic way to use a module is to add import module_name at the top of your code
import random

for i in range(5):
    value = random.randint(1, 20)
    print(value)
# There is another kind of import that can be used if you only need certain functions from a module.
from math import pi

print(pi)
# You can import a module or object under a different name using the as keyword.
from math import sqrt as square_root

print(square_root(100))

# Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing,
# subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

# The best way to install these is using a program called pip. Enter pip install library_name.

