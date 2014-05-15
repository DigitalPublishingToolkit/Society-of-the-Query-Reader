import html5lib, sys
from xml.etree import ElementTree as ET 


tree = html5lib.parse(sys.stdin.read().decode("utf-8"), namespaceHTMLElements=False)

def filtertext(t):
    if t == None:
        return None
    return t.replace("\n", " ")

# STOP = "script pre code style".split()
PROCESS = "p sub li a em".split()

def process (elt):
    # if elt.tag in STOP:
    #     return
    # print elt.tag
    if elt.tag in PROCESS:
        elt.text = filtertext(elt.text)
        elt.tail = filtertext(elt.tail)
    for child in elt:
        process(child)

process(tree)
sys.stdout.write(ET.tostring(tree).encode("utf-8"))

