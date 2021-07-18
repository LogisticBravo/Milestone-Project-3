window.onload = function () {
    /* Sets the newletter toggle on the profile page on or off dependant on if the user confirms their subscription or backs out.
    e.g. The user is already subscribed and toggle it off, changes their mind before submission and backs out. The toggle resets to on and vice versa. */
    $(document).ready(function () {
        function checked(state) {
            $("#subscription").prop("checked", state);
        }
        if ($("#subscription").attr("checked") == "checked") {
            $("#subscription").attr("data-bs-target", "#unsubscribe");
            var closeButton = document.getElementById("unsubClose");
            var cancelButton = document.getElementById("unsubCancel");
            closeButton.onclick = function () { checked("true"); };
            cancelButton.onclick = function () { checked("true"); };
        } else if ($("#subscription").prop("checked") == false) {
            $("#subscription").attr("data-bs-target", "#subscribe");
            var subCloseButton = document.getElementById("subClose");
            var subCancelButton = document.getElementById("subCancel");
            subCloseButton.onclick = function () { checked(false); };
            subCancelButton.onclick = function () { checked(false); };
        }
        /*Sets a sessionStorage for a user when they login. This is called in the review.js file to trigger additional code. The session 'value'
        is set by appending a random number from between 0 and d.getTime() to the string 'user'. new Date() and d.getTime() adapated from looking for it in W3Schools. */
        let d = new Date();
        let uid = Math.floor(Math.random() * d.getTime());
        if (window.sessionStorage.length != 1) {
            window.sessionStorage.setItem("session", "user" + uid);
        }
    });
};