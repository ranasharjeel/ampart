
function hover(){
    var img = document.getElementById("spotify-logo");
    var new_src = img.getAttribute("src").replace("light", "dark");
    img.setAttribute("src", new_src);
}
function unhover(){
    var img = document.getElementById("spotify-logo");
    var new_src = img.getAttribute("src").replace("dark","light");
    img.setAttribute("src", new_src);
}

