## Table of contents
---- 

- [Overview](#Milestone-Project-3 "Milestone Project 3")  
- [The Trusted Barista](#The-Trusted-Barista "The Trusted Barista")  
- [User Experience](#user-experience-(ux) "User Experience")  
   - [User Stories](#user-stories "User Stories")  
        - [First Time Visitor Goals](#first-time-visitor-goals "First Time Visitor Goals")  
        - [Returning Visitor Goals](#returning-visitor-goals "Returning Visitor Goals")  
        - [Frequent User Goals](#frequent-user-goals "Frequent User Goals")  
        - [Admin User Goals](#admin-user-goals "Admin User Goals")
- [Design](#design "Design")  
    - [Colour Scheme](#colour-scheme "Colour Scheme")  
    - [Typography](#typography "Typography")  
    - [Imagery](#imagery "Imagery")  
    - [Wireframes](#wireframes "Wireframes")  
- [Features](#features "Features")  
- [Technologies Used](#technologies-used "Technologies Used")  
    - [Languages Used](#languages-used "Languages Used")  
        - [HTML5](#html5 "HTML5")  
        - [CSS3](#css3 "CSS3")  
        - [Javascript & JQuery](#javascript/query "Javascript & JQuery")  
        - [Python](#python "Python")
    - [Database](#database "Database")
        - [MongoDB](#mmongodb "MongoDB")
- [Frameworks, Libraries & Programs used](#frameworks-libraries-&-programs-used "Frameworks, Libraries & Programs used")  
    - [Bootstrap v.4.5.3](#bootstrap-v.4.5.3 "Bootstrap v.4.5.3") 
    - [Google Fonts](#google-fonts "Google Fonts")    
    - [Favicon](#favicon "Favicon")   
    - [Figma](#figma "Figma")  
    - [Coolors.co](#coolors.co "Coolors.co")  
    - [jQuery](#jquery "jQuery")  
    - [Git](#git "Git")  
    - [GitHub](#github "GitHub")  
    - [Gitpod](#gitpod "Gitpod") 
    - [Flask](#flask "Flask") 
    - [PyMongo](#pymongo "PyMongo")
    - [Werkzeug](#werkzeug "Werkzeug")
    - [Randomkeygen](#randomkeygen "Randomkeygen")
    - [EmailJS](#emailjs "EmailJS")
    - [Google Map Generator](#google-map-generator "Google Map Generator")
    - [Lighthouse](#lighthouse "Lighthouse")    
- [Testing](#testing "Testing")  
        - [Testing User Stories from User Experience (UX)](#testing-user-stories-from-user-experience-(ux) "Testing User Stories from User Experience (UX) Section")  
        - [First Time Visitor Goals](#first-time-visitor-goals "First Time Visitor Goals")  
        - [Returning Visitor Goals](#returning-visitor-goals "Returning Visitor Goals")  
        - [Frequent User Goals](#frequent-user-goals "Frequent User Goals")  
    - [Further Testing](#further-testing "Further Testing")  
    - [Known Bugs](#known-bugs "Known Bugs")  
- [Deployment](#deployment "Deployment")   
    - [Local Clone](#local-clone "Local Clone") 
    - [MongDB Setup](#2-mongodb-setup "MongoDB Setup")
    - [Environment Setup](#3-environment-setup "Environment Setup")
    - [Deployment to Heroku](#4-deployment-to-heroku "Deployment to Heroku")
    - [Development](#development "Development")  
    - [Bugs & Feature Requests](#bugs-&-feature-requests "Bugs & Feature Requests")  
- [Credits](#credits "Credits")  
    - [Code](#code "Code")  
    - [Content](#content "Content")  
    - [Media](#media "Media")  
    - [Acknowledgements](#acknowledgements "Acknowledgements")  
# Milestone Project 3 - The Trusted Barista
![GitHub languages count](https://img.shields.io/github/languages/count/LogisticBravo/Milestone-Project-3) ![GitHub top language](https://img.shields.io/github/languages/top/LogisticBravo/Milestone-Project-3) ![GitHub second language](https://img.shields.io/badge/Python-13.5%25-blueviolet) ![GitHub third language](https://img.shields.io/badge/Javascript-9.5%25-yellow) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/LogisticBravo/Milestone-Project-3) ![GitHub Commits](https://img.shields.io/github/commit-activity/m/LogisticBravo/Milestone-Project-3) ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/LogisticBravo/Milestone-Project-3) ![GitHub contributors](https://img.shields.io/github/contributors/LogisticBravo/Milestone-Project-3) ![GitHub forks count](https://img.shields.io/github/forks/LogisticBravo/Milestone-Project-3?style=social)   
![GitHub deployments](https://img.shields.io/github/deployments/LogisticBravo/Milestone-project-3/flask-ms3-coffee) ![Bootstrap badge](https://img.shields.io/badge/Bootstrap-V4.5.3-blueviolet) ![Font Awesome badge](https://img.shields.io/badge/FontAwesome-V5.15.1-blue) ![deployments](https://img.shields.io/badge/Deployment-heroku-brightgreen) ![Website](https://img.shields.io/website?down_color=red&down_message=Down&up_color=green&up_message=Up&url=https%3A%2F%2Fflask-ms3-coffee.herokuapp.com)

This was created to demonstrate learnings from the Code Institute software development course and marks the third of four milestone projects to be created. It utilises HTML, CSS,Javascript, Jquery, Pymongo, Jinja 2, MongoDB and UX by way of an interactive website that can store user data to the back end. 

## The Trusted Barista

The Trusted Barista is a website designed for coffee lovers. Inspired by the likes of trustpilot, TripAdvisor etc. It aims to provide an honest review site for finding the right coffee for it's users. It allows users to Create reviews, Read and search for reviews, Update said reviews and Delete reviews that they have created as well as providing a platform for conversation of reviews by way of comments.

For the site owner, it's purpose is to capture user email addresses so as to promote paid for content by way of advertising through newlestters and commissions by way of affiliate links. 

A live version of the site can be viewed [here](https://flask-ms3-coffee.herokuapp.com).

![image](mdassets/mdimages/responsivedisplays.png "Images of site on mutiple screen sizes")

## User Experience (UX)
### User stories
#### First Time Visitor Goals
* As a First Time Visitor, I want to understand the purpose of the site. 
* As a First Time Visitor, I want to easily navigate through the site.
* As a First Time Visitor, I want to be redirected to the landing page if I navigate to a wrong or broken link.
* As a First Time Visitor, I want to find the site owners social media channels. 
#### Returning Visitor Goals
* As a Returning Visitor, I want to create an account so that I can write reviews and add or delete comments.
* As a Returning Visitor, I want to engage with other users.
* As a Returning Visitor, I want to engage and be engaged with by the site owners.
* As a Returning Visitor. I want to find where I can purchase coffee of reviews that I like.
#### Frequent User Goals
* As a Frequent User, I want to access the site across a range of devices.
* As a Frequent user, I want to manage my profile and reviews that I have left. 
* As a Frequent user, I want to update my preferences.
* As a Frequent user, I want to favourite reviews that I like so as to easily find in the future. 
* As a frequent user, I want to ensure that my data is being used accordingly.  

#### Admin User Goals
* As an Admin, I want to enable or disbale other accounts with Admin permission. 
* As an Admin, I want to moderate site content of reviews.
* As an Admin, I want to remove users if necessary. 
* As an Admin, I want to see statistics on the number of users and reviews on the site. 

### Design
#### Colour Scheme
The site uses the following 3 colours primarily.   
![image](mdassets/mdimages/colors.png)
* Atomic Tangerine - rgb(249,148,89) #f99459
* Jet Grey - rgb(60,58,67) #3C3A43
* White - rgb(255,255,255) #ffffff

In addition, the site also utilises the following colours for some Bootstrap buttons:   
* btn-success - (Sea Green) - rgb(25,135,84) #198754
* btn-danger - (Rusty Red) -  rgb(220,53,69) #dc3545
* btn-secondary -(Slate Grey) - rgb(108,117,125) #6c757d

#### Typography
* [Fredericka the Great](https://fonts.google.com/specimen/Fredericka+the+Great) is used on all `<h>` elements and major headings such as the brand logo in the header and footer throughout the site with cursive as a fall back in case of errors in loading the font. Fredericka the Great is a stylish popular choice as a chalkboard esque font and so fits the target market of those that would frequent coffee shops that would typically have menu's on hip blackboard's. It gives a modern and trendy feel to the site. 
* [Stardos Stencil](https://fonts.google.com/specimen/Stardos+Stencil) is used on all other primary elements such as `<p>, <span>` etc. Stencil fonts are a popular choice amidst many within the hospitality indusrty as a menu font so it was a fitting choice that complimented the design ethos of the site in addition to complimenting Fredericka the Great font.  
#### Imagery
The site uses only 4 images natively. 5 if you were to consider the logo branding as an image (styled using CSS). 
* The image that covers the navbar.
* The hero image of coffee beans found on the index page.
* A fallback image is used for users that do not have a link to an image when leaving reviews.
* A default user profile image is used for all users.  

All other additional images outside of this are user generated by way of an image link when adding a review.
#### Wireframes
![wireframeimage](mdassets/mdimages/wireframe.png)   

Full Wireframes drawn up using Figma can be found [here]()

## Features
* 
* 
* 
*    
* 
*    
   
![IDE Theme](mdassets/mdimages/idetheme.png)    
* 
* Custom 404 page should the user navigate to a non-existant link which will automatically be redirected to home.   
This can be tested [here](https://flask-ms3-coffee.herokuapp.com/404)    
![404 page image](mdassets/mdimages/404.png)    

## Technologies Used
### Languages Used
#### [HTML5](https://www.w3schools.com/html/default.asp)
* Html5 and semantic markup is used for the creation of this website.
#### [CSS3](https://www.w3schools.com/css/default.asp)
* CSS is used for styling various elements throughout the site. 
#### [Javascript/JQuery](https://www.w3schools.com/js/default.asp)
* JavaScript and Jquery language is used for development of some front features of the website and activation of Bootstrap features. 
#### [Python](https://www.w3schools.com/python/)
* Python 3 is used as the main application language.    

### Database
#### [MongoDB](https://cloud.mongodb.com/)
* MongoDB is used for storing and reading backend data.    

### Frameworks, Libraries & Programs Used
#### [Bootstrap v.5.0.0-beta-1](https://getbootstrap.com/) 
* Bootstrap was used throughout the project for it’s responsiveness of the website and styling such as paddings and margins. 
#### [Google Fonts](https://fonts.google.com/)  
* Google fonts were used for the importing of the ‘Fredericka the Great’ and ’ Stardos Stencil’ fonts to the style.css page which is used throughout the entirety of the site.
#### [Favicon]()  
* favIcon was used to create the site favicon.
#### [Figma](https://figma.com/)
* Figma was used to create wireframing.
#### [Coolors.co](https://coolors.co/)
* Coloors was used to assist with choosing the colour scheme that is used throughout the website.
#### [jQuery](https://www.w3schools.com/jquery/default.asp)
* jQuery was used extensively in the script files.
#### [Git](https://git-scm.com/)
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
#### [GitHub](https://github.com/)
* GitHub is used to store the projects code after being pushed from Git.
#### [Gitpod](https://gitpod.io/)
* Gitpod was used as the primary IDE for development of the site.  
#### [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* Flask was used for it's Python web framework such as Jinja2 templating.    
#### [PyMongo](https://pypi.org/project/pymongo/)
* PyMongo is is a native Python driver for MongoDB allowing for interaction with MongoDB databases from Python.
#### [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/utils/)
* Werkzeug is one of the most advanced WSGI utility libraries. It was used primarily for debugging and security helpers.
#### [Randomkeygen](https://randomkeygen.com/)
* randomkeygen.com was used as a secure password and keygen generator for creation of the Flask SECRET_KEY.
#### [EmailJS](https://www.emailjs.com/)
* emailjs uses their own Javascript language to trigger the sending of emails using client-side technologies and was used for the automated responses to the signing up to the newsletter and contact us form. 
#### [Google Map Generator](https://google-map-generator.com/)
* Google Map generator was used to generate the iframe used for the embedded map found on the contact page and it's associated styling found in the css stylesheet. 
#### [Lighthouse](https://developers.google.com/web/tools/lighthouse)
* Lighthouse, a Google Web Dev tool, was used extensively for testing performance, accessability, best practices and SEO of the site in it's entirety.

## Testing
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>

<a href="https://validator.w3.org/">
<img style="border:0;width:88px;height:31px"
        src="https://www.w3.org/Icons/valid-html401-blue"
        alt="Valid HTML!" /> 
        </a>

All links have been extensively tested to ensure correct continuity.

### Testing User Stories from User Experience (UX)
#### First Time Visitor Goals
*    
* 
* The site has a fun 404 page.    
![Typewriter effect](mdassets/mdimages/typewrite.png)
#### Returning Visitor Goals
* 
*    
![Easter Egg](mdassets/mdimages/easteregg.png)
#### Frequent User Goals
* The site is responsive across Desktops, tablets and mobile devices and was tested using Chrome Developer tools on Ipad, Ipad Pro, Iphone 6,7,8 X, Xiaomi F2, Xiamoi F1, Mac pro, MacBook and Safari.   
*     
![Mobile View](mdassets/mdimages/mobile.png)

#### Further Testing
Lighthouse, a Google Chrome web developement tool, was used extensively on the site in it's entirety. Every individual page was tested for desktop and mobile and received a score of in excess of 80+ across Performance, Accessability, Best Practices and SEO.    
![Lighthouse Screenshot](mdassets/mdimages/lighthouseresult.png)    
A copy of the Lighthouse report for each individual page can be found below:    
* Index - [Lighthouse Desktop Result](mdassets/pdf/index-lighthouse-report-desktop.pdf) | [Lighthouse Mobile Result](mdassets/pdf/index-lighthouse-report-mobile.pdf)
* CV - [Lighthouse Desktop Result](mdassets/pdf/cv-lighthouse-report-desktop.pdf) | [Lighthouse Mobile Result](mdassets/pdf/cv-lighthouse-report-mobile.pdf)
* 404 - [Lighthouse Desktop Result](mdassets/pdf/404-lighthouse-report-desktop.pdf) | [Lighthouse Mobile Result](mdassets/pdf/404-lighthouse-report-mobile.pdf)
#### Known Bugs
* The pixel icon dissappears on one occasion when typing out solve.

## Deployment

The website was created using Gitpod IDE. GitHub was used for hosting the repository and the environment is then deployed to Heroku for hosting. The following are the steps needed to set up your IDE, clone the repository and deploy to Heroku. In addition to those listed, MongoDB is used for storing the data and is also required for successful deployment. 

### 1. Clone the Repo
#### Local Clone
1. Navigate to the GitHub Repository: [Milestone Project 3 - The Trusted Barista ](https://github.com/LogisticBravo/Milestone-project-3)
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the dialogue box.
4. Open your developement editor of choice and open a terminal window in a directory of your choice.
5. Use the 'git clone' command in terminal followed by the copied git URL.    

        git clone https://github.com/LogisticBravo/Milestone-project-3
6. A clone of the project will be created locally on your machine.

### 2. MongoDB Setup
1. If you don't have one already, create an account for MongoDB [here](https://www.mongodb.com/try).
2. Once signed in and within Atlas > Clusters > Collections : Create a Database.
3. Name the database "coffee_beans".
4. Within this database, create the followoing collections (case sensitive):    
    - beans
    - newsletters
    - origin
    - privacy_policy
    - roast
    - users

### 3. Environment Setup
1. Install requirements.txt via your IDE terminal window for dependencies and external libraies. *Important 

        pip3 install -r requirements.txt 

2. Create the `env.py` file and within it add the following:    

        import os 
        os.environ.setdefault("IP", "0.0.0.0")     
        os.environ.setdefault("PORT", "5000")     
        os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")   
        os.environ.setdefault("MONGO_URI", "YOUR_MONGODB_URI")    
        os.environ.setdefault("MONGO_DBNAME", "YOUR_MONGODB_DATABASE_NAME")

    - Generate a secret key at [Randomkeygen.com](https://randomkeygen.com/) if you do not have one.    
3. Ensure that  "`env.py`" is added to your `gitignore` file. 
4. Ensure that your `Procfile` (case sensitive) is present. On the off chance that it is not:

        touch Procfile
    within it add the following:

        web: pyton app.py
5. Ensure that the above steps have been completed succesffully before proceeding to deployment. 
6. Stage, commit and push your local repo to GitHub.

        git add -A
        git commit -m "Initial Commit"
        git push

### 4. Deployment to Heroku
1. If you haven't already, Create an account and login to [Heroku](https://signup.heroku.com/).
2. Create a new app and give it a unique new name. Importance on unique as Heroku will flag if it's already taken. For simplicity, it's suggested to keep this aligned to your GitHub repository.
3. Choose from the available Shard options - EU or US - It's best to select closest to your location.
4. Navigate to App settings > 'Config Vars'
5. Replicate your previous variables from the `env.py` file here and ensure they match exactly.    

    |  Key | Value  |
    |:-:|:-:|
    |  IP |  0.0.0.0 |   
    |  PORT | 5000  |   
    |  SECRET_KEY |  YOUR_SECRET_KEY |   
    | MONGO_URI  |  YOUR_MONGODB_URI |   
    |  MONGO_DBNAME |  YOUR_MONGODB_DATABASE_NAME |   

6. From Heroku App deploy page:
    - Choose GitHub from the Deployment Method.
    - Hit "Connect to GitHub".
    - Log in to your GitHub from Heroku to link the App to GitHub.
    - Search for and select the repository to be linked in Github.
    - Hit Connect.
    - Choose Enable Automatic Deployment from the GitHub Master / Main branch.    
    
7. Open the App to confirm deployment. Note that Heroku can be slow to open on the first instance. 
  

### Development
We welcome all contributions. To do so:

1. Fork the Repo.
2. Log in to GitHub and locate the [Respository](https://github.com/LogisticBravo/Milestone-project-3).
3. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
4. You should now have a copy of the original repository in your GitHub account.	
5. Create a new branch.
6. Make your changes and ensure adequate testing with supporting documents.
7. Adhere accordingly to the existing style. 
8. Commit often with clear commit messages.
9. Push to the branch.
10. Create a pull request.

### Bugs & Feature Requests

Should you find a bug and want to help us squash it. Please open an issue [here](https://github.com/LogisticBravo/Milestone-project-3/issues/new) ensuring you add the '**bug**' label  with clear detail under the following:
* What you done?
* Where you done it?
* What you expected to happen?
* What actually happened?
	
To request a new feature or function then please open an issue [here](https://github.com/LogisticBravo/Milestone-project-3/issues/new) ensuring you add the '**enhancement**' label  with proposed changes including snippets of how to do so.

## Credits

### Code
* Bootstrap 5.0.0-beta-1: Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System and classes for padding, margins etc.
* CSS Styling code and corresponding classes/id’s was largely that of the developer Jay Bradley. Additional code is commented within the stylesheet itself. Most notable of which is the code used for the `.cutout` class courtesy of [w3Schools](https://www.w3schools.com/howto/howto_css_cutout_text.asp) which was used to style the Trusted Barista logo in the navbar and footer. 
* With the exception of the following, all Javascript and JQuery code is that of the developer.
    *  The onscroll trigger for the `newsletter()` function in review.js was inspired by [w3schools](https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onscroll3).
    * The local storage aspect of the `newsletter()` function in review.js was inspired by [Stackoverflow](https://stackoverflow.com/questions/8123032/how-do-i-make-a-count-variable-persistent-across-sessions).
    * The `.each(function())` within the `clearButton.onClick` in review.js was adapted from this [Codegrepper Post](https://www.codegrepper.com/code-examples/javascript/jquery+clear+all+input+fields).
    * Initializers from the Bootstrap library to inititiate the modals and tooltips.
* With exception of the authentication functionality to login using Werkzeug security helpers for salt & hash passwords and the basic structure of the CRUD functionality adapted from the Code Institute walkthrough projects of the Task manager, all other and additional Python code and logic is that of the developer Jay Bradley.
* Jinja2 templating is used for dynamic rendering. All jinja logic is that of the developer Jay Bradley. 
* [Python Tutor](http://pythontutor.com/) was used to troubleshoot logic when dealing with nested arrays on more than one occasion. 
* The hero image callout was adapted by the [starbootstrap theme business casual](https://startbootstrap.com/previews/business-casual).


### Content
* The structure and concept were entirely that of the the developer Jay Bradley. 
* All language and content is that of the developer Jay Bradley with the exception of reviews written by user 'Jay21' which were largely copied from the corresponding reviewed coffee's facebook. 


### Media
*   
* 

### Acknowledgements
* My wife for her continued and tireless support as I worked through this project.
* My Mentor, Seun for her great feedback and continously pushing me.
* 
*  
* 
* 
* 