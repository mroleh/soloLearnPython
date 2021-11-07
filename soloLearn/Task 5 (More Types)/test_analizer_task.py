def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("Enter a filename: ")

with open("C:\\Users\\Newfire\\Documents\\soloLearnPython\\soloLearn\\" + filename) as f:
    text = f.read()

print(text)

print("The character is shown in text '" + str(count_char(text, "r")) + " times")

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
