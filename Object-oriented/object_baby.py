#!/usr/bin/python

import urllib

def wget(url):
    try:
        text = urllib.urlopen(url)
        if text.info().gettype() == 'text/html':
            print text.read()
    except IOError:
        print "could not access", url
        
        
wget("http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/100-most-popular-boys-names-so-far-in-2018")        