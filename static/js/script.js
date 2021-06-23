var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})

var toastElList = [].slice.call(document.querySelectorAll('.toast'))
var toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})

$(document).ready(function () {
    var myModal = new bootstrap.Modal(document.getElementById('writeReviewToggle'), {
        keyboard: false
    })
    if (window.location.hash.indexOf("writeReviewToggle") > -1) {
        myModal.show();
    }
});
