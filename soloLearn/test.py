import codecs

error_list = ['192810', 'acb123/*-#', 'ABC123abc /*-+#$%&_"']
print(error_list)


def decode_list():
    for i in range(len(error_list)):
        error_list[i] = codecs.decode(error_list[i], 'unicode-escape')

    return error_list


def decode_list1():
    for item in error_list:
        item = (item, codecs.decode(item, 'unicode-escape'))

    return error_list


def decode_list2():
    result = []
    for item in error_list:
        result.append(codecs.decode(item, 'unicode-escape'))
    return result


# new_list = codecs.decode(error_list[0], 'unicode-escape')


# print(decode_list())

print(decode_list1())
