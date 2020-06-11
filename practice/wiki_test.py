# practicing using the wikipedia API. Doesn't seem to lead anywhere for me because i dont really know how to access Wikisource through this API

import wikipedia as wk

print(wk.search("Programming"))

print(wk.summary("Android"))

print(wk.summary("Android", sentences=3))

print(wk.search("Seneca"))

print(wk.page("Seneca the Younger"))

seneca = (wk.page("Seneca the Younger"))
print(seneca.content)

wk.search("Letters from a Stoic")
wk.page("Epistulae Morales ad Lucilium").links


