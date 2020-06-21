import all_letters

##### make sure to use 'r' when you want to read a file!

##### load json lists #####
def json_loader(filename):
    import json
    with open(filename) as file_object:
        return json.load(file_object)

descs_json = 'all_letters/descriptions.json'
links_json = 'all_letters/links.json'
names_json = 'all_letters/names.json'

descriptions = json_loader(descs_json)
names = json_loader(names_json)
links = json_loader(links_json)



##### strips the lists of '\n' ######
def strip_lists(list_name):
    l = []
    for item in list_name:
        l.append(item.strip())
    return l

links = strip_lists(links)
names = strip_lists(names)
descriptions = strip_lists(descriptions)

def list_letter_names():
    """Returns a list of letters names and descriptions"""
    for i in range(0, len(names)):
        name = names[i]
        desc = descriptions[i]
        name_and_desc = f"{name}_{desc}"
        print(name_and_desc)

list_letter_names()

def get_letter(lettername):
    """Prints out the letter which was requested"""
    letter_number = names.index(lettername.title())
    name = names[letter_number]
    desc = descriptions[letter_number]
    filename = f'all_letters\{name}_{desc}.txt'
    with open(filename, 'r') as fo:
        lines = fo.readlines()
    for l in lines:
        print(l)

get_letter("introduction")