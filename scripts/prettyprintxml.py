#!/usr/bin/env python
"""
Copyright 2014 Michael Murtaugh
Released under a GPL3 License. See LICENSE.

"""
import sys, html5lib
from xml.etree import ElementTree as ET


def indent(elem, level=0):
    """ source: http://effbot.org/zone/element-lib.htm#prettyprint """
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def prettyprint (src, method="xml"):
    t = html5lib.parse(src, namespaceHTMLElements=False)
    indent(t)
    return ET.tostring(t, method=method)

if __name__ == "__main__":
    print prettyprint(sys.stdin.read().decode("utf-8"), method="html").encode("utf-8")

