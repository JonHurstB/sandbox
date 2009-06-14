from xml.etree import cElementTree
import os
import datetime

pages_directory = "pages/"

nonstd = (
    ("index", "daily", "1.0"),
    ("newsletter", "never", "0.75"),
    ("topic-web", "monthly", "0.5"))


def build_href_list(element, list):
    for child in element:
        if child.tag == "{http://www.w3.org/1999/xhtml}li":
            a = child.find("{http://www.w3.org/1999/xhtml}a")
            if a is not None:
                list.append(a.get("href"))
            u = child.find("{http://www.w3.org/1999/xhtml}ul")
            if u is not None:
                build_href_list(u, list)


def sitemap(element):
    str = ""
    hrefs = []
    build_href_list(element, hrefs)
    for h in hrefs:
        if h[:4] == "node": continue #don't add nodes to sitemap
        if not os.access(pages_directory + h, os.R_OK): continue #only add hrefs in pages
        freq, priority = "yearly", "0.5"
        for t in nonstd:
            if h.startswith(t[0]):
                freq, priority = t[1:]
        str += (
            "  <url>\n"
            "    <loc>http://www.churchill-pri.n-somerset.sch.uk/%s</loc>\n"
            "    <changefreq>%s</changefreq>\n"
            "    <lastmod>%s</lastmod>\n"
            "    <priority>%s</priority>\n"
            "  </url>\n") % (h, freq, datetime.date.fromtimestamp(os.stat(pages_directory + h).st_mtime), priority)
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
        "%s"
        "</urlset>\n") % str



if __name__ == "__main__":
    structure, iddict = cElementTree.XMLID(file("structure.html").read())
    print sitemap(iddict["navigation"].find("{http://www.w3.org/1999/xhtml}ul"))
    
