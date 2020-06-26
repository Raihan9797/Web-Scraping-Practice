import json

def json_loader(filename):
    with open(filename) as file_object:
        return json.load(file_object)

fn1 = 'all_letters/dict_0to10.json'
fn2 = 'all_letters/dict_11to20.json'
fn3 = 'all_letters/dict_21to30.json'

dict_0to10 = json_loader(fn1)
dict_11to20 = json_loader(fn2)
dict_21to30 = json_loader(fn3)

test = dict_0to10
test.update(dict_11to20)
test.keys()

test.update(dict_21to30)
test.keys()

fn = 'practice/thirty_letters.json'
with open(fn, 'w') as fo:
    json.dump(test, fo, indent=4)