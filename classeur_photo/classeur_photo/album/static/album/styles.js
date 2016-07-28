
$("document").ready(function() {
    // set Variables
    var body_layer = $("#body-layer");
    var center_form = $("#center-form");
    var welcome_button = $("#welcome");

    var new_album_button = $("#new-album");
    var album_name_input = $("#id_album_name");
    var album_permalink_input = $("#id_permalink");
    var permalink_edited = false;
    var create_album = $("#create-album");

    var image_list = $(".thumb");

    var main_body = $("#main-body");

    // define functions
    function get_permalink(name){
        name = name.toLowerCase()
        name = name.replace(/([^\s\w])+/g, '')
        name = name.replace(/\s/g, '_')
        return name
    }

    // set initial properties
    if (welcome_button.length !== 0){
        return;
    }

    body_layer.hide();
    center_form.hide();

    // set event handlers
    body_layer.on({
        "drop": function(e){
            e.stopPropagation();
            e.preventDefault();
            body_layer.fadeOut();
            if (window.File && window.FileReader && window.FileList && window.Blob) {
              // alert("Great success! All the File APIs are supported.");
            } else {
              alert('The File APIs are not fully supported in this browser.');
            }

            var files = e.originalEvent.dataTransfer.files;

            for (var i = 0, f; f = files[i]; i++) { // iterate in the files dropped
                if (f.type.startsWith('image')) {
                    // Get file
                    var reader = new FileReader();

                    // Closure to capture the file information.
                    reader.onload = (function(theFile) {
                    return function(e) {
                        // Render thumbnail.
                        var span = document.createElement('span');
                        span.innerHTML = ['<img class="thumb" src="', e.target.result,
                                          '" title="', escape(theFile.name), '"/>'].join('');
                        document.getElementById('list').insertBefore(span, null);
                    };
                    })(f);

                    // Read in the image file as a data URL.
                    reader.readAsDataURL(f);
                } else if (!f.type) {
                    alert("You cannot directly drag a folder.");
                }
            }
        },
        "dragover": function(e){
            e.stopPropagation();
            e.preventDefault();
        },
        "dragend": function(e){
            if (e.target.id == "body-layer"){
                body_layer.fadeOut();
            }
        },
        "click": function(e){
            if (e.target.id == "body-layer"){
                body_layer.fadeOut();
                center_form.fadeOut();
            }
        }
    })

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

    main_body.on({
        "dragenter": function(e){
            body_layer.fadeIn();
        },
        "dragover": function(e){
            e.stopPropagation();
            e.preventDefault();
        },
        "dragend": function(e){
            body_layer.fadeOut();
        }
    })

    //Display Images as cropped squares
    image_list.each(function() {
      if ($(this).width() > $(this).height()) {
        $(this).addClass('landscape');
      }
    });

    // http://www.html5rocks.com/en/tutorials/file/dndfiles/
});
