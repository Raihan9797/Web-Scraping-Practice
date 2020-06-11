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
