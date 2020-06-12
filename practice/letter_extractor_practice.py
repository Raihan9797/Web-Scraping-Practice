# you need to make sure that requests takes in full links and not '\n'

########## letter extractor practice #########
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

