
// function upvote(){
//     placeholder
// }

// function downvote(){
//     placeholder
// }

function showImage() {
    var cow = document.createElement("IMG")
    document.getElementById("cow").appendChild(cow)
    cow.src = "/static/korovann.png"
}

//Это говно не работает
function LootImage(){
    var cow = document.getElementsByTagName("IMG")
    document.removeChild(cow)
}