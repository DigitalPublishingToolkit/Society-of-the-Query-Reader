from gathermetadata import gathermetadata
import sys


authors = set()
md = gathermetadata(sys.argv[1:])
for a in md['articles']:
    author = a.get('Author')
    if type(author) == list:
        for name in author:
            authors.add(name)
    elif author:
        authors.add(author)

authors = list(authors)
authors.sort()

for x in authors:
    print u"<dc:creator>{0}</dc:creator>".format(x).encode("utf-8")
