#!/usr/bin/env python

import yaml, json
import os, sys
from yaml.parser import ParserError

def gathermetadata (srcs):
    ret = {}
    ret['articles'] = []

    def process (m):
        ret['articles'].append(m)

    for x in srcs:
        with open(x) as f:
            try:
                for meta in yaml.load_all(f):
                    process(meta)
                    break
            except Exception:
                pass
    return ret


if __name__ == "__main__":
    md = gathermetadata(sys.argv[1:])
    print(json.dumps(md))
