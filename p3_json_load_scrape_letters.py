"""This uses the links from the .txt files to access each letter and scrape them to be saved."""

##### load json lists #####
def json_loader(filename):
    import json
    with open(filename) as file_object:
        return json.load(file_object)

descs_json = 'meta_letters/descriptions.json'
links_json = 'meta_letters/links.json'
names_json = 'meta_letters/names.json'

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



test_dict = {}
##### letter extractor #####
def extract_letter_range(start, end):
    from bs4 import BeautifulSoup
    import requests

    for i in range(start ,end):
        # get source code from the link
        link_source_code = requests.get(links[i]).text

        # get prettified soup
        link_soup = BeautifulSoup(link_source_code, 'lxml')

        # get title name and description
        name = names[i]
        desc = descriptions[i]
        name_and_desc = f"{name}: {desc}"
        nd = name + " " + desc

        # extract text from the soup
        # add the name and description to the top of the text
        link_soup_texts = link_soup.find_all('p')
        text_list = []
        link_text = name_and_desc + "\n \n"
        text_list.append(link_text)
        for t in link_soup_texts:
            link_text += t.text + '\n'
            text_list.append(t.text + '\n')
        
        # add list to dict
        test_dict[i] = text_list

        # save it to a .txt file using its name and desc
        file_name = f"all_letters/{nd}.txt"
        with open(file_name, 'w') as fo:
            fo.write(link_text)

extract_letter_range(0, 11)

fn = 'all_letters/dict_0to10.json' # keep changing the file names based on the range of letters extracted

def json_dumper(data, filename):
    import json
    with open(filename, 'w') as fileobject:
        json.dump(data, fileobject)

json_dumper(test_dict, fn)