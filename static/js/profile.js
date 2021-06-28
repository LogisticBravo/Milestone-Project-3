$(document).ready(function () {
if ($("#subscription").attr("checked") == "checked") {
    $("#subscription").attr("data-bs-target", "#unsubscribe")
} else if ($("#subscription").attr("checked") == undefined) {
    $("#subscription").attr("data-bs-target", "#subscribe")
}})