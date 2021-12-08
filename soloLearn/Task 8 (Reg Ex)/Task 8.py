# Regular Expressions
# They are useful for two main tasks:
# - verifying that strings match a pattern (for instance, that a string has the format of an email address),
# - performing substitutions in a string (such as changing all American spellings to British ones).

# After you've defined a regular expression, the re.match function can be used to determine whether
# it matches at the beginning of a string.
# If it does, match returns an object representing the match, if not, it returns None.
# To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    # The function re.search finds a match of a pattern anywhere in the string.
    print("Match")
else:
    print("No match")

# The function re.findall returns a list of all substrings that match a pattern.
print(re.findall(pattern, "eggspamsausagespam"))
# The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.


# The regex search returns an object with several methods that give details about it.
pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())  # group which returns the string matched
    print(match.start())  # start and end which return the start and ending positions of the first match
    print(match.end())
    print(match.span())  # span which returns the start and end positions of the first match as a tuple

# One of the most important re methods that use regular expressions is sub.
# This method replaces all occurrences of the pattern in string with repl,
# substituting all occurrences, unless count provided. This method returns the modified string.

str1 = "My name is David. Hi David."
pattern = r"David"
newstr1 = re.sub(pattern, "Amy", str1)
print(newstr1)

# Metacharacters
# Metacharacters are what make regular expressions more powerful than normal string methods.
# r"..." - search word that have 3 symbols
# r"..!$" - word that have 3 symbols and and with !

# The first metacharacter we will look at is . (dot).
# This matches any character, other than a new line.
pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

# The next two metacharacters are ^ and $.
# These match the start and end of a string, respectively.
pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

