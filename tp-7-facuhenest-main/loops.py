def index_of_by_index(word, strings, start_index):
    index = start_index
    while index < len(strings):
        if word == strings[index]:
            return index
        index += 1 
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_by_index("Black", colors, 1))  
print(index_of_by_index("Black", colors, 4)) 
print(index_of_by_index("Green", colors, 2))  


def index_of_empty(strings):
    index = 0
    while index < len(strings):
        if strings[index] == "":
            return index
        index += 1 
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of_empty(colors)) 

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(index_of_empty(colors))  

def index_of(word, strings):
    index = 0
    while index < len(strings):
        if word == strings[index]:
            return index
        index += 1
    return -1

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(index_of("Black", colors))  
print(index_of("Blue", colors))  
 

def put(word, strings):
    index = 0
    while index < len(strings):
        if strings[index] == "":
            strings[index] = word
            return index
        index += 1
    return -1

colors = ["Red", "Green", "", "", "Pink", "", "Black"]
print(put("Blue", colors))  

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(put("Blue", colors))  



def remove(word, strings):
    index = 0
    eliminations = 0
    while index < len(strings):
        if word == strings[index]:
            strings[index] = ""
            eliminations += 1
        index += 1
    return eliminations

colors = ["Red", "Green", "White", "Black", "Pink", "Yellow", "Black"]
print(remove("Black", colors)) 
print(remove("Blue", colors))  


