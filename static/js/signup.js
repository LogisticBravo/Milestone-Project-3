document.addEventListener('DOMContentLoaded', (event) => {
    /* validation that the passwords match when signing up. 
    Locks the submit button if they dont. Displays a message to the user advising they don't match. */
    document.getElementById('confirm_password').addEventListener("change", unlock);
    $('p').hide();

    function unlock() {
        if ($('#new_password').val() !== $('#confirm_password').val()) {
            $('#submit').prop("disabled", true);
            $('p').show();
        }
        else if ($('#new_password').val() === $('#confirm_password').val()) {
            $('#submit').removeAttr("disabled");
            $('p').hide();
        }
    }
});