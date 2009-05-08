# coding=utf-8

header = """\
<div id="header">
  <img src="images/logo.png" alt="Churchill school"/>
  <h1>Churchill Primary C.E.V.C School</h1>
</div>
"""

footer = """\
<div id="footer">
  <img src="images/awards.png" alt="awards"/>
  <p>©2009 All Rights Reserved | <a href="privacy.html">PRIVACY POLICY</a> | <a href="terms-of-use.html">TERMS OF USE</a></p>
</div>
"""

#replacement table
includes = [["<!--header-->", header],
            ["<!--footer-->", footer]]


#node page
node_page = """\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Churchill Primary School - %(title)s</title>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/> 
    <link rel="stylesheet" type="text/css" href="stylesheets/styles.css"/>
    <script type="text/javascript" src="script/suckerfish.js"></script>
  </head>
  <body>
    <div id="page">
<!--header--> 
<!--navigation-->
    <div id="content">
       <h1>%(title)s</h1>
       <ul>
%(list)s
       </ul>
    </div>
<!--footer-->
    </div>
  </body>
</html>"""
