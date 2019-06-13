# a simple and rustic download & parse tool
# -*- coding: utf-8 -*-

from urllib.request import urlopen

"""
A simplistic tool for fetching ADN sequences at ebi.ac.uk
"""

import ssl

def ebi_url(key):
    """
    default strategy to map a key to a URL
    """
    return 'https://www.ebi.ac.uk/ena/data/view/{key}&display=text&download=txt&filename={key}.txt'\
        .format(key=key)

def download(url, verbose=False):
    """
    the actual download - discards obvious failures
    """
    
    response = urlopen(url, context=ssl.SSLContext())
    text = response.read()
    if not isinstance(text, str):
        text = text.decode()
    if 'not supported' in text:
        print("WARNING: url=", url)
        print("  returned", text)
    if verbose:
        print("url=", url)
        print("text=", text)
    return text

def valid_contents(line):
    """
    keeps only the contents that has nucleotides
    """  
    return "".join( [ x.upper() for x in line if x.lower() in ('c', 'a', 'g', 't')])

def parse(text):
    """
    rough parsing of the .txt format
    """
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
    """
    one-stop shopping
    """
    url = ebi_url(key)
    try:
        return parse(download(url))
    except Exception as e:
        import traceback
        traceback.print_exc()
        print("Could not fetch key {} (exception {})".format(key, e))
        return str(e)

####################
# how to display our own source code
import inspect
def list_module(module):
    lines, lineno = inspect.getsourcelines(module)
    for line in lines:
        print(line, end="")
