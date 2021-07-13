var button = document.getElementById("contact-submit")

button.onclick = function(){
    $("#message, #fname, #email").addClass("d-none")
    $("#contact-submit").before("<span class ='d-block my-2'>Thank you for Contacting Us! We've reveived your message</span>")
}