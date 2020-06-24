### trying to store the letters in a dict where key: letter number and value: the full letter


### first, load the names and descriptions
def json_loader(filename):
    import json
    with open(filename) as file_object:
        return json.load(file_object)

descs_json = 'descriptions.json'
links_json = 'links.json'
names_json = 'names.json'

descriptions = json_loader(descs_json)
names = json_loader(names_json)
links = json_loader(links_json)

for x in names:
    print(x)

len(names)
len(descriptions)
len(links)

names_and_descriptions = []
for i in range(0, len(names)):
    if descriptions[i] == "\n":
        # print(names[i].strip() + " " + names[i].strip())
        names_and_descriptions.append(names[i].strip() + " " + descriptions[i].strip())
    else:
        # print(names[i].strip() + " " + descriptions[i].strip())
        names_and_descriptions.append(names[i].strip() + " " + descriptions[i].strip())

for nd in names_and_descriptions:
    print(nd)

test_dictionary = {}
for i in range(0, 31):
    nd = names_and_descriptions[i]
    filename = f"all_letters/{nd}.txt"
    with open(filename, 'r') as fo:
        text = fo.read()
        # print(text)
        test_dictionary[i] = text


print(test_dictionary[1])
test_dictionary
test_dictionary[int("1")]

test_dictionary.keys()

fn = "practice/test_dict.json"
import json
with open (fn, 'w') as fo:
    json.dump(test_dictionary, fo)