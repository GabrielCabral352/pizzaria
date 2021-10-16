document.addEventListener('click', function({ target }) {
    if (target.id == "popupBg"){
        document.querySelector(".popup").style.display = "none"
        document.querySelector(".popupBg").style.display = "none"
    }
}, true);

document.getElementById("closeBTN").addEventListener('click', function({ target }) {
    document.querySelector(".popup").style.display = "none"
    document.querySelector(".popupBg").style.display = "none"

}, true);
function popup(tag){
    document.querySelector(".popup").style.display = "block";
    document.querySelector(".popupBg").style.display = "block";
    document.querySelector(".popup").innerHTML = tag.outerHTML
    document.querySelector(".popup").innerHTML = "sadsdasdasdas"
}

