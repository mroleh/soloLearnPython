# Functional Programming

# Functional programming is a style of programming that (as the name suggests) is based around functions.
# A key part of functional programming is higher-order functions.
# We have seen this idea briefly in the previous lesson on functions as objects.
# Higher-order functions take other functions as arguments, or return them as results.

def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))


# Pure Functions
# Functional programming seeks to use pure functions.
# Pure functions have no side effects, and return a value that depends only on their arguments.

def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


# Impure function
# The function above is not pure, because it changed the state of some_list.
some_list = []


def impure(arg):
    some_list.append(arg)


# Lambdas
# The same is possible with functions, provided that they are created using lambda syntax.
# Functions created this way are known as anonymous.

# Example 1
def my_func(f, arg):
    return f(arg)


my_func(lambda x: 2 * x * x, 5)


# Example 2
# named function
def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

# lambda
print((lambda x: x ** 2 + 5 * x + 4)(-4))

# Lambda functions can be assigned to variables, and used like normal functions.

double = lambda x: x * 2
print(double(7))


# Map and Filter
# The function map takes a function and an iterable as arguments, and returns a new iterable
# with the function applied to each argument.

# Example V1
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# Example V2
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x + 5, nums))

# To convert the result into a list, we used list explicitly.

# The function filter filters an iterable by removing items that don't match a predicate.
nums = [11, 22, 33, 44, 55]

result = list(filter(lambda x: x % 2 == 0, nums))
print(result)


# Generators are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
# They can be created using functions and the yield statement.
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


for i in countdown():
    print(i)


# Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
def infinite_sevens():
    while True:
        yield 7


for i in infinite_sevens():
    print(i)


# Decorators
# Decorators provide a way to modify functions using other functions. You do the changes with function without it modify

def decor(func):
    def wrap():
        print("=========")
        func()
        print("=========")

    return wrap()


def print_text():
    print("Hello world!")


# Call decorated function V1
decorated = decor(print_text)


# Call decorated function V2 (better), cause we show annotation
@decor
def print_text():
    print("Hello world!")


# Recursion
# The fundamental part of recursion is self-reference - functions calling themselves.
# The base case acts as the exit condition of the recursion.

# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120).
# To implement this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. n! = n * (n-1)!.
# Furthermore, 1! = 1. This is known as the base case

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))

# Sets
# Sets are data structures, similar to lists or dictionaries.
num_set = {1, 2, 3, 4}
string_set = set(["one", "two", "three"])

# To create an empty set, you must use set(), as {} creates an empty dictionary.
# They are unordered, which means that they can't be indexed.
# They cannot contain duplicate elements.
# They can store any type of value
# We can use len(), add() - add element, remove() - remove element with value, pop() -> will remove random
num_set = {1, 2, 3, 4}

num_set.add(5)
num_set.add("Oleh")
num_set.add(4.4)

first = {1, 3, 4, 7}
second = {2, 3, 5, 8}

print(first | second)  # The union operator | combines two sets to form a new one containing items in either.
print(first & second)  # The intersection operator & gets items only in both.
print(first - second)  # The difference operator - gets items in the first set but not in the second.
print(second - first)
print(first ^ second)  # The symmetric difference operator ^ gets items in either set, but not both.

# Data Structures
# Python supports the following data structures: lists, dictionaries, tuples, sets.
#
# When to use a dictionary:
# - When you need a logical association between a key:value pair.
# - When you need fast lookup for your data, based on a custom key.
# - When your data is being constantly modified. Remember, dictionaries are mutable.
#
# When to use the other types:
# - Use lists if you have a collection of data that does not need random access.
#    Try to choose lists when you need a simple, iterable collection that is modified frequently.
# - Use a set if you need uniqueness for the elements.
# - Use tuples when your data cannot change.

# Many times, a tuple is used in combination with a dictionary.
# For example, a tuple might represent a key, because it's immutable.

# ITERTOOLS
# itertools - standard library that contains several functions that are useful in functional programming.
# The function count counts up infinitely from a value.
# The function cycle infinitely iterates through an iterable (for instance a list or string).
# The function repeat repeats an object, either infinitely or a specific number of times.

from itertools import count

for i in count(3):
    print(i)
    if i >= 11:
        break

# There are many functions in itertools that operate on iterables, in a similar way to map and filter.
# Some examples:
# takewhile - takes items from an iterable while a predicate function remains true;
# chain - combines several iterables into one long one;
# accumulate - returns a running total of values in an iterable.
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)

print(list(takewhile(lambda x: x <= 6, nums)))

# There are also several combinatoric functions in itertool, such as product and permutation.
# These are used when you want to accomplish a task with all possible combinations of some items.

from itertools import permutations, product

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
