list_of_names_and_links = 'meta_letters/list_of_names_and_links.txt'

# get a list of names and links from .txt file
with open(list_of_names_and_links) as f:
    names_and_links = f.readlines() # list created

for line in names_and_links:
    print(line.rstrip())

# uninterleave the lists
def uninterleave_lists(lists, numtosplit = 2):
    list_of_lists = []
    for i in range(0, numtosplit):
        # print(i)
        gen_list = []
        for j in range(i, len(lists), numtosplit):
            # print(j)
            gen_list.append(lists[j])
        list_of_lists.append(gen_list)
    return list_of_lists

list_of_lists = uninterleave_lists(names_and_links)

names = list_of_lists[0]
links = list_of_lists[1]

# get a list of descriptions from .txt file
list_of_descriptions = 'meta_letters/list_of_descriptions.txt'

with open(list_of_descriptions) as f:
    descriptions = f.readlines() # list created

for description in descriptions:
    print(description.rstrip())

## JSON DUMPING OF LISTS  ###
descs_json = 'meta_letters/descriptions.json'
links_json = 'meta_letters/links.json'
names_json = 'meta_letters/names.json'

def json_dumper(data, filename):
    import json
    with open(filename, 'w') as fileobject:
        json.dump(data, fileobject)

json_dumper(descriptions, descs_json)
json_dumper(links, links_json)
json_dumper(names, names_json)


### dump name and desc into a txt file
names_and_descriptions = []
for i in range(0, len(names)):
    n = names[i]
    d = descriptions[i]
    nd = n.strip() + ' ' + d.strip()
    names_and_descriptions.append(nd)

fn = 'meta_letters/names and descriptions.txt'
with open(fn, 'w') as fo:
    for nd in names_and_descriptions:
        fo.writelines(nd + '\n')