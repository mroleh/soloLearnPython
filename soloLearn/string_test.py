all_camel_string = 'This Is Test String'
all_lower_string = 'this is test string'
all_caps_string = 'THIS IS TEST STRING'
decoded_string = 'My name is Ståle'
digit_string = '123456789'
digits_string_with_spaces = '  123456789  '
long_digit_string = '12312312376123861283617823'
part_one = "abc"
part_two = "def"
string_tuple = ('Apple', 'Orange', 'Blackberry')
string_array = "apple, banana, cherry"
string_with_new_line = "Thank you for the music\nWelcome to the jungle"


def capitalize():
    print(all_caps_string)
    print(all_caps_string.capitalize())


def casefold_test():
    print(all_caps_string)
    print(all_caps_string.casefold())
    # This method is similar to the lower() method


def upper_test():
    print(all_lower_string)
    print(all_lower_string.upper())


def swapcase_test():
    print(all_camel_string)
    print(all_camel_string.swapcase())


def lower_test():
    print(all_caps_string)
    print(all_caps_string.lower())


def center_test():
    print(digit_string)
    print(digit_string.center(20))
    # return the string in the center of setup length


def count_test():
    print(long_digit_string)
    print(long_digit_string.count('1', 1))
    # It is possible to add  parameter start and end to count in the defined length


def encode_test():
    print(decoded_string)
    print(decoded_string.encode())
    print(decoded_string.encode(encoding="ascii", errors="backslashreplace"))


def find_test():
    print(long_digit_string)
    symbol_to_find = '1'
    print(long_digit_string.find(symbol_to_find))
    # The find() method is almost the same as the index() method,
    # the only difference is that the index() method raises an exception if the value is not found.
    print(long_digit_string.rfind(symbol_to_find))


def format_string():
    new_string = "For only {price:.2f} dollars {day}!"
    print(new_string.format(price=49, day='today'))


def formatted_string():
    price = 49
    day = 'today'
    print(f"For only {price:.2f} dollars {day}!")


def isdigit_test():
    print(digit_string)
    print(digit_string.isdigit())


def isspace_test():
    print(all_lower_string)
    print(all_lower_string.isspace())


def join_test():
    print(string_tuple)
    print(" ".join(string_tuple))


def just_test():
    print(digit_string)
    print(digit_string.ljust(20))
    print(digit_string.rjust(20))


def strip_test():
    print(digits_string_with_spaces)
    print(digits_string_with_spaces.strip())
    print(digits_string_with_spaces.lstrip())
    print(digits_string_with_spaces.rstrip())


def split_test():
    print(string_array)
    print(string_array.split(", "))
    print(all_lower_string)
    print(all_lower_string.split(' '))


def splitlines_test():
    print(string_with_new_line)
    print(string_with_new_line.splitlines())


def partition_test():
    print(all_lower_string)
    print(all_lower_string.partition('st'))
    print(all_lower_string.rpartition('st', ))


def replace_test():
    print(all_lower_string)
    print(all_lower_string.replace("t", "1"))


upper_test()
swapcase_test()
