#!/usr/bin/env python
#!/usr/bin/env python
"""
Copyright 2014 Michael Murtaugh
Released under a GPL3 License. See LICENSE.

"""
from __future__ import print_function
import sys, html5lib
from xml.etree import ElementTree as ET


def nbstrip (text):
    """ Whitespace stripper that also works on &nbsp; """
    return text.replace("&#160;", " ").replace("&nbsp;", " ").strip()

def iterparent(tree):
    """ http://effbot.org/zone/element.htm#accessing-parents """
    for parent in tree.getiterator():
        for child in parent:
            yield parent, child

def iterparentandprev(tree):
    for parent in tree.getiterator():
        prev = None
        for child in parent:
            yield parent, prev, child
            prev = child

def remove_with_tail (parent, prev, elt):
    """ ElementTree remove that deals with relocating elt's tail which if nonempty, is appended to either prev.tail or parent.text"""
    if elt.tail != None and elt.tail != "": # MOVE THAT TAIL
        if prev:
            prev.tail = (prev.tail or "") + elt.tail
        else:
            parent.text = (parent.text or "") + elt.tail
    parent.remove(elt)

# ? generalize to striptags with strip_p predicate?
def stripemptytags (src, method="xml", empty=lambda x: x.replace("&#160;", " ").strip() == ""):
    """ applies the empty predicate to each element, and removes the element when empty is true;
    NB: This function preserves whitespace and other wrapped textual content,
    only the tag itself is removed as elt.text gets unwrapped from the element
    """
    t = html5lib.parse(src, namespaceHTMLElements=False)
    for parent, prev, elt in iterparentandprev(t):
        if elt.text != None and len(elt) == 0:
            if empty(elt.text):
                # log(u"removing empty tag {0}".format(ET.tostring(elt, method=method)))
                elt.tail = elt.text + (elt.tail or "")
                remove_with_tail(parent, prev, elt)
    return ET.tostring(t, method=method)

if __name__ == "__main__":
    print(stripemptytags(sys.stdin.read().decode("utf-8"), method="html").encode("utf-8"))

