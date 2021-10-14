file = open("../test.txt")
file_line = file.readlines()
print(file_line)

for i in range(len(file_line)):
    if file_line[i].__contains__('\n'):
        temp_book_name = file_line[i][0] + str(len(file_line[i]) - 1)
        print(temp_book_name)
    else:
        temp_book_name = file_line[i][0] + str(len(file_line[i]))
        print(temp_book_name)

file_line[0].find()
