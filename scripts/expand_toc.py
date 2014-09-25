#!/usr/bin/env python
# Process a TOC to a set of links

from __future__ import print_function
import markdown, sys, html5lib, re, argparse, sys, os
from subprocess import Popen, check_output, PIPE
from itertools import izip


def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)

def grouped(iterable, n):
    """
    http://stackoverflow.com/questions/5389507/iterating-over-every-two-elements-in-a-list
    s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ...
    """
    return izip(*[iter(iterable)]*n)

parser = argparse.ArgumentParser(description='Table of contents Tools')
parser.add_argument('toc', help='toc file')
parser.add_argument('--list', dest='list', action='store_true', help='output makefile friendly list of linked files')
parser.add_argument('--ignore-missing', dest='ignoreMissing', action='store_true', help='')
parser.add_argument('--filter', dest="filter", default="cat", help='script to run on each linked chapter')
# parser.add_argument('--section-id', dest="sectionID", help='script to determine link ids')
parser.add_argument('--section-level', help='level from which to generate sections')
parser.add_argument('--section-template', help='template to generate sections')

args = parser.parse_args()

## in fact filter markdown links, return original targets when list is requested
## otherwise return toc with links replaced to links to titles

markdown_link_pattern = re.compile(r"\[(.*?)\]\((.*?)\)", re.DOTALL)
markdown_header_pattern = re.compile(r"^(#+)(.*)$", re.M)


toc = args.toc
with open(toc) as f:

    if args.list:
        srcs = []
        toctext = f.read().decode("utf-8")
        for m in markdown_link_pattern.finditer(toctext):
            srcs.append(m.groups()[1])
        for s in srcs:
            if args.ignoreMissing:
                if os.path.exists(s):
                    print (s)
                else:
                    print ("MISSING", s, file=sys.stderr)
            else:
                print (s)
    else:
        toctext = f.read().decode("utf-8")
        split = markdown_header_pattern.split(toctext)
        split.insert(0, None)
        split.insert(0, None)

        ## First pass, output the toc with mapped links,
        ## cache the (filtered) sources
        sources_text = {}

        def id_for_source (src):
            """
            converts the (filtered) src to html with pandoc
            and searches for the first id attribute to use as a link
            """
            # cmd = [args.sectionID, src]
            # return check_output(cmd).strip()
            markdown_src = check_output([args.filter, src])
            # cache filtered src!
            sources_text[src] = markdown_src
            p = Popen(["pandoc", "--to", "html", "--from", "markdown"], stdin = PIPE, stdout=PIPE)
            (html, err) = p.communicate(markdown_src)
            idpat = re.compile(r"id=\"(.*?)\"")
            for m in idpat.finditer(html):
                return m.group(1)

        def toc_link_sub(m):
            label, link = m.groups()
            return u"[{0}]({1})".format(label,"#"+id_for_source(link))

        for header_hashes, header, text in grouped(split, 3):
            if header:
                # Up the h-level of > 1's by 1 (so 2 ==> 3)
                n = len(header_hashes)
                if n > 1:
                    n += 1
                print (((u"#"*n)+header).encode("utf-8"))
            # OUTPUT TEXT WITH REPLACED LINKS
            print (markdown_link_pattern.sub(toc_link_sub, text).encode("utf-8"))
        print ()

        ## Second pass, output the (filtered) markdown in order
        ## with toc headers at the right spots
        ##
        for header_hashes, header, text in grouped(split, 3):
            if header:
                n = len(header_hashes)
                if n > 1:
                    n -= 1
                    print (((u"#"*n)+header).encode("utf-8"))
                    print ()
            for m in markdown_link_pattern.finditer(text):
                src = m.groups()[1]
                print (sources_text[src])
                print () 

