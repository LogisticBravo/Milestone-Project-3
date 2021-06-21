document.getElementById('confirm_password').addEventListener("change", unlock);
$('p').hide()

function unlock() {
    if ($('#new_password').val() !== $('#confirm_password').val())
    {
    $('#submit').prop("disabled", true);
    $('p').show()
    }
    else if ($('#new_password').val() === $('#confirm_password').val())
    {
    $('#submit').removeAttr("disabled");
    $('p').hide()
    }
}