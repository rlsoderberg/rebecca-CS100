function changeImage() {

    var skel_img = document.getElementById("skel_img");
    
    var youtubeimgsrc = document.getElementById("skel_img").src;
    document.getElementById("demo").innerHTML = youtubeimgsrc;

    if (skel_img.src == "skel_dance.gif"){
        skel_img.src = "skel_explode.gif";
    } else {
        skel_img.src = "skel_dance.gif";
    }
}