# -*- coding:utf-8 -*`-
import os
import glob
import codecs
from bs4 import BeautifulSoup

def freeStyleWiki(text, indent):
    prefix = ""
    if indent == 1:
        prefix = "!!!"
    elif indent == 2:
        prefix = "!!"
    elif indent == 3:
        prefix = "!"
    elif indent == 4:
        prefix = "::"
    elif indent == 5:
        prefix = "*"
    elif indent == 6:
        prefix = "**"
    
    return '%s%s\r\n' % (prefix, text)

def parse(out, node, indent):
    
    try:
        out.write(freeStyleWiki(node['text'], indent))
    except KeyError:
        return

    indent = indent + 1
    for child in node.contents:
        parse(out, child, indent)

def meke_formatted_text(path):
    mms = glob.glob(os.path.join(path, "*.mm"))
    for mm in mms:
        out = codecs.open(mm + ".out.txt", 'w', 'utf-8')
        soup = BeautifulSoup(open(mm))
        parse(out,soup.map.contents[0],1)
        out.close()
        
if __name__ == '__main__':
    target = 'C:\Users\piroto\Dropbox\Private\Maindmap\FreeMindFormat'
    meke_formatted_text(target)
    print "finish"
    