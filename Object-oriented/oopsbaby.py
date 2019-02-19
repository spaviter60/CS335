#!/usr/bin/python
import urllib
import re
import sys
class BabyNames :
    def __init__(self,year):
        self.year = year
        print year
    def Retrieve_Names(self, url):
        print url
        Text = urllib.urlopen(url)
        if Text.info().gettype() == 'text/html':
            Bnames = re.findall(r'<ol>(.*?)</ol>', Text.read())
        print Bnames   
        self.names = url
    def printNames(self):
        print self.names
        
def main():
    args = sys.argv[1:]
    if not args:
        print 'usage: [--summaryfile] url'
        sys.exit(1)
    
    summary = False
    
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    try:
        text = urllib.urlopen(args[0])
        if text.info().gettype() == 'text/html':
            years = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
            Little = years[0].split('"')
            Little2 = years[1].split('"')
            Final = []
            i = 0
            for element in Little:
                if i % 2 == 1:
                    Final.append(element)
                i = i + 1 
            i = 0
            for element in Little2:
                if i % 2 == 1:
                    Final.append(element)
                i = i + 1     
            Url = args[0]
            URL = Url.split('/')
            strn = ''
            strn = URL[0]+'//'+URL[2]
            URLList = [strn + x for x in Final]
            Year = []
            for yearURL in URLList:
                YEar = re.findall(r'-(\d{4})', yearURL)
                Year.append(YEar)
                i =0 
            for Years in Year:    
                bn = BabyNames(Years)
                bn.Retrieve_Names(URLList[i])
                bn.printNames
                i = i + 1
    except IOError:
        print "Could not access"
if __name__ == '__main__':
  main()