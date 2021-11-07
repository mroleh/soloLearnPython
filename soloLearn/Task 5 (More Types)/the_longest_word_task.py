text = input()

word_list = text.split(" ")
print(word_list)

max_len_word = word_list[0]
for i in range(len(word_list)):
    if len(max_len_word) < len(word_list[i]):
        max_len_word = word_list[i]
print(max_len_word)
