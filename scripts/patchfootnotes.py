# -*- coding: utf-8 -*-
# Cleanup the mess pandoc makes mapping Calibre's HTML footnotes to markdown
#
# The footnote links:
# ^^[1](#note_1 "1")^^ ==> [^1]
#
# The footnotes themselves:
# [[←1](#back_note_1 "1")]
# :   See Language Council of Sweden, ‘Google Does Not Own the Language’,
#     26 March 2013, http://www.sprakradet.se/15922 (in Swedish).
# ==>
# [^1] : See Language Council of Sweden, ‘Google Does Not Own the Language’,
#     26 March 2013, http://www.sprakradet.se/15922 (in Swedish).

import re

fnlinkpat = re.compile(r'\^\^\[(\d+)\]\(#note_\d+ "\d+"\)\^\^', re.I)
fnpat = re.compile(ur'\[\[←(\d+)\]\(#back_note_\d+ "\d+"\)\]\n:(.*?)\n\n', re.I|re.DOTALL)

def patchfootnotes (text):
    def s (m):
        n = int(m.group(1))
        return u"[^{0}]".format(n)
    text = fnlinkpat.sub(s, text)

    def sfn (m):
        id, body = m.groups()
        body = body.lstrip().splitlines()
        return u"[^{0}]: {1}\n\n".format(id, u"\n".join(body))

    text = fnpat.sub(sfn, text)

    return text

import sys
text = sys.stdin.read().decode("utf-8")
text = patchfootnotes(text)
print text.encode("utf-8")
