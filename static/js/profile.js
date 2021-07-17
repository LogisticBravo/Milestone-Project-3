window.onload = function(){
/* Sets the newletter toggle on the profile page on or off dependant on if the user confirms their subscription or backs out.
e.g. The user is already subscribed and toggle it off, changes their mind before submission and backs out. The toggle resets to on and vice versa. */
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
})}