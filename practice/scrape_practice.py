# installed beautifulsoup4, lxml and requests
# he also reccs html5lib to replace lxml but whatever

from bs4 import BeautifulSoup
import requests

# with open('view-source:https://en.wikisource.org/wiki/Moral_letters_to_Lucilius') as html_file:
#    soup = BeautifulSoup(html_file, 'lxml')


source = requests.get('https://en.wikisource.org/wiki/Moral_letters_to_Lucilius').text

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify)

body_content = soup.find('mw-body-content')

print(body_content.prettify())

## restart
a = soup.find('div')
print(a) # returns first 'div'

b = soup.find('body')
print(b)

c = soup.find('content')
print(c) # none

d = soup.find('div', style ='text-align:right')
print(d) # none

e = soup.find('div')
print(e) # returns first div
# this means no div with that style attribute

f = soup.find('div', style ='text-align:right;padding-right:1.0em;')
print(f) # also none, which means that 'd' was not specific!

g = soup.find('td', style = 'text-align:right;padding-right:1.0em;')
print(g) # this is what we want!!!
print(g.text.strip()) # get the name without /n

list_of_articles = soup.find_all('td', style = 'text-align:right;padding-right:1.0em;')
for articles in list_of_articles:
    print(articles.text.strip())

g
g.a # gives you the link!
# not quite the link but yes it contains the link

intro_source = requests.get(g.a).text # missingschema error
# happens because you are taking the entire line and not giving an actual link!
g.a('href')

g2 = soup.find('a', title = '^Moral letters to Lucilius')

import re
g3 = soup.find('a', {'title': re.compile(r'^Moral letters')})
print(g3.text)
print(g3)
# now we are searching directly for the links and the titles

articles2 = soup.find_all('a', {'title': re.compile(r'^Moral letters')})

for a2 in articles2:
    print(a2.text)
    print(a2['href']) # wow this works!

## now trying to check if the href links works!
introlink = g3['href']
introlink


introlink = "https://en.wikisource.org/" + introlink

introv2 = requests.get(introlink).text
print(introv2)

#intro_soup = soup('lxml', introv2)
intro_soup = BeautifulSoup(introv2, 'lxml')
intro_soup
print(intro_soup.prettify)

intro_soup.find('div', {'id':'mw-content-text'})

intro_soup.find('div', lang = 'en')

intro_soup.find('div', class_ = 'mw-parser-output')

print(intro_soup.find('div', class_ = 'mw-parser-output').p.text)


# print(intro_soup.find(text=True).text)

intro_texts = intro_soup.find_all('p')
for t in intro_texts:
    print(t.text) # yes!!!
