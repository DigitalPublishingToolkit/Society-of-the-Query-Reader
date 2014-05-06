#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import highlight

import cgitb; cgitb.enable()
import cgi
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
<script src="/lib/jquery/jquery-1.4.3.min.js"></script>
<script src="/lib/fancybox/jquery.fancybox-1.3.4.js"></script>
<script>
$(document).ready(function () {{
    $("div.image a").fancybox();

}});
</script>
<link rel="stylesheet" type="text/css" href="/lib/fancybox/jquery.fancybox-1.3.4.css">
</head>
<body onload="document.getElementById('q').focus();">
<form action="">
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

if q:
    ix = open_dir("index")
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(q)
        hf = highlight.HtmlFormatter()
        corrected = searcher.correct_query(query, q)
        # print corrected.string.encode("utf-8")
        if corrected.query != query:
            print '<div class="suggest">'
            print("Did you mean:", corrected.format_string(hf))
            print '</div>'

        results = searcher.search(query)
        for r in results:
            print '<div class="result {0}">'.format(r['type'])
            if r['type'] == "image":
                print '<a href="/{0}_z.jpg" rel="images"><img src="/{0}_t.jpg" /></a>'.format(r['path'].replace(".json", ""))
            else:              
                print '  <div class="title"><input type="checkbox" name="s" value="{0}" /><a href="/{0}">'.format(r['path'])
                print r['title'].encode("utf-8")
                print '  </a></div>'
                print '  <div class="content">'
                print r.highlights('content').encode("utf-8")
                print '  </div>'
            print '</div>'
        if len(results):
            print '<input type="submit" name="_submit" value="download epub" />'

print """
</form>
</body>
</html>
"""