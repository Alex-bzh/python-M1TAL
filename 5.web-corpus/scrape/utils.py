#!/usr/bin/env python
#-*- coding: utf-8 -*-

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

def parse_html_by_class(html, selector):
    """Extracts tags from HTML whith CSS selector.
    
    Keyword arguments:
    html -- the html page
    selector -- the CSS selector
    """
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.select(selector)

    return tags

if __name__ == '__main__':
    """Usage example.
    Works only when used as standalone.
    """
    url = "http://www.llf.cnrs.fr/ita/"
    html = get_html_from_url(url)
    anchors = parse_html_by_class(html, '.liste-membres .field-content a')
    for anchor in anchors:
        print(anchor.get_text())
