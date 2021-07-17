window.onload = function(){


/* triggers newsletter modal. Code partially from: https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onscroll3
local storage code partially from https://stackoverflow.com/questions/8123032/how-do-i-make-a-count-variable-persistent-across-sessions
takes the users email address and stores it to local storage to be poulated on the signup page if it's triggered. i.e if they are not signed in. */
window.onscroll = function () {
    newsletter()
}

function newsletter() {
    if ((document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) && window.localStorage.getItem("newsletterCount") != 1) {
        var newsletterModal = new bootstrap.Modal(document.getElementById('newsletter'), {
            keyboard: false
        })
        newsletterModal.show();
        window.localStorage.setItem("newsletterCount", 1);
        var newsletterButton = document.getElementById("newsletterSub");
        newsletterButton.onclick = function () {
            var newmail = document.getElementById("emailInput").value;
            window.localStorage.setItem("usermail", newmail);
            window.localStorage.getItem("usermail");
            var submitButton = document.getElementById("submitnewsletter")
            submitButton.onsubmit = function () {
                emailjs.sendForm('service_ldfr7wv', 'newsletter', this);
                return true
            }
        }
    }
}

//Scroll to top button
$("button[id*='scrollUp-']").on("click", function () {
    $(document).scrollTop(0)
})

if (window.sessionStorage.getItem("session") !== null){
var preview = [];
//Sets up an array called Preview that input fields are pushed to.
var clearButton = document.getElementById("write-review")

//Resets preview array and clears residual in the input form. .each(function()) inspired by https://www.codegrepper.com/code-examples/javascript/jquery+clear+all+input+fields
clearButton.onclick = function () {
    preview = []
    $("#clear").find('input:text, textarea').each(function () {
        $(this).val(" ");
        $(this).removeClass("is-invalid").removeClass("is-valid");
    });
}
//Creates the function that takes the input from the add review form and pushes it to the preview array
function editReview(inputId) {
    review = document.getElementById((inputId)).value;
    preview.push(review);
}
//Prints the values from the preview array to the final form for submission
function print(elementId, index) {
    document.getElementById(elementId).setAttribute('value', preview[index])
}
//sets up the first continue button of the add review form modal
var button = document.getElementById("continueModal1");
//takes all inputs from the input form and prints it back to the user to allow for changes to be made before submitting reveiw.
button.onclick = function () {
    if ($("#rating-1").prop("checked") == true && $("#rating-2").prop("checked") == false) {
        $("#bean-rating").val("1")
    } else if ($("#rating-2").prop("checked") == true && $("#rating-3").prop("checked") == false) {
        $("#bean-rating").val("2")
    } else if ($("#rating-3").prop("checked") == true && $("#rating-4").prop("checked") == false) {
        $("#bean-rating").val("3")
    } else if ($("#rating-4").prop("checked") == true && $("#rating-5").prop("checked") == false) {
        $("#bean-rating").val("4")
    } else {
        $("#bean-rating").val("5")
    }

    editReview("bean-name")
    preview.push($("#bean-roast").prop("value"))
    editReview("bean-rating")
    editReview("bean-origin")
    editReview("brew-type")
    editReview("bean-description")
    preview.push($("#origin-type").prop("value"))
    print("bean_name", 0)
    $("#bean_roast").prop("value", preview[1])
    print("bean_rating", 2)
    print("bean_origin", 3)
    print("brew_type", 4)
    document.getElementById("bean_description").innerText = preview[5] //Print function couldn't be used as it relies on populating the value attribute.
    $("#origin_type").prop("value", preview[6])
}

function validate() {
    $("#validate").find('input:text, textarea').each(function () {
        if ($(this).val() == "") {
            $(this).addClass("is-invalid")
            $("#continueModal1").addClass("disabled")
        } else {
            $(this).removeClass("is-invalid").addClass("is-valid");
            $("#continueModal1").removeClass("disabled")
        };
    });
}

document.getElementById("disableContinue").onmouseover = function () {
    validate()
};

// Sets up a fallback image for the coffe being reviewed if the user does not have an image. Equally, reverts if the user changes their mind. 
var imgFallback = document.getElementById("imageLinkCheck")
var checkCount = 0;
imgFallback.onclick = function () {
    if (checkCount == 0) {
        $("#bean-image").val("https://cdn.pixabay.com/photo/2013/08/11/19/46/coffee-171653_960_720.jpg")
        $("#bean-image").addClass("disabled d-none")
        $("#bean-image-label").after("<p id='fallback-msg'>We'll add our own ;-)</p>")
        checkCount += 1
    } else if (checkCount == 1) {
        $("#bean-image").val("");
        $("#bean-image").toggleClass("disabled d-none");
        $("#fallback-msg").remove();
        checkCount -= 1;
    }

}

//Dynamically sets the button for editing image url on edit review as each id is dynmaically unique.
$("input[id*='imageUrl-']").on("click", function () {
    var editImg = $(this).attr("id");
    beanId = editImg.slice(9, 33);
    $("#bean_imageEdit-" + beanId).toggleClass("disabled d-none")
    $("#bean_imageLabel-" + beanId).toggleClass("disabled d-none")
})

//continuation of above as the image and affiatiate link inputs are in a different modal
var continueButton = document.getElementById("continueModal2")

continueButton.onclick = function () {
    editReview("bean-image")
    editReview("affialiate-link")
    print("bean_image", 7)
    print("affialiate_link", 8)
    /*Takes the value from rating selection and floats it.
     A while loop prints FA icons for equating to the value of 'fai' (font awesome icon) to form submission modal */
    fai = parseFloat(preview[2])
    let i = 0;
    while (i < fai) {
        $("#icon-rating").after('<i class="fas fa-coffee rating"></i>');
        i++;
    }
    purchase = preview[0].replace(/ /, "+")
    $("#affialiate_link").val("https://www.google.ie/search?q=" + purchase)
    if ($("#imageLinkCheck").prop("checked") == true) {
        $("#bean_image").addClass("disabled d-none")
        $("#bean_image").after("<p>Default Trusted Barista Image</p>")
    } else if ($("#bean-image").val() == "") {
        $("#bean_image").val("https://cdn.pixabay.com/photo/2013/08/11/19/46/coffee-171653_960_720.jpg");
        $("#bean_image").addClass("disabled d-none");
        $("#bean_image").after("<p>Default Trusted Barista Image</p>");
    }
}

/*Fixes bug where favourite button was still displaying on favourited reviews to user. 
Identifies an element wthat contains 'remove-favourite' in id and selects the next element, in this case the favourite button.
Adds bootstraps disabled and d-none class to hide and disable the button.  */
$(document).ready(function () {
    $("a[id*='remove-favourite']").next().addClass("disabled d-none");
    //Changes class on FA icon on hover
    $('.fa-star, .fa-trash-alt, .fa-comments, .fa-edit').hover(
        function () {
            $(this).toggleClass('far').toggleClass('fas')
        }
    )
})

//Used as part of the click function to use FA icon to checkbox
function rating(checkId) {
    if ($('#' + checkId).prop("checked") == false) {
        $('#' + checkId).prop("checked", true)
    } else if ($('#' + checkId).prop("checked") == true) {
        $('#' + checkId).prop("checked", false)
    }
}

//Controls the color of the icon based on the checkbox being checked or not by controlling .rating class
function checkIcon(thisCheckId, thisIconid) {
    if ($("#" + thisCheckId).prop("checked") == true) {
        $("#" + thisIconid).addClass("rating")
    } else {
        $("#" + thisIconid).toggleClass("rating")
    }
}

//Controls the checkboxes that preceed and ensure they remain checked
function prevCheck(thisCheckId, prevCheckId, prevIconId) {
    if ($("#" + thisCheckId).prop("checked") == true) {
        $("#" + prevCheckId).prop("checked", true);
        checkIcon(prevCheckId, prevIconId);
    } else {
        $("#" + prevCheckId).prop("checked", false);
        $("#" + prevIconId).removeClass('rating');
    }
}

/*Controls the checkboxes that come after a checked checkbox to ensure they are false e.g. if 3 is checked make sure 4 is off.
Also rechecks itself and checks that the icon color is turned on*/
function check(nextCheckId, nextIconId, thisCheckId, thisIconid) {
    if ($("#" + nextCheckId).prop("checked") == true) {
        $("#" + nextCheckId).prop("checked", false);
        checkIcon(nextCheckId, nextIconId)
        rating(thisCheckId)
        checkIcon(thisCheckId, thisIconid)
    }
}

//Checks other icons to ensure they're checked correctly according to the currently checked box
function checkOther(nextCheckId, nextIconId, thisCheckId, thisIconid) {
    if ($("#" + nextCheckId).prop("checked") == true) {
        $("#" + nextCheckId).prop("checked", false);
        checkIcon(nextCheckId, nextIconId)
        checkIcon(thisCheckId, thisIconid)
    }
}

//click functions for each check box
$("#one-rating").click(function () {
    $(this).toggleClass('rating')
    rating("rating-1")
    check("rating-2", "two-rating", "rating-1", "one-rating")
    checkOther("rating-3", "three-rating", "rating-1", "one-rating")
    checkOther("rating-4", "four-rating", "rating-1", "one-rating")
    checkOther("rating-5", "five-rating", "rating-1", "one-rating")
})

$("#two-rating").click(function () {
    $(this).toggleClass('rating')
    rating("rating-2")
    check("rating-3", "three-rating", "rating-2", "two-rating")
    prevCheck("rating-2", "rating-1", "one-rating")
    checkOther("rating-4", "four-rating", "rating-2", "two-rating")
    checkOther("rating-5", "five-rating", "rating-2", "two-rating")
})

$("#three-rating").click(function () {
    $(this).toggleClass('rating')
    rating("rating-3")
    check("rating-4", "four-rating", "rating-3", "three-rating")
    prevCheck("rating-3", "rating-2", "two-rating")
    prevCheck("rating-2", "rating-1", "one-rating")
    checkOther("rating-5", "five-rating", "rating-2", "two-rating")
})

$("#four-rating").click(function () {
    $(this).toggleClass('rating')
    rating("rating-4")
    check("rating-5", "five-rating", "rating-4", "four-rating")
    prevCheck("rating-4", "rating-3", "three-rating")
    prevCheck("rating-3", "rating-2", "two-rating")
    prevCheck("rating-2", "rating-1", "one-rating")
})

$("#five-rating").click(function () {
    $(this).toggleClass('rating')
    rating("rating-5")
    prevCheck("rating-5", "rating-4", "four-rating")
    prevCheck("rating-4", "rating-3", "three-rating")
    prevCheck("rating-3", "rating-2", "two-rating")
    prevCheck("rating-2", "rating-1", "one-rating")
})}}