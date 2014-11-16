import re, sys

linkpat = re.compile(r"https?://[\S]+")
# prepat = re.compile(r"^[^a-zA-Z0-9/:?&_\-]")
postpat = re.compile(r"[^a-zA-Z0-9/:?&_\-]+$")

text = sys.stdin.read()

def repl (m):
    href = m.group(0)
    post = ""

    m = postpat.search(href)
    if m != None:
        post = m.group(0)
        href = href[:m.start(0)]
    return "[{0}]({0}){1}".format(href, post)

sys.stdout.write(linkpat.sub(repl, text))
