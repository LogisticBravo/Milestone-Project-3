var preview = [];
//Sets up an array called Preview that input fields are pushed to.
var clearButton = document.getElementById("write-review")

//Resets preview array and clears residual in the input form. .each(function()) inspired by https://www.codegrepper.com/code-examples/javascript/jquery+clear+all+input+fields
clearButton.onclick = function (){
   preview = []
   $("#clear").find('input:text, textarea').each(function(){
       $(this).val("");
    });
}
//Creates the function that takes the input from the add review form and pushes it to the preview array
function editReview(inputId){
    review = document.getElementById((inputId)).value;
    preview.push(review);
}
//Prints the values from the preview array to the final form for submission
function print(elementId, index){
    document.getElementById(elementId).setAttribute('value',preview[index])
}
//sets up the first continue button of the add review form modal
var button = document.getElementById("continueModal1");
//takes all inputs from the input form and prints it back to the user to allow for changes to be made before submitting reveiw.
button.onclick = function () {
    editReview("bean-name")
    editReview("bean-roast")
    editReview("bean-rating")
    editReview("bean-origin")
    editReview("brew-type")
    editReview("bean-description")
    print("bean_name",0)
    print("bean_roast",1)
    print("bean_rating",2)
    print("bean_origin",3)
    print("brew_type",4)
    document.getElementById("bean_description").innerText = preview[5] //Print function couldn't be used as it relies on populating the value attribute.
}
//continuation of above as the image and affiatiate link inputs are in a different modal
var continueButton = document.getElementById("continueModal2")

continueButton.onclick = function () {
    editReview("bean-image")
    editReview("affialiate-link")
    print("bean_image",6)
    print("affialiate_link",7)
}
