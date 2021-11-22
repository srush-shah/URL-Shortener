# Shortening URL using an API

from __future__ import with_statement
import contextlib

try:
    from urllib.parse import urlencode

except ImportError:
    from urllib import urlencode

try:
    from urllib.request import urlopen

except ImportError:
    from urllib3 import urlopen

import sys


# function to shorten the URL
def make_tiny(url):
    req_url = ('http://tinyurl.com/api-create.php?'+urlencode({'url':url}))
    with contextlib.closing(urlopen(req_url)) as res:
        return res.read().decode('utf-8')


for tinyurl in map(make_tiny, sys.argv[1:]):
    print(tinyurl)


# Run the program with the following command:
# python url-shortener.py <long_url_1> <long_url_2> etc...