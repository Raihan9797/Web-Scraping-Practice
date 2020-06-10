## from the Letters From A Stoic, get each of the letter's links and the title of their article

import requests
import json
from bs4 import BeautifulSoup

source = requests.get('https://en.wikisource.org/wiki/Moral_letters_to_Lucilius').text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify)


# can't do json dump of beautifulsoup objects
# fn = 'letters_website.json'
# with open(letters_website, 'w') as f_obj:
    # json.dump(soup, f_obj)

fn = 'listofnamesandlinks.txt'

with open(fn, 'w') as f:
    for a2 in articles2:
        f.writelines(a2.text + '\n')
        f.writelines("https://en.wikisource.org/" + a2['href']  + '\n')


with open(fn) as f:
    lines = f.readlines()

print(lines)

for line in lines:
    print(line.rstrip())

# titles = []
# for i in range(0, len(lines), 2):
    # titles.append(lines[i].strip())
# 
# for t in titles:
    # print(t)

# links = []
# for i in range(1, len(lines), 2):
    # links.append(lines[i].strip())

# for l in links:
    # print(l)

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

# test = [1, 'a', 'hello', 2, 'b', 'bye']
# lol = uninterleave_lists(test, 3)

list_of_titles_and_links = uninterleave_lists(lines)
tt = list_of_titles_and_links[0]
ll = list_of_titles_and_links[1]
titles = [t.strip() for t in tt] # list of titles
links = [l.strip() for l in ll] # list of links



# obtaining the text from each link testing phase

introlink = links[0]
introsourcecode = requests.get(introlink).text
print(introsourcecode)

intro_soup = BeautifulSoup(introsourcecode, 'lxml')
print(intro_soup.prettify)

# forming the text as a whole
intro_texts = intro_soup.find_all('p')
text = ''
for t in intro_texts:
    text += t.text + '\n' # forms the full text
    print(t.text) # yes!!!
print(text)



################## text extractor #############
for i in range(0, 3):

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
    title = titles[i]
    file_name = f"{title}.txt"

    # save it to a .txt file
    with open(file_name, 'w') as fo:
        fo.write(link_text)

## i dont have the names of the letters

style="text-align:left;vertical-align:top;"
    



    





