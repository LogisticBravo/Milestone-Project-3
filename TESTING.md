# Contents

- [Testing User Stories](#testing-user-stories "Testing User Stories")
    - [First Time Visitor Goals](#first-time-visitor-goals)
        - [Test Case 1](#test-case-1 "Test Case 1")
        - [Test Case 2](#test-case-2 "Test Case 2")
        - [Test Case 3](#test-case-3 "Test Case 3")
        - [Test Case 4](#test-case-4 "Test Case 4")
    - [Returning Visitor Goals](#returning-visitor-goals)
        - [Test Case 5](#test-case-5 "Test Case 5")
        - [Test Case 6](#test-case-6 "Test Case 6")
        - [Test Case 7](#test-case-7 "Test Case 7")
        - [Test Case 8](#test-case-8 "Test Case 8")
    - [Frequent Visitor Goals](#frequent-visitor-goals)
        - [Test Case 9](#test-case-9 "Test Case 9")
        - [Test Case 10](#test-case-10 "Test Case 10")
        - [Test Case 11](#test-case-11 "Test Case 11")
        - [Test Case 12](#test-case-12 "Test Case 12")
        - [Test Case 13](#test-case-13 "Test Case 13")
    - [Admin User Goals](#admin-user-goals "Admin User Goals")
        - [Test Case 14](#test-case-14 "Test Case 14")
        - [Test Case 15](#test-case-15 "Test Case 15")
        - [Test Case 16](#test-case-16 "Test Case 16")
        - [Test Case 17](#test-case-17 "Test Case 17")

## Testing User Stories
### First Time Visitor Goals
#### Test Case 1

> As a First Time Visitor, I want to understand the purpose of the site.

**Description**
Verify that the site's purpose is clear to a user when they land on the landing page of the site. Verify that the site's purpose is clear to a user when they land on the landing page of the site.Verify that the site's purpose is clear to a user when they land on the landing page of the site.

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. If on mobile, a minor scroll to continue reading the content will be required. 
4. On larger devices, Read the content present with the callout hero image.
5. Confirm that the sites intention is clear.

**Expected Result:**
A 'callout-text' div should be present outlining the purpose of the site. 

**Actual Result:**
A 'callout-text' div is present which outlines the purpose of the site. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 2

> As a First Time Visitor, I want to easily navigate through the site.

**Description**
Verify that the site contains an intuitive navigation menu and sitemap.

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. If on mobile, a 'Hamburger' icon will be present and require tapping.
4. On larger devices, confirm that the sites navigation links are present in the navbar.
5. Confirm that the site contains a sitemap in the footer.
6. Confirm that the current active page is evident.
7. Navigate through all site links to ensure continuity.
7. Create an account, log in and repeat the above steps. 
8. Confirm that the footer links are dependant on a user logged in or not.

**Expected Result:**
 - When visiting the site, the Navbar should contain a clearly defined navigation menu. 
 - The footer should contain a Sitemap that is conjucent with if a user is logged in or not. 
 - The current active page should be highlighted in the navbar. 

**Actual Result:**
 - When visting the site, the navbar is clearly present and is familiar to the user. 
 - When on mobile, a "hamburger" icon is present and is familiar to the user. Tapping this reveals the navigation links. 
- The navigation menu remains consistent throughout site navigation. 
- When logged in the sitemap in the footer reads "My Account" as opposed to "Sign-Up" when the user is not logged in. 
- The current active page is highlighted with #f99459 and underlined.  

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 3

> As a First Time Visitor, I want to be redirected to the landing page if I navigate to a wrong or broken link.

**Description**
Verify that the site contains a 404 page that is evident to the user they have navigated to a wrong or broken link. Verify that the page is directs the user to return to the homepage.

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/404](https://flask-ms3-coffee.herokuapp.com/404)
3. Alternatively, navigate to [https://flask-ms3-coffee.herokuapp.com/YOUR_RANDOM_STRING](https://flask-ms3-coffee.herokuapp.com/YOUR_RANDOM_STRING)
4. Confirm that the page states it is a 404 page and that something went wrong. 
5. Confirm that it directs the user to return to the Home page.
6. Confirm that the link to the Home page returns the user to the Home page. 
7. Create and account, login and repeat the above steps.


**Expected Result:**
 - When visiting a wrong or broken link, the user should land on a 404 page that is clearly defined. 
 - It should feature a button that directs the user to "Go Home".
 - Clicking the button should return the user to the Home page. 
 - The expected result should take place regardless of the user being signed in or not.

**Actual Result:**
 - When navigating to [https://flask-ms3-coffee.herokuapp.com/404](https://flask-ms3-coffee.herokuapp.com/404) or [https://flask-ms3-coffee.herokuapp.com/YOUR_RANDOM_STRING](https://flask-ms3-coffee.herokuapp.com/YOUR_RANDOM_STRING) a clearly defined 404 page is displayed to the user which states that something went wrong. 
 - The 404 page displays a button directing the user to "Go Home".
 - Clicking this button returns the user to the Home Page.
 - The same happens regardless of the user being signed in or not.

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 4

> As a First Time Visitor, I want to find the site owners social media channels.

**Description**
Verify that the site contains 5 established social media icons in the footer. Verify that clicking these icons directs the user to the associated social media channel in a new tab. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Confirm that there are 5 recognisable social media icons within the footer of the site.
4. Hover over each icon to confirm that the currently selected one is made aware to the user by way of highlightin it with #f99459.
5. Click each social media icon respectively and confirm that each opens up to the related social media channel in a new tab. 


**Expected Result:**
 - When visiting the site there should clearly be branded social media icons in the footer. 
 - When hovering on these icons they should be coloured with #f99459 alerting the user that it is the current icon they are hovering. 
 - Clicking the respective icons should open the related social media channel in a new tab. 

**Actual Result:**
 - When visiting the site there is clearly 5 branded icons in the footer.
 - When hovering the icons, it is clearly higjlighted with #f99459 alerting the user that it is the current icon being hovered upon. 
 - Clicking the respective icons opens up the associated social media channels in a new tab in the browser. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

### Returning Visitor Goals
#### Test Case 5

> As a Returning Visitor, I want to create an account so that I can write reviews and add or delete comments.

**Description**
 Verify that when on the reviews page that reviews cannot be added and that the user is prompted that they must be logged in if they wish to add comments. Verify that the site contains a sign-up page and confirm that an account can be created. Verify that once an account is created and the user signed in that they can add reviews, add comments and delete comments and reviews that they have added.  

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/reviews](https://flask-ms3-coffee.herokuapp.com/reviews)
3. Confirm that there is no option or facility to add a review when not logged in.
4. Click on the comments tab (signalled by speech bubbles icon) and confirm that there is no option or facility to add comments or delete comments. 
5. Confirm that the user is prompted that they must be logged in to add comments. 
6. Create an account or sign in and confirm that as a user there is a "Write Review" button on the reviews page. 
7. Confirm that when on the comments tab that a user is displayed with a comment box and a button that say's "Add".
8. Confirm that clicking the "Write Review" button opens a modal to write a review. 
9. Confirm that a review is added after completing the "Write Review" modal/form. 
10. Confirm that a comment is added after adding a comment to the comment input and clicking "Add".
11. Confirm that having left a comment, the user is displayed a "delete" button. 
12. Confirm that clicking the delete button removes the comment. 
13. Confirm that the user is displayed with an edit icon and trasj icon on the review that they have added. 
14. Confirm that clicking the edit review icon allows the user to edit the review. 
15. Edit the review and confirm that the edit's took effect.
16. Click on the trashcan icon and confirm that the review is removed. 

**Expected Result:**   
The following should be visible to a user only when they are logged in:
 - A "Write Review" button.
 - An Edit icon (paper with pencil) on a review that have created.
 - A Delete icon (trash can) on a review they have created. 
 - A comment input box and "Add" button on all reviews comment tab. 
 - A "delete" button on all comments that they have added.

 Clicking the "Write Review" button should open a modal with a form and guide the user through adding a review by way of tooltips. After a user has submittted the form the review should be added to the reviews page. 

 Clicking the Edit icon should open a modal form that allows the user to edit their existing review and should only be visible on reviews that the user has added. Editing this form should be reflected in the review after it's submission. 

 Clicking the comments tab on any review should show an input box with an "Add" button. Adding text to this inpout box and clicking "Add" should attach the comment to the review. 

 Any comments left by a user should have a "delete" button attached to it. Clicking "delete" on a comment should remove the comment. 

 Clicking the trash can icon, delete, should remove the review from the page and should only be visible to reviews that the user has added. 

**Actual Result:**
- Navigating through the page when not logged in displays no buttons to write a review. 
- There are no icons visible on reviews themselves to edit or delete even for reviews that the user has added as the user is not logged in. 
- There is no input box or add button on any comments when not logged in. There are also no "delete" buttons on any comments even for comments left by the user as they are no logged in. 
- The comments section prompts the user that they must be logged in to add a comment. 
- When logged in the following is visible to the user:
    - A "Write Review" button.
    - An Edit icon (paper with pencil) on a review that have created.
    - A Delete icon (trash can) on a review they have created. 
    - A comment input box and "Add" button on all reviews comment tab. 
    - A "delete" button on all comments that they have added.
- When logged in, navigating through the Write review modal/form add's a new review to the page. 
- When logged in, clicking the Edit icon a review allows it to be edited and it's changes reflected within the newly published review. 
- When logged in, clicking the trash icon removes the review from the page. 
- When logged in, adding a comment is attached to the respective review. 
- When logged in, clicking the delete button on a commment removes the comment from the respective review. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 7

> As a Returning Visitor, I want to engage and be engaged with by the site owners.

**Description**   
Verify that for the first time scrolling the reviews page, whether logged in or out that a pop-up "Newletter Sign Up" modal appears. Verify that if a user is not logged in and subscribes to the newsletter that they are directed to the sign-up page and the email input box is pre-populated with the email address that the user entered for the subscription they created. Verify that the user receives an email if they subscribe to the Newsletter through this modal. Verify that the site contains a contact us page with a contact form. Verify that the user recveives confirmation of form submission and an email for contacting the site owner.  

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/reviews](https://flask-ms3-coffee.herokuapp.com/reviews)
3. Scroll down the reviews page and confirm that a newsletter modal is shown to the user. 
4. Complete the form and submit it. 
- Confirm if not logged in that the user is directed to the sign up page.
- Confirm that the email address input to the newsletter modal was pre-populated to the email input of the sign up form. 
- Confirm that if logged in that the user receives a toast thanking them for updating their subscription. 
5. Check the email inbox and confirm that an email was receieved confirming subscribtion to the newsletter. 
6. Navigate to [https://flask-ms3-coffee.herokuapp.com/contact](https://flask-ms3-coffee.herokuapp.com/contact) or "Contact us" via the footer.
7. Confirm that there is a contact form on this page. 
8. Complete and submit the form and confirm that a form is replaced with a message confirming it's submisison. 
9. Check the email inbox of the email address used and confirm that an email relating to the contact form was received. 


**Expected Result:**
 - When scrolling the reviews page for the first time a modal pop up event should occur that prompts the user to subscibe to the newsletter. 
 - Completing this form should trigger an email delivered to the users inbox and if not logged in direct them to the signup form with their email address pre-populated. 
 - If logged in the user should receive a toast thanking them for updating their subscription. 
 - The user should receive an email relating the newsletter subscription. 
 - On the contact us page, a contact form should be visible.
 - Completing and submitting the contact form should remove the contact form and display a message confirming it's submission. 
 - The user should receive an email relating to the contact form. 

**Actual Result:**
- When scrolling the reviews page for the first time, a newsletter modal pop's up prompting the user to subscribe to the Newsletter. 
- Completing this and submitting the form directs the user to the sign-up page with their email address pre-populated if not logged in. 
- The user receives an email relating to the newsletter. 
- There is a contact form on the contact us page. 
- Submitting the contact form removes the form and displays a message confirming it's submission. 
- The user receives an email relating to the contact us form. 
- If logged in and subscribing to the newsletter via the Newsletter modal, the user receives a toasts thanking them for updating their subscription.  

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 8

> As a Returning Visitor, I want to find where I can purchase coffee of reviews that I like.

**Description**   
Verify that each review has an **Affiliate link attached to it. Confirm that clicking this link opens in a new tab and that the user is taken to the respective affiliate link website. 

**An Affiliate link is simulated in this instance. The simulated link takes the title of the coffee review and opens up a google search of that title in a new tab. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/reviews](https://flask-ms3-coffee.herokuapp.com/reviews)
3. Select any review and confirm that under the image of that review is a link that says "Available to buy Here".
4. Confirm that clicking this link opens in a new tab. 
5. Confirm that the link that was opened in a new tab is a google search of the title of that review. 


**Expected Result:**
 - When scrolling the reviews page, under each review there should be a link under every image that states "Available to buy here"
 - Clicking the link should open a google search of the title of that review in a new tab. 

**Actual Result:**
- All reviews have a link under the image of the review that states "Available to buy here"
- Clicking the link opens a google search of the title of that review in a new tab.   

**Pass/Fail:**
Pass

**Image of Test Result:** 

### Frequent Visitor Goals
#### Test Case 9

> As a Frequent User, I want to access the site across a range of devices.

**Description**   
Verify that the site is responsive across a range of media devices. Confirm that everything is clearly visible and accessible.  

**Steps**
1. Open Google Chrome browser.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Using Chrome Dev tools (F12 on your keyboard)
4. Select the "Toggle Device Toolbar" icon (CMD Shift M on a mac).
5. Using the dropdown menu to select a range of device sizes. 
6. Test every page of the website using this method across different device selections. 


**Expected Result:**
 - When navigating the website through different devices all elements, modals, forms etc. should visible and clear. Confirm that the UI of the site maintains it's structure across various screen sizes. 

**Actual Result:**
- The site is responsive across Desktops, tablets and mobile devices and was tested using Chrome Developer tools on Ipad, Ipad Pro, Iphone 6,7,8 X, Xiaomi F2, Xiamoi F1, Mac pro, MacBook and Safari and Chrome browsers. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 10

> As a Frequent user, I want to manage my profile and reviews that I have left.

**Description**   
Verify that on the profile page the user is displayed a list of reviews that they have left. Verify that a user has the ability to change their username from their profile page and update their password. 
* Confirm that a change takes effect when a user changes their username.
* Confirm that a change takes effect when a user updates their password. 
* Confirm that a list of reviews that the user has left is listed on the profile page. 
* Confirm the list of reviews links to that respective review where the user can edit or delete the review. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Using the login option - log into your account. 
4. On the profile page, confirm that there is an option to update the users username and password beneath the profile image. 
5. On the profile page, confirm that there is a list of reviews that the user has written.
6. Confirm that each review in this list is a clickable link which takes the user to the respective reveiw on the reviews page. 
7. Confirm that the review can be edited and deleted. 
8. On the profile page, confirm that the username can be updated. 
9. On the profile page, update the password, logout and login again with the new password to confirm the password was updated. 


**Expected Result:**  
 Logging into the profile page, the user should be displayed with an input field to update their username or password.
 - Each input field should have a palceholder describing it's purpose. 
 - Each input field should have an update button associated with it. 
 - Updating the user's username should be reflected in the profile and the user receive a toast confirming it's update.
 - When updating the username, the user should have to authenticate their password to finalize the update. 
 - Updating the password should return a toast to the user confirming the password was updated. 

 On the profile page should be a list under the heading of "My Reviews" which lists all the reviews the user has added, if any. 
 - Each review in this list is a clickable link and underlined to draw attention to it being a link. 
 - Clicking this link should take the user to that respective review and allow them to edit or delete the review.

**Actual Result:**
- Logging into the Profile page, the user is displayed two input fields with placeholders and associated "Update" buttons. Within each input field is placeholder text outlining their intentions.  
- Adding a new username to the username input box updates the user's username and is reflected in the newly refreshed site. The user receives a toast that their username was updated. 
- When updating their username, if the user inputs an incorrect password during authentication of this change the username is not changed and the user receives a toast warning the password was incorrect. 
- Entering a new password in the password field and clicking update updates the password. 
- Logging out and logging back in with the new password is successful.

**Pass/Fail:**
Pass

**Image of Test Result:**

#### Test Case 11

> As a Frequent user, I want to update my preferences.

**Description**   
Verify that on the profile page the user is displayed a 'Subscription' toggle switch. Confirm that toggling this switch updates the user's preferences to their subscription. Confirm that backing out of the change reverts the toggle to it's original state.  

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Using the login option - log into your account. 
4. On the profile page, confirm that there is a "Subscription" toggle beaneath the password update field. 
5. Toggle this switch and confirm a modal pop up asking to confirm your change to subscription status. 
6. Verify that when this change is submitted the toggle is set correctly and that the user receives a toast confirming the change to their subscription. 
7. Do this again and confirm that the modal pop up differs to the last. 
8. Verify that when backing out or cancelling the confirmation of changing the subscription status that the toggle reverts to it's original state. 


**Expected Result:**  
-  Logging into the profile page, the user should be displayed with a "Subscription" toggle.
- The subscription status should be set to their current prefences based on their original sign up. i.e if they selected the checkbox to subscribe to the newsletter then the subscription toggle should be in the 'on' position. 
- Toggling this should fire a modal pop up to confirm their change to their subscription. 
- The content of this modal should vary dependant on the current status of their subscription. 
- Backing out of this modal, i.e. not confirming the change to their subscription should rever the toggle to it's original state.
- Confirming the modal should update their preferences and the user should receive a toast confirming the change. The toggle should be in the position that reflects their current subscription preference status.


**Actual Result:**
- Logging into the profile page, the user is displayed with a "Subscription" toggle.
- The toggle is set reflective of their current subscription status. 
- Toggling the toggle presents the user with a modal to confirm the change to their preference. 
- The content of the modal is differnet dependant on their current subscription preference. 
- Backing out or cancelling the confirmation modal reverts the toggle to it's original state. 
- Confirming the change to their preference is reflected with a toast to the user to confirm the change and the toggle is switched to reflect their current subscription preference.
- Navigating away from the profile page and returning to it displayes their correct subscription preference. 

**Pass/Fail:**
Pass

**Image of Test Result:**

#### Test Case 12

> As a Frequent user, I want to favourite reviews that I like so as to easily find in the future.

**Description**   
Verify that on the reviews page there is a star icon assocaited with each review. Verify that when clicked the star icon remains in an 'on' state. i.e that it is coloured. Verify that on the users profile page a list of reviews that have been favourited is displayed to the user under the heading of "My favourites". Confirm that each review in this list is a clickable link which takes the user to that review on the reviews page. Confirm that unchecking a favourite removes the solid star and that the favourite is removed from the favourites list on the users profile page. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Using the login option - log into your account. 
4. On the profile page, confirm that there is a "My favourites" list of reviews that have been favourited, if any. 
5. Navigate to the reviews page and confirm that each review has a star icon. 
6. Confirm that clicking this icon switches it to an 'on' solid state. 
7. Confirm that the favourited review is displayed on the users profile page under the 'My favourites" list. 
8. Confirm that clicking the link in this list takes the user to the respective review on the reviews page. 
9. Confirm that unfavouriting a review removes the solid state of the star icon and returns it to an 'off' state. 
10. Confirm that the favourite is removed from the list on the profile page of the user.  


**Expected Result:**  
-  When logged in and on the reveiws page the user should see a star icon associated with each review. 
- Clicking the star icon should turn it to a solid 'on' state. 
- The review should be added to a list on the user profile page under the heading of "My favourites".
- Each review in this list should be a clickable link and highlighted as such by way of an underline. 
- Clicking this link should take the user to that review. 
- Unfavouriting the review should remove the 'solid' state of the star icon and return it to an 'off' state. 
- The review should be removed from the users "My favourites" list. 


**Actual Result:**
-  When logged in and on the reveiws page the user see's a star icon associated with each review. 
- Clicking the star icon switches it to a solid 'on' state. 
- The review is added to a list on the user profile page under the heading of "My favourites".
- Each review in this list is a clickable link and highlighted as such by way of an underline and by increasing font size on hover. 
- Clicking this link takes the user to the associated review. 
- Unfavouriting the review removes the 'solid' state of the star icon and returns it to an 'off' state. 
- The review is removed from the users "My favourites" list.

**Pass/Fail:**
Pass

**Image of Test Result:**

#### Test Case 13

> As a Frequent user, I want to ensure that my data is being used accordingly.

**Description**   
Verify that there is a link to a "privacy policy" in the footer of the site. Confirm that visiting this link displays the user with a "Privacy policy". Confirm that this link is visible and can be visitied regardless of a user being logged in.  

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Navigate to the footer of the site. 
4. Confirm that there is link to a "Privacy Policy"
5. Confirm that the link works and takes the user to a page displaying the "Privacy policy"
6. Confirm that this link works and is attainable regardless of being logged in. 
7. Do this for every page on the site. 
8. Confirm that the direct link works by navigating to [https://flask-ms3-coffee.herokuapp.com/privacy](https://flask-ms3-coffee.herokuapp.com/privacy)


**Expected Result:**  
- In the footer of the site there should be link to a "Privacy policy"
- Clicking this link should take the user to page which outlines the site's "Privacy Policy".
- This link should be accessible regardless of a user being signed in.
- The link should be accessible across all pages in the site.
- The link should be accessibel by going directly to the URL. 


**Actual Result:**
- In the footer of the site there is a link to a "Privacy policy".
- Clicking this link takes the user to page which outlines the site's "Privacy Policy".
- This link is accessible and works regardless of a user being signed in.
- The link is accessible and works across all pages in the site.
- The link is accessible by going directly to the URL. 

**Pass/Fail:**
Pass

**Image of Test Result:**

### Admin User Goals
#### Test Case 14

> As an Admin, I want to enable or disbale other accounts with Admin permission.

**Description**  
Verify that admins have access to an "Admin Panel" page. Confirm that on the admin panel that the following buttons are present and associated to each user in the list:
- Enable Admin
- Disable Admin

Confirm that if an account is "Enabled" as an admin that the "Enabled" button is disbaled. Confirm that the 'Admin" status reads "True" if the admin is enabled. Confirm the opposite of this if the admin is disbaled.

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Login with an account that has Admin permissions enabled.
4. Under the "My account" dropdown in the navbar, navigate to the "Admin Panel" page. 
5. Confirm that every user has an associated "Enable Admin" and "Disable Admin" button. 
6. Confirm that users that are admins state that their 'Admin' statsu is "True".
7. If True, confirm that the "Enable" button is disbaled.
8. Disbale an admin from their Admin permissions. 
9. Confirm that their 'Admin' status reads "False".
10. Confirm that the 'Disbaled' button is disabled and that the "Enable" button is enabled. 
11. Repeat the above steps in the reverse direction. i.e. Enable an admin or vice versa dependant on your starting position. 
12. Confirm that in each update to Enabling or Disabling admin preferences that a toast message si displayed confirming the update. 
13. To truly test, do this with two accounts that you own, one that is Admin enbaled and one that is not. 
    - Set your non admin account as an admin with your admin account and confirm that the admin panel is now available to that account. 
    - Revoke admin priveledges and confirm that the "Admin Panel" is no longer visible or accessible. 

**Expected Result:**
- As an admin, an Admin panel should be visible under the "My account" dropdown in the navbar.
- Clicking this link should take the admin to an Admin page where they can see all users and their current admin permission sets.
- Every user should have an associated "Enable" or "Disable" admin button. 
- Every user should have an "Admin" status that reads as "True" or "False" dependant on their current permissions set. 
- Enabling a user as an admin should disbale the "Enable admin" button and enable the "Disable admin" button. 
- Enabling a user as an admin should change their "Admin" status to True.
- Enabling a user as an admin should give them access to the admin panel page.

**Actual Result:**
- As an admin, an Admin panel is visible under the "My account" dropdown in the navbar.
- Clicking this link takes the admin to an Admin page where they can see all users and their current admin permission sets.
- Every user has an associated "Enable" or "Disable" admin button. 
- Every user should has an "Admin" status that reads as "True" or "False" dependant on their current permissions set. 
- Enabling a user as an admin disbales the "Enable admin" button and enables the "Disable admin" button. 
- Enabling a user as an admin changes their "Admin" status to True.
- Enabling a user as an admin gives them access to the admin panel page.
- The opposite is also true of all of the above. i.e. if a user is already an admin then the "Enable admin" button is disabled etc. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 15

> As an Admin, I want to moderate site content of reviews and comments.

**Description**  
Verify that admins can see and action the following on each review and their respective comments section:
 - Edit Review icon.
 - Delete Reviw icon. 
 - Delete button on all comments. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Login with an account that has Admin permissions enabled.
4. Navigate to the reviews page. 
5. Confirm that all reviews have the Edit and Delete reviews visible and actionable on them regardless of the creator of the review. 
6. Confirm that under the comments section of all reviews that every comment has a "Delete" button. 
7. Confirm that editing a review edits the review. 
8. Confirm that a review can be deleted.
9. Confirm that comments can be deleted. 

As an aside, this is best tested with two accounts, one of which does not have admin permissions enabled on it but that can create reviews and comments that can be modified and deleted by the admin account so as to not unnecessarily modify or delete natural site content by other users. 

**Expected Result:**
- An admin should be able to see the Edit icon and Delete icon of all reviews regardless of the reviews creator. 
- Ad admin should see a "Delete" button on all comments across the site regardless of the comment creator.
- All buttons should be actionable and have the corresponding effect. 

**Actual Result:**
- An admin can see the Edit icon and Delete icon of all reviews regardless of the reviews creator. 
- Ad admin can see a "Delete" button on all comments across the site regardless of the comment creator.
- All buttons are actionable and have the corresponding effect.

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 16

> As an Admin, I want to remove users if necessary.

**Description**  
Verify that admins have access to an "Admin Panel" page. Confirm that on the admin panel that the following buttons are present and associated to each user in the list:
- Delete Account

Confirm that deleting an account removes the users from the site. This will be reflected by the site statistics at the top of the Admin page which specifies how many users are on the site. Confirm that a toast message si received confirming that the user was deleted. Confirm that the user is no longer present in the list.

As an aside, this is best tested with two accounts, one of which can be deleted so as to not unnecessarily impact natural users of the site. 

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Login with an account that has Admin permissions enabled.
4. Under the "My account" dropdown in the navbar, navigate to the "Admin Panel" page. 
5. Confirm that every user has an associated "Delete Account" button.
6. Delete a user.
7. Confirm that a toast message is received to confirm that the account was deleted. 
8. Confirm that the user is no longer present in the list. 
9. Confirm that the sites statistics at the top of the Admin page reflect the change to the number of users across the site.
10. If testing with two accounts, confirm that the deleted account can no longer log in. 

**Expected Result:**
- As an admin, an Admin panel should be visible under the "My account" dropdown in the navbar.
- Clicking this link should take the admin to an Admin page where they can see all users and a corresponding "Delete Account" button.
- Clicking this button should remove the selected user from the list.
- The admin should receive a toast message confirming that the account was deleted. 
- The statistics at the top of the Admin page should reflect the change to the number of users across the site. 
- The deleted account should not be able to log in with their credentials. 

**Actual Result:**
- As an admin, an Admin panel is visible under the "My account" dropdown in the navbar.
- Clicking this link takes the admin to an Admin page where they can see all users and a corresponding "Delete Account" button.
- Clicking this button removes the selected user from the list.
- The admin receives a toast message confirming that the account was deleted. 
- The statistics at the top of the Admin page reflect the change to the number of users across the site. 
- The deleted account can no longer log in with their credentials. 

**Pass/Fail:**
Pass

**Image of Test Result:** 

#### Test Case 17

> As an Admin, I want to see statistics on the number of users and reviews on the site. 

**Description**  
Verify that admins have access to an "Admin Panel" page. Confirm that on the admin panel at the top of the page is a small section called "Statistics". Confirm that under statistics it lists the following:

- Total number of users.
- Total number of reviews.

**Steps**
1. Open your browser of choice.
2. Navigate to [https://flask-ms3-coffee.herokuapp.com/](https://flask-ms3-coffee.herokuapp.com/)
3. Login with an account that has Admin permissions enabled.
4. Under the "My account" dropdown in the navbar, navigate to the "Admin Panel" page. 
5. Confirm that there is a statistics section at the top of the page. 
6. Confirm that the statisitcs lists the number of users and number of reviews across the site. 
7. Test the truthyness of the statistics by adding a review and checking the statistics to see the reflected change.
8. Delete the review and check the statistics again. 
9. Follow Test Case 16 to check the truthyness of the statistics related to number of users. 

**Expected Result:**
- As an admin, an Admin panel should be visible under the "My account" dropdown in the navbar.
- Clicking this link should take the admin to an Admin page where they can see a statistics section at the top of the page. 
- Under the statisctics section it should list the following:    
    - Total number of users.
    - Total number of reviews.
- Statisitcs shown should be accurate.
- Adding/Deleting a review should be reflected in the accuracy of the statistics,
- Deleting a user should be reflected in the accuracy of the statistics.


**Actual Result:**
- As an admin, an Admin panel is visible under the "My account" dropdown in the navbar.
- Clicking this link takes the admin to an Admin page where they can see a statistics section at the top of the page. 
- Under the statisctics section it lists the following:    
    - Total number of users.
    - Total number of reviews.
- Statisitcs shown are accurate.
- Adding/Deleting a review isreflected in the accuracy of the statistics,
- Deleting a user is reflected in the accuracy of the statistics.

**Pass/Fail:**
Pass

**Image of Test Result:**
---
