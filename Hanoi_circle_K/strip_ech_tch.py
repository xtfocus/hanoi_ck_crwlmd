import re

tch = re.compile(r'&tch=\d+')
ech = re.compile(r'&ech=\d+')

def strip_ech_tch(string):
    
    e = ech.findall(string)[0]
    t = tch.findall(string)[0]
    
    return string.replace(e,'').replace(t,'')