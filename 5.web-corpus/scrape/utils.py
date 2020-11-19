#!/usr/bin/env python
#-*- coding: utf-8 -*-

#
#   Modules to import
#
import urllib.request
from bs4 import BeautifulSoup

def get_html_from_url(url, charset='utf-8'):
    """Extracts the HTML code from a single URL.
    
    Keyword arguments:
    url -- the url to scrape
    charset -- charset used to decode caracters
    """
    headers = { 'User-agent' : 'HTML extractor (Alexandre Roulois)' }
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request) as f:
        html = f.read().decode(charset)
    return html
