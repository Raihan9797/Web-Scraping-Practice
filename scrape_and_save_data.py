from bs4 import BeautifulSoup
import requests

# get main page source code
source = requests.get('https://en.wikisource.org/wiki/Moral_letters_to_Lucilius').text

# convert to soup
soup = BeautifulSoup(source, 'lxml')
print(soup.prettify)

## find the table of links, names and descriptions

# searching via the 'a' which is the link tag.
# also used regex to make sure that the links is related to the letters!
import re
links_source_code = soup.find_all('a', {'title': re.compile(r'^Moral letters')})

for link_source_code in links_source_code:
    print(link_source_code.text)
    print(link_source_code['href']) # wow this works!

# the links are not exactly accessible. It doesn't start with 'https://' etc. we need to append that
wikisource_http = "https://en.wikisource.org/"

# i need to write all these links to a .txt file so that i don't have to keep requesting.
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

# print(lines)

for line in lines:
    print(line.rstrip())


## although i have the link and link names, i still havent found the descriptions

## i might be able to get the title from here!
## ok no they are not the same
# for link_source_code in links_source_code:
    # print(link_source_code.text)
    # print(link_source_code['href'])
    # print(link_source_code['title']) # doesnt work
    # print(link_source_code)

## wrong choices; going deeper into the code
# <td style="text-align:left;vertical-align:top;">On saving time </td>
# soup.find('td', style = "text-align:left")
# soup.find('div', class_='mw-parser-output')
# soup.find('table') # wrong table, i think because there is another table on top

table_soup = soup.find('table', align = "center")
type(table_soup) # still a soup element. This means we can start our search from here instead of all the way from the main source code

## the text that you want
# <tr>
# <td style="text-align:right;padding-right:1.0em;"><a href="/wiki/Moral_letters_to_Lucilius/Letter_19" title="Moral letters to Lucilius/Letter 19">Letter 19</a> </td>

# <td style="text-align:left;vertical-align:top;">On worldliness and retirement</td>
# </tr>>


# x = table_soup('td', style="text-align:left;vertical-align:top;")
# type(table_soup) # bs4.element.Tag
# type(x) # bs4.element.ResultSet
## it's actually kind of like a list. see the output: [...] BUT THATS BECAUSE YOU DIDNT USE FINDALL()

table_desc_soup = table_soup.find_all('td',style="text-align:left;vertical-align:top;")
type(table_desc_soup) # SAME! find_all returns a ResultSet

## trying to extract the description from the soup
# descriptions = []
# for td in table_desc_soup:
    # print(td.text.strip()) # got it
    # there are 3 /n at the end because the last 3 titles do not have descriptions
    # also the same for the first desc


filename_desc = 'list_of_descriptions.txt'

with open(filename_desc, 'w') as fileobject:
    for td in table_desc_soup:
       fileobject.writelines(td.text.strip() + '\n')
    