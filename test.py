def list_uppercase(words):
    word_list = []

    for word in words:
        word_list.append(word.upper())

    return word_list

print(list_uppercase(["hello", "john", "holly" ]))