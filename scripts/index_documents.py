import os
import html5lib
from xml.etree import ElementTree as etree
from whoosh.index import open_dir


ix = open_dir("index")
with ix.writer() as writer:
    for root, dirs, files in os.walk('essays'):
        # print root, files
        if 'index.html' in files:
            fp = os.path.join(root, 'index.html')
            print fp
            src = open(fp).read().decode("utf-8")
            if type(fp) != unicode:
                fp = fp.decode("utf-8")
            tree = html5lib.parse(src, namespaceHTMLElements=False)
            paragraphs = tree.findall(".//p")
            try:
                title = paragraphs[0].text.strip()
            except AttributeError:
                title = u""
            authors = u""
            # if paragraphs[1].text:
            #    authors = paragraphs[1].text.strip()
            text = etree.tostring(tree, method="text", encoding="utf-8").decode("utf-8")
            # lines = text.splitlines()
            # for i, x in enumerate(lines[:10]):
            #     print i, x
            # print
            # print u"Indexing {0}".format(title).encode("utf-8")
            writer.add_document(title=title, type=u"essay", authors=authors, path=fp, content=text, ncontent=title+u" "+text)

    # writer.commit()
