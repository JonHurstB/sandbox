function set_photo()
{
    document.getElementById("photo").src = photos[current_photo]
    document.getElementById("photo").className = aspects[current_photo]
    document.getElementById("buttonbar").className = aspects[current_photo]
    var count = "<p class=\"count\">" + (current_photo + 1) + " of " + photos.length + "</p>"
    document.getElementById("photo").alt = (current_photo + 1) + " of " + photos.length
    document.getElementById("caption").innerHTML = count + captions[current_photo]
}

function first_photo()
{
    current_photo = 0
    set_photo(current_photo)
    return false;
}

function prev_photo()
{
    current_photo--
    if(current_photo<0)
        current_photo = 0
    set_photo(current_photo)
    return false;
}

function next_photo()
{
    current_photo++
    if(current_photo == photos.length)
        current_photo--
    set_photo(current_photo)
    return false;
}

function last_photo()
{
    current_photo = photos.length - 1
    set_photo(current_photo)
    return false;
}
    

sfHover = function() {
    var sfEls = document.getElementById("buttonbar").getElementsByTagName("LI");
    for (var i=0; i<sfEls.length; i++) {
	sfEls[i].onmouseover=function() {
	    this.className+=" sfhover";
	}
	sfEls[i].onmouseout=function() {
	    this.className=this.className.replace(new RegExp(" sfhover\\b"), "");
	}
    }
}

if (window.attachEvent) window.attachEvent("onload", sfHover);
var current_photo = 0
