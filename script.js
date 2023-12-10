function previewFile() {
    var preview = document.getElementById('previewImg');
    var file    = document.getElementById('fileToUpload').files[0];
    var reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}

function previewFile2() {
    var preview = document.getElementById('previewImg2');
    var file    = document.getElementById('fileToUpload2').files[0];
    var reader  = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}