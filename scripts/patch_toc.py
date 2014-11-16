import os, sys
from xml.etree import ElementTree as ET 
from urlparse import urljoin


class EPUBDir:
    def __init__(self, path):
        self.path = path
        self.locate_content()

    def locate_content (self):
        for base, dirs, files in os.walk(self.path):
            for f in files:
                rpath = os.path.relpath(os.path.join(base, f), self.path)
                if f == "content.opf":
                    self.content_path = rpath

    def open_content (self):
        # muy importante (for output/rewrite)
        ET.register_namespace('',"http://www.idpf.org/2007/opf")
        self.content = ET.parse(open(os.path.join(self.path, self.content_path)))
        # self.content.register_namespace("", "http://www.idpf.org/2007/opf")
        self.manifest = epub.content.find(".//{http://www.idpf.org/2007/opf}manifest")
        self.spine = epub.content.find(".//{http://www.idpf.org/2007/opf}spine")
        self.guide = epub.content.find(".//{http://www.idpf.org/2007/opf}guide")
        return self.content

    def rewrite_content (self):
        ET.register_namespace('',"http://www.idpf.org/2007/opf")
        content_path = os.path.join(self.path, self.content_path)
        with open(content_path, "w") as f:
            self.content.write(f, xml_declaration=True, encoding="utf-8", method="xml")
            # f.write(ET.tostring(self.content.getroot(), method="xml"))

    def path_for_href(self, href):
        return os.path.join(self.path, urljoin(self.content_path, href))

def replace_toc (self, old_toc_id, new_toc_id):
    # p = ".//{{http://www.idpf.org/2007/opf}}manifest/{{http://www.idpf.org/2007/opf}}item[@id='{0}']".format(old_toc_id)
    p = "./{{http://www.idpf.org/2007/opf}}item[@id='{0}']".format(old_toc_id)
    old_toc = self.manifest.find(p)
    if old_toc == None:
        print "toc not found"
        return
    self.manifest.remove(old_toc)
    # p = ".//{{http://www.idpf.org/2007/opf}}manifest/{{http://www.idpf.org/2007/opf}}item[@id='{0}']".format(new_toc_id)
    p = "./{{http://www.idpf.org/2007/opf}}item[@id='{0}']".format(new_toc_id)
    new_toc = self.manifest.find(p)
    new_toc.attrib['properties'] = "nav"
    # p = ".//{{http://www.idpf.org/2007/opf}}spine/{{http://www.idpf.org/2007/opf}}itemref[@idref='{0}']".format(old_toc_id)
    p = "./{{http://www.idpf.org/2007/opf}}itemref[@idref='{0}']".format(old_toc_id)
    elt = self.spine.find(p)
    self.spine.remove(elt)
    if self.guide != None:
        guide_toc = self.guide.find("./{http://www.idpf.org/2007/opf}reference[@type='toc']")
        if guide_toc != None:
            guide_toc.attrib['href'] = new_toc.attrib['href']

    ### Wrap TOC section with a nav element
    href = new_toc.attrib['href']
    new_toc_path = self.path_for_href(href)
    ET.register_namespace("", "http://www.w3.org/1999/xhtml")
    ET.register_namespace("epub", "http://www.idpf.org/2007/ops")
    t = ET.parse(new_toc_path)
    body = t.find(".//{http://www.w3.org/1999/xhtml}body")
    section = t.find(".//{http://www.w3.org/1999/xhtml}section")
    # print "b,s", body, section
    body.remove(section)
    nav = ET.SubElement(body, "{http://www.w3.org/1999/xhtml}nav")
    nav.attrib["{http://www.idpf.org/2007/ops}type"] = "toc"
    nav.append(section)
    with open(new_toc_path, "w") as f:
        t.write(f, xml_declaration=True, encoding="utf-8", method="xml")

def patch_footnotes (self):
    # search content for all html
    # <item id="ch010_xhtml" href="ch010.xhtml" media-type="application/xhtml+xml" />
    links = {}

    def register_link(href):
        if href not in links:
            links[href] = True

    for item in self.manifest.findall(".//{http://www.idpf.org/2007/opf}item"): 
        if item.attrib["media-type"] == "application/xhtml+xml":
            changed = False
            path = self.path_for_href(item.attrib['href'])
            ET.register_namespace("", "http://www.w3.org/1999/xhtml")
            ET.register_namespace("epub", "http://www.idpf.org/2007/ops")
            t = ET.parse(path)
            for fn in t.findall(".//{http://www.w3.org/1999/xhtml}a[@class='footnoteRef']"):
                sup = fn.find("./{http://www.w3.org/1999/xhtml}sup")
                if sup != None:
                    number = int(sup.text)
                    fn.remove(sup)
                else:
                    number = int(fn.text)
                fn.text = u"NOTE {0}".format(number)
                changed = True

            for a in t.findall(".//{http://www.w3.org/1999/xhtml}a"):
                clas = a.attrib.get('class', '')
                href = a.attrib.get('href')
                
                if clas == 'uri' and href != None and href.startswith("http"):
                    a.attrib['target'] = 'external'
                    register_link(href)

                if href != None and href.startswith("#fnref"):
                    if clas:
                        newclass = clas + " "
                    else:
                        newclass = ""
                    a.attrib['class'] = newclass+"footnote_backlink"
                    a.text = "BACK"
                    changed = True

            if changed:
                with open(path, "w") as f:
                    t.write(f, xml_declaration=True, encoding="utf-8", method="xml")
    
    # Manifest external links
    # all_links = links.keys()
    # all_links.sort()
    # for i, link in enumerate(all_links):
    #     print link
    #     li = ET.SubElement(self.manifest, "{http://www.idpf.org/2007/opf}item")
    #     li.attrib['id'] = "extlink{0}".format(i+1)
    #     li.attrib['href'] = link
    #     li.attrib['media-type'] = "text/html"
    #     li.attrib['properties'] = "remote-resources"

# <nav epub:type="toc"> add inside the section

if __name__ == "__main__":
    path = sys.argv[1]
    epub = EPUBDir(path)
    epub.open_content()
    # remove the title page
    # <itemref idref="title_page_xhtml" linear="no" />
    titleref = epub.spine.find('.//{http://www.idpf.org/2007/opf}itemref[@idref="title_page_xhtml"]')
    epub.spine.remove(titleref)
    replace_toc(epub, "nav", "ch002_xhtml")
    patch_footnotes(epub)
    epub.rewrite_content()
