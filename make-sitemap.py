import structure
import datetime

def to_urls(structure):
    str = ""
    for s in structure:
        if len(s) == 3:
            str += to_urls(s[2])
        if s[1][:4] == "node":
            continue
        str += (
            "  <url>\n"
            "    <loc>http://www.churchill-pri.n-somerset.sch.uk/%s</loc>\n"
            "    <changefreq>yearly</changefreq>\n"
            "    <lastmod>%s</lastmod>\n"
            "    <priority>0.5</priority>\n"
            "  </url>\n") % (s[1], datetime.date.today())
    return str


print (
    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
    "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n"
    "%s"
    "</urlset>\n") % to_urls(structure.site_structure)

            
    
