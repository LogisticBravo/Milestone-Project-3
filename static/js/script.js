document.addEventListener('DOMContentLoaded', (event) => {
    //removes the sessionStorage 'session' on logout.
    if (window.location.href.indexOf("logout") !== -1) {
        window.sessionStorage.removeItem("session");
    }

    // Initializer for bootstrap tooltips.
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    //Iniatializer for bootstrap toasts
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });

    //Calls the bootstrap modal for leaving a review if user is prompted to add one from their profile page.
    if (window.location.hash.indexOf("writeReviewToggle") > -1) {
        var myModal = new bootstrap.Modal(document.getElementById('writeReviewToggle'), {
            keyboard: false
        });
        myModal.show();
    }

    /*recalls the local storage value of 'usermail' and populates the input form for email on the sign-up page if it exists.
    It exists if the URL contains 'newsletter_form' */
    if (window.location.href.indexOf("newsletter_form") !== -1) {
        $("#email").val(window.localStorage.getItem("usermail"));
    }
});

