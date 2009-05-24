# coding=utf-8

header = """\
<div id="header">
  <img src="images/logo.png" alt="Churchill school"/>
  <h1>Churchill Primary C.E.V.C School</h1>
</div>
"""

footer = """\
<div id="footer">
  <img id="awards" src="images/awards.png" alt="awards"/>
  <p id="w3c"><a href="http://validator.w3.org/check?uri=referer"><img
        src="images/valid-xhtml10-blue.png"
        alt="Valid XHTML 1.0 Strict" height="31" width="88" /></a></p>
<p>©2009 All Rights Reserved | <a href="privacy.html">Privacy</a> | <a href="terms-of-use.html">Terms</a></p>
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
       <div id="strut"></div>
       <h1>%(title)s</h1>
       <ul>
%(list)s
       </ul>
    </div>
<!--footer-->
    </div>
  </body>
</html>"""
