import os, json

### get all json files from all_letters folder
path_to_json = 'all_letters/'
files = os.listdir(path_to_json)
json_files = [f for f in files if f.endswith('.json')]
json_files.sort() ### sort() is not NATURAL SORT
# because they are strings, 0to10 < 111to125 < 11to20 ...
print(json_files)


### natural sort the json file names
import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

sorted_json_files = sorted_alphanumeric(json_files)
sorted_json_files

### load the json files in a list
letters_dict = {}
for filename in sorted_json_files:
    with open(path_to_json + filename) as json_fileobject:
        letters_dict.update(json.load(json_fileobject))

letters_dict.keys()   

### dump the entire letter dict into a json
fn = 'all_letters/dict_all_letters.json'
with open(fn, 'w') as fo:
    json.dump(letters_dict, fo)
