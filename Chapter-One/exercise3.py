#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError



"""
    But, the server if the server could't bee founded, like a url
    misstiping, or something like that, we receive the URLError and
    not HTTPError. In this case, we need to improve the except:
"""

try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')