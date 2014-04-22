#!/usr/bin/env python

import cgitb; cgitb.enable()
import cgi, json, sys, os

env = os.environ
referer = env.get("HTTP_REFERER")
pwd = env.get("PWD", env.get("PATH_TRANSLATED"))
fs = cgi.FieldStorage()
path = fs.getvalue("path", "").strip("/")
data = fs.getvalue("data", "")

# Evt todo: map URL to path including foo/ => foo/index.html

# print "Content-type: application/json;charset=utf-8"
# print
# print json.dumps({'result': True, 'message': 'saved', 'pwd': pwd, 'path': path, 'referer': referer})
# sys.exit(0)

if path:
    abspath = os.path.join(pwd, path)
    try:
        if os.path.exists(abspath):
            if os.path.exists(abspath+"~"): # for windows (rename fails if ~ exists)
                os.remove(abspath+"~")
            os.rename(abspath, abspath+"~")
        f = open(abspath, "w")
        f.write(data)
        f.close()
        print "Content-type: application/json;charset=utf-8"
        print
        print json.dumps({'result': True, 'message': 'saved'})

    except OSError, e:
        print "Content-type: application/json;charset=utf-8"
        print
        print json.dumps({'result': False, 'message': 'OSError: '+str(e)})
