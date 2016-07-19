
$("document").ready(function() {
    // set Variables
    var body_layer = $("#body-layer");
    var center_form = $("#center-form");

    var new_album_button = $("#new-album");
    var album_name_input = $("#id_album_name");
    var album_permalink_input = $("#id_permalink");
    var permalink_edited = false;
    var create_album = $("#create-album");

    var import_images_button = $("#import-images")
    var import_url_input = $("#id_url_path");
    var import_folder_input = $("#id_folder_path");
    var import_url_div = $("#url-div");
    var import_folder_div = $("#folder-div");
    var import_url_selected = $("#select_url");
    var import_folder_selected = $("#select_folder");
    var import_submit = $("#import-submit");

    // define functions
    function get_permalink(name){
        name = name.toLowerCase()
        name = name.replace(/([^\s\w])+/g, '')
        name = name.replace(/\s/g, '_')
        return name
    }

    // set initial properties
    body_layer.hide();
    center_form.hide();
    import_url_div.hide();
    import_folder_selected.focus();

    // set event handlers
    $(this).on("click", "#body-layer", function(evt) {  //listen for clicks
        var target = $(evt.target ||evt.srcElement);  //get the element that was clicked on
        if (target.is("#body-layer")) {  //make sure it was not a child that was clicked.
            body_layer.fadeOut();
            center_form.fadeOut();
        }
    });

    // Create Album
    new_album_button.on({
        "click": function(){
            album_name_input.val("");
            album_permalink_input.val("");
            permalink_edited = false;
            body_layer.fadeIn();
            center_form.fadeIn();
        }
    });

    album_name_input.on({
        "keyup": function(){
            if (! permalink_edited){
                album_permalink_input.val(get_permalink(album_name_input[0].value));
            }
        }
    });

    album_permalink_input.on({
        "keyup": function(){
            permalink_edited = true;
        }
    });

    create_album.on({
        "click": function(){
            var permalink = album_permalink_input[0].value;
            if (permalink != get_permalink(permalink)){
                alert('Invalid Permalink. It should only have alphanumeric characters and underscores.');
                album_permalink_input.val(get_permalink(permalink));
                return;
            }
        }
    });

    // Import Images
    import_images_button.on({
        "click": function(){
            import_url_input.val("");
            import_folder_input.val("");
            body_layer.fadeIn();
            center_form.fadeIn();
        }
    });

    import_url_selected.on({
        "click": function(){
            import_url_div.show();
            import_folder_div.hide();
            import_submit.show();
            import_url_input.val("");
            import_folder_input.val("");
        }
    });

    import_folder_selected.on({
        "click": function(){
            import_url_div.hide();
            import_folder_div.show();
            import_submit.show();
            import_url_input.val("");
            import_folder_input.val("");
        }
    });


});