#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

"""
If the page has been successfully received, exist the problem of the
content of page doesn't bee exaclty what we want, yet.

Improve the code with verification of existence of tag scraped
is more smart idea. If we try to access a tag that has doesn't exist,
we receive a none object. The problem is: try to access one tag in
none object result in launch a AttributeError.
In the code below, we try to access a 'nonExistentTag' for reproduce
that problem. We need to treat this object and not proceed trying to
call other function in none object. Let's go to see this in practice:
"""

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')

try:
    badContent = bs.nonExistentTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found2')
    else:
        print(badContent)
