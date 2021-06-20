document.getElementById('confirm_password').addEventListener("change", unlock);


function unlock() {
    if ($('#new_password').val() !== $('#confirm_password').val())
    {
    $('#submit').prop("disabled", true);
    }
    else if ($('#new_password').val() === $('#confirm_password').val())
    {
    $('#submit').removeAttr("disabled");
    }
}