# -*- coding:utf-8 -*`-
import os
import glob
import codecs
from bs4 import BeautifulSoup

indent_1 = 0
indent_2 = 0
indent_3 = 0

def out_format(format_type, text, indent):
    
    if 'FreeStyleWIki'.upper() == format_type.upper():
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
    
    elif 'html'.upper() == format_type.upper():
        global indent_1
        global indent_2
        global indent_3

        style = ''
        prefix = ''
        if indent < 4:
            tag = 'h%d' % (indent + 1)
            
            if indent == 1:
                indent_1 = indent_1 + 1
                prefix = "%d" % (indent_1)
                indent_2 = 0
                indent_3 = 0
            elif indent == 2:
                indent_2 = indent_2 +1
                prefix = "%d.%d" % (indent_1, indent_2)
                indent_3 = 0
            elif indent == 3:
                indent_3 = indent_3 + 1
                prefix = "%d.%d.%d" % (indent_1, indent_2, indent_3)
        else:
            tag = 'p'
            prefix = '-'
            
        if indent > 1:    
            style = ' style="text-indent:%dem"' % ((indent-1))    
        return '<%s%s>%s %s</%s>\r\n' % (tag, style, prefix,text, tag)
    

def parse(out, node, indent, format_type):
    try:
        out.write(out_format(format_type, node['text'], indent))
    except KeyError:
        return

    indent = indent + 1
    for child in node.contents:
        parse(out, child, indent, format_type)

def meke_formatted_text(path, format_type):

    mms = glob.glob(os.path.join(path, "*.mm"))
    for mm in mms:
        out = codecs.open(mm + ".out.txt", 'w', 'utf-8')
        soup = BeautifulSoup(open(mm))
        parse(out,soup.map.contents[0],1,format_type)
        out.close()
        
if __name__ == '__main__':
    target = os.path.join(os.path.expanduser('~'), 'Dropbox\Private\Maindmap\FreeMindFormat')
    meke_formatted_text(target, 'html')
    print "finish"
    