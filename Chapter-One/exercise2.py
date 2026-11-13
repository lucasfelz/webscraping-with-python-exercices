#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


"""
The example below is used when we wish to pass 404 errors or 500
class errors. In these cases, the function urlopen launch the generic
exempt 'HTTPError'.
"""

# If is it a completly new programm, we need to do:
# from urlib.request import urlopen
# from urllib.error import HTTPError

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # return null in this case, exec a break or other plan if you have
else:
    print('nothing to do')

"""
    Continue.. Obs: if we use a break in this except, doesn't
    necessary to use else instruction
    If an error has been returned, the programm don't exec the
    rest of programm in else instruction.
"""