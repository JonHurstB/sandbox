#!/usr/bin/python

from xml.etree import cElementTree
import sitemap
import glob
import os

source_dir="pages/"
site_dir="site/"
template_page = "templates/template.html"
structure_page = "structure.html"

def process_nodes(element, filename):
    """"Specialises the navigation div for a particular filename.

    The class attrib is first removed from all anchors to allow re-use, then Class 'current' is added to the anchor
    containing the filename and all its parent anchors. Class 'node' is added to any anchor with a sub-menu."""
    parent_current = False
    for e in element: #all the <li> tags
        current = False
        classes = []
        anchor = e.find("{http://www.w3.org/1999/xhtml}a")
        if "class" in anchor.attrib:
            del(anchor.attrib["class"])
        sublist = e.find("{http://www.w3.org/1999/xhtml}ul")
        if sublist:
            current = process_nodes(sublist, filename)
            classes.append("node")
        if current or filename.split(".")[0] == anchor.get("href").split(".")[0]:
            classes.append("current")
            parent_current = True
        if classes:
            anchor.set("class", " ".join(classes))
    return parent_current


def build_node_pages(element):
    """"Builds the pages displayed if an anchor leading to a sub-menu is clicked rather than hovered"""
    template = file(template_page).read()
    for e in element: #all the <li> tags
        str = ""
        anchor = e.find("{http://www.w3.org/1999/xhtml}a")
        sublist = e.find("{http://www.w3.org/1999/xhtml}ul")
        if sublist:
            build_node_pages(sublist)
            for se in sublist:
                se_anchor = se.find("{http://www.w3.org/1999/xhtml}a")
                str += '<li><a href="%s">%s</a></li>\n' % (se_anchor.get("href"), se_anchor.text)
            print "Creating", source_dir + anchor.get("href")
            output = template.replace("<!--Add title here-->", anchor.text)
            output = output.replace("<!--Add content here-->",
                                      "<h1>%s</h1>\n<ul>\n%s</ul>\n" % (anchor.text, str))
            open(source_dir + anchor.get("href"), "w").write(output)
                        


if __name__ == "__main__":
    structure, iddict = cElementTree.XMLID(file(structure_page).read())
    nav = iddict["navigation"].find("{http://www.w3.org/1999/xhtml}ul")
    #create the node pages
    build_node_pages(nav)
    #create the site map
    print "Creating", site_dir + "sitemap"
    file(site_dir + "sitemap", "w").write(sitemap.sitemap(nav))
    #create the html pages
    for f in glob.glob(source_dir + "*.html"):
        process_nodes(iddict["navigation"].find("{http://www.w3.org/1999/xhtml}ul"), os.path.basename(f))
        s = file(f).read()
        for r in ("header", "footer", "navigation"):
            s = s.replace("<!--%s-->" % r, cElementTree.tostring(iddict[r], "utf-8"))
        s = s.replace("html:", "")
        outfile = site_dir + os.path.basename(f)
        print "Creating", outfile
        open(outfile , "w").write(s)

