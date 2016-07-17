
$("document").ready(function() {
    var new_album_button = $("#new-album");
    var new_album_layer = $("#body-layer");

    $("#body-layer").hide()

    new_album_button.on({
        "click": function(){
            new_album_layer.fadeIn();
        }
    });
//
//    new_album_layer.on({
//        "click": function(){
//            new_album_layer.fadeOut();
//        }
//    });
//
    $(this).on("click", "#body-layer", function(evt) {  //listen for clicks
        var target = $(evt.target ||evt.srcElement);  //get the element that was clicked on
        if (target.is("#body-layer")) {  //make sure it was not a child that was clicked.
            new_album_layer.fadeOut();
        }
    });
});