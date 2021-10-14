# Exceptions
# Common exceptions:
# ImportError: an import fails;
# IndexError: a list is indexed with an out-of-range number;
# NameError: an unknown variable is used;
# SyntaxError: the code can't be parsed properly;
# TypeError: a function is called on a value of an inappropriate type;
# ValueError: a function is called on a value of the correct type, but with an inappropriate value.

# Exception example with 1 exeption
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Calculation is done")
except ZeroDivisionError:
    print("An error occurs")

# Exception example with few exceptions
try:
    variable = 10
    print(variable + "Hello")
    print(variable / 2)
except ZeroDivisionError:
    print("divided by zero")
except (ValueError, TypeError):
    print("Error occurs")

# The finally statement is placed at the bottom of a try/except statement.
# Code within a finally statement always runs after execution of the code in the try, and possibly in the except, blocks
try:
    print("hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Zero error")
finally:
    print("the finally text")

# You can raise exceptions by using the raise statement.
print(1)
raise TypeError

# Exceptions can be raised with arguments that give detail about them.
name = "123"
raise TypeError("Called the error")

# Assertions
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

# Assertion can have 2-nt parameter - message
temp = -10
assert (temp > 0), "It is cold"

# Opening Files
mfile = open("test.txt")

# Sending "r" means open in read mode, which is the default.
# Sending "w" means write mode, for rewriting the contents of a file.
# Sending "a" means append mode, for adding new content to the end of the file.
# Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
mfile = open("test.txt", "w")
mfile.close()

# Reading Files
mfile = open("test.txt", "r+")
count = mfile.read()  # read all lines
count1 = mfile.read(4)  # read specific bites
print(count)
mfile.close()

# count symbols in text
print(len(count))

# Return one line
count = mfile.readline()  # read one line

# Return array of lines V1
count = mfile.readlines()  # read all lines

# Return array of lines V2
for line in mfile:
    print(line)

# Write in the file
# When a file is opened in write mode, the file's existing content is deleted.
file.write("This is new text")

# The write method returns the number of bytes written to a file, if successful.
file = open("test.txt", "w")
amount = file.write("This is new text")
print(amount)
file.close()

# It is good practice to avoid wasting resources by making sure that files are always closed after they have been used
# V1
try:
    f = open("test.txt")
    print(f.read())
finally:
    f.close()

# V2
with open("test.txt") as f:
   print(f.read())
