#!/usr/bin/env python

from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh import highlight

import cgitb; cgitb.enable()
import cgi, json
from xml.sax.saxutils import quoteattr


f = cgi.FieldStorage()
q = f.getvalue("q", "").decode("utf-8").strip()
ix = open_dir("index")

with ix.searcher() as searcher:
    ret = {}
    ret['query'] = q
    query = QueryParser("content", ix.schema).parse(q)
    hf = highlight.HtmlFormatter()
    corrector = searcher.corrector("content")
    corrections = []
    ret['corrections'] = corrections
    for word in q.split():
        word = word.strip()
        cc = [word]
        cc.extend(corrector.suggest(word, limit=7))
        corrections.append(cc)
    corrected = searcher.correct_query(query, q)
    # print corrected.string.encode("utf-8")
    if corrected.query != query:
        ret['corrected'] = corrected.string
        ret['correctedh'] = corrected.format_string(hf)

    results = searcher.search(query, terms=True)
    ret['results'] = []
    for r in results:
        ret['results'].append({
            'title': r['title'],
            'path': '/'+r['path'],
            'rank': r.rank,
            'score': r.score,
            'highlights': r.highlights("content")
            # 'matched_terms': r.matched_terms()
        })

    print "Content-type:application/json;charset=utf-8"
    print 
    print json.dumps(ret)
