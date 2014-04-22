import os, json
from glob import glob
from whoosh.index import open_dir


ix = open_dir("index")
with ix.writer() as writer:
    for f in glob('photos/*.json'):
        if f.endswith(".json") and not f.endswith("/index.json"):
            with open(f) as inf:
                print f
                data = json.load(inf)['photo']
                title = data['description']
                title = data['title']['_content']
                text = data['description']['_content']
                print

            writer.add_document(title=title, type=u"image", authors=u"", path=f.decode("utf-8"), content=text, ncontent=title+u" "+text)
    # writer.commit()
