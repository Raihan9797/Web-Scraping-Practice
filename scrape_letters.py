"""This uses the links from the .txt files to access each letter and scrape them to be saved."""

# import json

# test = 'practice/test.json'
# with open(test) as file_object:
    # descriptions = json.load(file_object)

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

# strips the links with '\n'
def strip_lists(list_name):
    l = []
    for item in list_name:
        l.append(item.strip())
    return l

links = strip_lists(links)
names = strip_lists(names)


########## text extractor practice #########
from bs4 import BeautifulSoup
import requests

for i in range(0, 2):

    # get source code from the link
    link_source_code = requests.get(links[i]).text

    # get prettified soup
    link_soup = BeautifulSoup(link_source_code, 'lxml')
    print(link_soup.prettify)

    # extract text from the soup
    link_soup_texts = link_soup.find_all('p')
    link_text = ''
    for t in link_soup_texts:
        link_text += t.text + '\n'
    print(link_text)

    # get title name
    name = names[i]
    file_name = f"all_letters/{name}.txt"

    # save it to a .txt file
    with open(file_name, 'w') as fo:
        fo.write(link_text)

