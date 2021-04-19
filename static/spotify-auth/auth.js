
window.addEventListener("load", getAccess); // fire on page load
const token_data = JSON.parse(document.getElementById("auth-page").getAttribute("value"));


// POST Request is sent here
const TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token";


// Post auth code to get access/refresh tokens
function getAccess(){
    let request = TOKEN_ENDPOINT;
    console.log(token_data);

}
