def enumerate_list(strings):
    new_list = []
    for index, current_elem in enumerate(strings):
        if current_elem:
            new_list.append(f"{index}. {current_elem}")
    return new_list

colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_list(colors))  



def enumerate_backwards(strings):
    new_list = []
    for index, current_elem in enumerate(strings):
        if current_elem:
            new_list.append(f"{index}. {current_elem[::-1]}")
    return new_list

colors = ["Red", "Green", "", "White", "Black"]
print(enumerate_backwards(colors))  
