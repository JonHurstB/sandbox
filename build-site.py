#!/usr/bin/python

import glob
import os
import structure
import templates

source_dir="pages/"
site_dir="site/"


def build_nav(filename):
    """Builds the navigation div for a given FILENAME"""
    return ("<div id=\"navigation\">\n"
            "%s\n</div>\n" %
            build_list(structure.site_structure, filename)[0])


def build_list(structure, filename):
    """Recursively called list builder that monitors whether filename is in the current directory branch. Returns a
    tuple consisting of the list and a boolean indicating whether filename was found"""
    str = "<ul>\n"
    current_found = False
    for e in structure:
        classes = []
        substr, is_current = "", False
        if len(e) == 3:#i.e. a sub-menu exists
            substr, is_current = build_list(e[2], filename)
            classes.append("node")
        if filename.split(".")[0] == e[1].split(".")[0]:
            current_found = True
            is_current = True
        if is_current:
            classes.append("current")
        class_str = ""
        if classes:
            class_str = "class=\"%s\"" % " ".join(classes)
        str += "<li><a %s href=\"%s\">%s</a>" % (class_str, e[1], e[0])
        if substr:
            str += "\n" + substr
        str += "</li>\n"
    str += "</ul>"
    return str, current_found


def build_node_page(structure):
    str = ""
    for node in structure:
        if len(node) == 3:#i.e. a sub menu exists
            for subnode in node[2]:
                str += "<li><a href=\"%s\">%s</a></li>\n" % (subnode[1], subnode[0])
                build_node_page(subnode)
            print "Creating", node[1]
            open(source_dir + node[1], "w").write(
                templates.node_page % {"title": node[0], "list": str})
        str = ""
            

build_node_page(structure.site_structure)
for f in glob.glob(source_dir + "*.html"):
    print f
    s = file(f).read()
    for i in templates.includes:
        s = s.replace(*i)
    s = s.replace("<!--navigation-->", build_nav(os.path.basename(f)))
    open(site_dir + os.path.basename(f), "w").write(s)
