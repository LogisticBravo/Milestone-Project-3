$(document).ready(function () {
    function checked(state) {
            $("#subscription").prop("checked", state)
        };
    if ($("#subscription").attr("checked") == "checked") {
        $("#subscription").attr("data-bs-target", "#unsubscribe");
        var closeButton = document.getElementById("unsubClose");
        var cancelButton = document.getElementById("unsubCancel");
        closeButton.onclick = function(){checked("true");}
        cancelButton.onclick = function(){checked("true");}
    } else if ($("#subscription").prop("checked") == false) {
        $("#subscription").attr("data-bs-target", "#subscribe");
        var subCloseButton = document.getElementById("subClose");
        var subCancelButton = document.getElementById("subCancel");
        subCloseButton.onclick = function(){checked(false);}
        subCancelButton.onclick = function(){checked(false);}
    }
})