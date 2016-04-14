# a simple and rustic download & parse tool
# -*- coding: utf-8 -*-

from __future__ import print_function

import urllib2

def download(key, verbose=False):
    
    url = 'http://www.ebi.ac.uk/ena/data/view/{key}&display=text&download=txt&filename={key}.txt'\
          .format(key=key)

    response = urllib2.urlopen(url)
    text = response.read()
    if 'not supported' in text:
        print("WARNING: url=", url)
        print("  a retourné", text)
    if verbose:
        print("url=", url)
        print("text=", text)
    return text

def valid_contents(line):
    return "".join( [ x.upper() for x in line if x.lower() in ('c', 'a', 'g', 't')])

def parse(text):
    in_sequence = False
    result = ""
    for line in text.split("\n"):
        start = line[:2]
        if start == 'SQ':
            in_sequence = True
        elif start == '  ' and in_sequence:
            result += valid_contents(line)
        elif start == '//':
            in_sequence = False
    return result
        
def fetch(key):
    return parse(download(key))
