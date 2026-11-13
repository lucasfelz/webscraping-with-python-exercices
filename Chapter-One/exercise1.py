#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
print(bs.html.body.h1)
print(bs.body.h1)
print(bs.html.h1)

"""
Remember, we can use lxml or html5lib instead html.parser.
We can install lxml with pip3 install lxml and html5lib with
pip3 install html5lib.

In general, the html5lib and lxml perform better against 
malformed or poorly writtten HTML pages
"""

"""
The example below is used when we wish to pass 404 errors or 500
class errors. In these cases, the function urlopen launch the generic
exempt 'HTTPError'.
"""

# If is it a completly new programm, we need to do:
# from urlib.request import urlopen
# from urllib.error import HTTPError
"""
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null in this case, exec a break or other plan if you have
else:
"""

"""
    Continue.. Obs: if we use a break in this except, doesn't
    necessary to use else instruction
    If an error has been returned, the programm don't exec the
    rest of programm in else instruction.
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






