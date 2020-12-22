
let menu =document.getElementById("menu")
let header = document.getElementById("header")
let nav_menu = document.getElementById("nav_menu")
let nav_menu_header = document.getElementById("nav_menu_header")
let icon = document.getElementById("icon")

menu.addEventListener("click", function() {
    if(header.style.height == "70px"){
        header.style.height = 70 + nav_menu.offsetHeight + nav_menu_header.offsetHeight + icon.offsetHeight + "px"
    } else {
        header.style.height = "70px"
    }
})