# The None object is used to represent the absence of a value.
# It is similar to null in other programming languages.
print(None)


# The None object is returned by any function that doesn't explicitly return anything else.

def func():
    print("hi")


print(func())

# Dictionaries
# Dictionaries are data structures used to map arbitrary keys to values.
# Each element in a dictionary is represented by a key:value pair.
# Only immutable objects can be used as keys to dictionaries. (Str, inf, float), can't be array

# Example 1
ages = {"Oleh": 25, "Andrew": 24, "Fred": 20}
print(ages["Oleh"])
print(ages["Ivan"])

# Example 2 (dictionaries key can have array values)
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
print(primary["red"])

# We can assign value to already created dictionaries or to the new one
squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9
print(squares)

# We use "in" or "not in" to see is key in the dictionaries
nums = {
    1: "one",
    2: "two",
    3: "three"
}

print(1 in nums)
print("three" in nums)
print(4 not in nums)

# We use "get" to retrieve the value
pairs = {
    1: "apple",
    "orange": [2, 3, 4],
    True: False,
    None: "True"
}
print(pairs.get("orange"))
print(pairs.get(7))  # return None if doesn't find the key
print(pairs.get(12345, "not in the dictionary"))  # return message which we write after the key if doesn't find a key

# To get the list of dictionary keys
list(pairs.keys())
pairs.keys()

# Tuples (кортежі)
# Tuples are very similar to lists, except that they are immutable (they cannot be changed).
# Also, they are created using parentheses, rather than square brackets.
words = ("spam", "eggs", "sausages",)
print(words[0])

# Tuples can be created without the parentheses, by just separating the values with commas.
my_tpl = "one", "two", "three"
print(my_tpl[0])

# Empty tuples
tpl = ()

# List Slices
# List slices provide a more advanced way of retrieving values from a list.
# This returns a new list containing all the values in the old list between the indices.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])  # return [4, 9, 16, 25]
print(squares[3:8])
print(squares[0:1])

# If the first number in a slice is omitted, it is taken to be the start of the list.
# If the second number is omitted, it is taken to be the end.

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# List slices can also have a third number, representing the step, to include only alternate values in the slice.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])  # return each second value
print(squares[2:8:3])  # return list of values from 3-rd to 7-th value with step 3

# When negative values are used for the first and second values in a slice, they count from the end of the list.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])  # return list from second to the second from the end

# Revert the list V1
squares.reverse()
print(squares)
# Revert the list V2
print(squares[::-1])

# List Comprehensions
# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.
cubes = [i ** 3 for i in range(5)]
print(cubes)

# List Comprehensions can contain if
evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)  # return only negative values

# String Formatting
# String formatting uses a string's format method to substitute a number of arguments in the string.
num = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(num[0], num[1], num[2])
print(msg)

# String formatting can also be done with named arguments.
a = "{x}, {y}".format(x=5, y=12)
print(a)

# String functions
# join - joins a list of strings with another string as a separator.
print(", ".join(["one", "two", "thee"]))
# replace - replaces one substring in a string with another.
print("Hello ME".replace("ME", "world"))
# startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
print("This is a sentence.".startswith("This"))  # return True
# To change the case of a string, you can use lower and upper.
print("ALL IN CAPTURE".lower())
# The method split is the opposite of join turning a string with a certain separator into a list.


# List functions
# Often used in conditional statements, all and any take a list as an argument,
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
# The function enumerate can be used to iterate through the values and indices of a list simultaneously.
nums = [55, 44, 33, 22, 11]
if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)
    # return pair of index of element and value
    # (0, 55)
    # (1, 44)
    # (2, 33)
    # (3, 22)
    # (4, 11)

# Example how to format file output
# round() function is used to Round a number to a given precision in decimal digits.  2.9887 -> 2.99
print("{0} - {1}%".format(value1, round(value2, 2)))
