def index_of_by_index(word, strings, start_index):
    index = start_index
    while index < len(strings):
        if word == strings[index]:
            return index
        index += 1 
    return -1



def index_of_empty(strings):
    index = 0
    while index < len(strings):
        if strings[index] == "":
            return index
        index += 1 
    return -1



def index_of(word, strings):
    index = 0
    while index < len(strings):
        if word == strings[index]:
            return index
        index += 1
    return -1


def put(word, strings):
    index = 0
    while index < len(strings):
        if strings[index] == "":
            strings[index] = word
            return index
        index += 1
    return -1




def remove(word, strings):
    index = 0
    eliminations = 0
    while index < len(strings):
        if word == strings[index]:
            strings[index] = ""
            eliminations += 1
        index += 1
    return eliminations


