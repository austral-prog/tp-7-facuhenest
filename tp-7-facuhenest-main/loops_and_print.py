def enumerate_list(list):
    new_list = []
    index_new = 0
    for current_elem in list:
        if current_elem != "":
            new_list.append(f"{index_new}. {current_elem}")
            index_new += 1
    return new_list



def enumerate_backwards(list):
    new_list = []
    index_new = 0
    for current_elem in list:
        if current_elem != "":
            new_list.append(f"{index_new}. {current_elem[::-1]}")
            index_new += 1
    return new_list
