#!/usr/bin/python
#coding=utf-8

from xml.etree import ElementTree

script_directory = "script/"
pages_directory = "pages/"
photos_directory = "photos/"
gallery_prefix = "gallery_"
source = "photos/galleries.html"


javascript_template="""\
var photos = [\n\"%(photos)s\"\n]
var captions = [\n\"%(captions)s\"\n]
var current_photo = 0
"""

withjavascript_html_template="""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Churchill Primary School - %(title)s</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/> 
    <link rel="stylesheet" href="stylesheets/styles.css" type="text/css" />
    <link rel="stylesheet" href="stylesheets/galleries.css" type="text/css" />
    <script type="text/javascript" src="script/suckerfish.js"></script>
    <script type="text/javascript" src="%(javascript_file)s"></script>
    <script type="text/javascript" src="script/imagebrowser.js"></script>
  </head>
  <body>
  <div id="page">
<!--header-->
  <div class="%(aspect)s" id="content">
    <noscript>
      <p>This photo browser requires javascript. A <a href="%(nojavascript_html_file)s">no javascript</a> version is
      available.</p>
    </noscript>
    <img class="gallery" id="photo" src="%(first_photo)s" alt="1 of %(count)s"/>
    <ul id="buttonbar">
      <li><a href="#" onclick='return first_photo()'>First</a></li>
      <li><a href="#" onclick='return prev_photo()'>Prev</a></li>
      <li><a href="#" onclick='return next_photo()'>Next</a></li>
      <li><a href="#" onclick='return last_photo()'>Last</a></li>
    </ul>
    <div class="caption" id="caption">
      <p class="count">1 of %(count)s</p>
      %(first_caption)s
    </div>
    </div>
    <!--navigation-->
    <!--footer-->
  </div>
  </body>
</html>
"""

nojavascript_html_template = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Churchill Primary School - %(title)s</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/> 
    <link rel="stylesheet" href="stylesheets/styles.css" type="text/css" />
    <link rel="stylesheet" href="stylesheets/galleries.css" type="text/css" />
    <script type="text/javascript">
      window.location="%(with_javascript_html)s"
    </script>
  </head>
  <body>
    <div id="page">
      <!--header-->
      <div class="%(aspect)s" id="content">
%(images)s
      </div>
      <!--navigation-->
      <!--footer-->
    </div>
  </body>
</html>
"""


nojavascript_image_template="""\
        <img class="gallery" src="%(photo)s" alt="%(count)s"/>
        <div class="caption">
          <p class="count">%(count)s</p>
          %(caption)s
        </div>
"""


def build_javascript(gallery):
    return javascript_template % {
        "photos": "\",\n\"".join([photos_directory + x[0] for x in gallery[2]]),
        "captions": "\",\n\"".join([x[1].replace("\n", "\\\n ").replace("\"", "\\\"") for x in gallery[2]])}
             
           
def build_withjavascript_html(gallery, javascript_file, nojavascript_html_file):
    return withjavascript_html_template % {
        "title": gallery[0],
        "count": len(gallery[2]),
        "javascript_file": script_directory + javascript_file,
        "nojavascript_html_file": nojavascript_html_file,
        "first_photo": photos_directory + gallery[2][0][0],
        "first_caption": gallery[2][0][1],
        "aspect": gallery[3]}


def build_nojavascript_html(gallery, withjavascript_html_file):
    images=""
    for count, (image, caption) in enumerate(gallery[2]):
        images += nojavascript_image_template % {
            "photo": photos_directory + image,
            "caption": caption,
            "count": str(count + 1) + " of " + str(len(gallery[2]))}
    return nojavascript_html_template % {
        "title": gallery[0],
        "with_javascript_html": withjavascript_html_file,
        "images": images,
        "aspect": gallery[3]}
            

def process_source(filename):
    retval = []
    body = ElementTree.parse(filename).find("{http://www.w3.org/1999/xhtml}body")
    for div in body:
        files = []
        retval.append([div.find("{http://www.w3.org/1999/xhtml}h1").text, div.get("id"), files, div.get("class")])
        for tag in div:
            if tag.tag == "{http://www.w3.org/1999/xhtml}h1":
                continue
            elif tag.tag == "{http://www.w3.org/1999/xhtml}img":
                files.append([tag.get("src"), ""])
            else:
                files[-1][1] = files[-1][1] + clean_string(ElementTree.tostring(tag))
    return retval


def clean_string(str):
    return str.replace(
        ' xmlns:html="http://www.w3.org/1999/xhtml"', "").replace(
        'html:', "").rstrip()



for gallery in process_source(source):
    print "Building", gallery[0]
    javascript_file = gallery_prefix + gallery[1] + ".js"
    nojavascript_html_file = gallery_prefix + gallery[1] + ".nojs.html"
    withjavascript_html_file = gallery_prefix + gallery[1] + ".html"
    open(script_directory + javascript_file, "w").write(
        build_javascript(gallery))
    open(pages_directory + nojavascript_html_file, "w").write(
        build_nojavascript_html(gallery, withjavascript_html_file))
    open(pages_directory + withjavascript_html_file, "w").write(
        build_withjavascript_html(gallery, javascript_file, nojavascript_html_file))

