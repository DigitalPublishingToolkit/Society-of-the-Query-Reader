from whoosh.index import create_in
from whoosh.fields import *

schema = Schema(
    title=TEXT(stored=True),
    authors=TEXT(stored=True),
    path=ID(stored=True),
    type=KEYWORD(stored=True),
    content=TEXT(stored=True, spelling=True),
    ncontent=NGRAMWORDS(stored=True)
)
ix = create_in("index", schema)

