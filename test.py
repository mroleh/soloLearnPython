celsius = int(input())


def conv(c):
    # your code goes here
    far_value = 9 / 5 * c + 32
    return far_value

fahrenheit = conv(celsius)
print(fahrenheit)
