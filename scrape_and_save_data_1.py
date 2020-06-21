from bs4 import BeautifulSoup
import requests

##### GET MAIN PAGE SOURCE CODE #####
source = requests.get('https://en.wikisource.org/wiki/Moral_letters_to_Lucilius').text

##### CONVERT TO SOUP #####
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify)

##### FIND TABLE OF LINKS NAMES AND DESCRIPTIONS #####

# searching via the 'a' which is the link tag.
# also used regex to make sure that the links is related to the letters!
import re
links_source_code = soup.find_all('a', {'title': re.compile(r'^Moral letters')})

for link_source_code in links_source_code:
    print(link_source_code.text)
    print(link_source_code['href'])

# the links are not exactly accessible. It doesn't start with 'https://' etc. we need to append that
wikisource_http = "https://en.wikisource.org/"

##### WRITE ALL THE LINKS TO .TXT FILE SO I DONT HAVE TO KEEP REQUESTING #####
fn = 'list_of_names_and_links.txt'
with open(fn, 'w') as fo:
    for link_source_code in links_source_code:
        # print(link_source_code.text)
        fo.writelines(link_source_code.text + '\n')
        # print(link_source_code['href'])
        fo.writelines(wikisource_http + link_source_code['href']  + '\n')


# now that i've saved that file. time to extract it
with open(fn) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())


##### GETTING DESCRIPTIONS #####

## i might be able to get the title from here!
table_soup = soup.find('table', align = "center")
type(table_soup) # still a soup element. This means we can start our search from here instead of all the way from the main source code

table_desc_soup = table_soup.find_all('td',style="text-align:left;vertical-align:top;")
type(table_desc_soup) # SAME! find_all() returns a ResultSet

##### EXTRACT DESCRIPTIONS FROM SOUP #####

for td in table_desc_soup:
    print(td.text.strip()) # got it
# there are 3 /n at the end because the last 3 titles do not have descriptions. also the same for the first desc

filename_desc = 'list_of_descriptions.txt'
with open(filename_desc, 'w') as fileobject:
    for td in table_desc_soup:
       fileobject.writelines(td.text.strip() + '\n')
    