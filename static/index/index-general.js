/*
    Hover effect for spotify login button
    changes the spotify logo color depending on the hover
*/
const spotify_login_button = document.getElementById("spotify-login-btn");
spotify_login_button.addEventListener("mouseover", hover);
spotify_login_button.addEventListener("mouseout", unhover);

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




const auth_data = JSON.parse(spotify_login_button.getAttribute("value"));


function authStuff(text){
    console.log(text);
}