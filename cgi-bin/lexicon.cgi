#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
import cgitb; cgitb.enable()
import cgi, urllib
from xml.sax.saxutils import quoteattr


f = cgi.FieldStorage()
q = f.getvalue("q", "").decode("utf-8").strip()
print "Content-type:text/html;charset=utf-8"
print
print u"""<!DOCTYPE html>
<html>
<head>
<title>society of the query</title>
<link rel="stylesheet" type="text/css" href="/styles.css" />
</head>
<body onload="document.getElementById('q').focus();">
<form action="/cgi-bin/search.cgi">
    <span class="logo">
        <a href="/">
            <span class="r">Q</span>
            <span class="g">U</span>
            <span class="b">E</span>
            <span class="r">R</span>
            <span class="g">Y</span>
        </a>
    </span>
    <input id="q" type="text" name="q" class="q" value={0} />
    <input type="submit" name="_submit" value="ok" />
    <input type="submit" name="_submit" value="i'm feeling lucky" />
""".format(quoteattr(q)).encode("utf-8")

ix = open_dir("index")
with ix.reader() as reader:
    for term in reader.lexicon('title'):
        print '<a href="/cgi-bin/search.cgi?{0}">{1}</a>'.format(urllib.urlencode({"q": term}), term)
    print "<hr />"
    for term in reader.lexicon('content'):
        print '<a href="/cgi-bin/search.cgi?{0}">{1}</a>'.format(urllib.urlencode({"q": term}), term)


print """
</form>
</body>
</html>
"""