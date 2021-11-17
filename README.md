# Z Dentist
Z Dentist is a dentist practice for everyone.

This website can not be used as a template for a business since it's a project for educational purposes.

Live website: [Z Dentist](https://z-dentist.herokuapp.com/)

![Skärmavbild 2021-11-15 kl  14 55 41](https://user-images.githubusercontent.com/85236391/141793921-c9a1c459-6645-41a3-9e9e-669098aa83ae.png)

## Table of Contents

* [UX (User Experience)](#ux-user-experience)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
* [Design](#design)
  * [Fonts](#fonts)
  * [Colors](#colors)
  * [Wireframe](#wireframe)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks and Tools](#frameworks-and-tools)
  * [Contrast Checker](#contrast-checker)
* [Features](#features)
* [Testing](#testing)
  * [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [Python](#python)
  * [Different Screen Size](#different-screen-size)
* [Issues found during site development](#issues-found-during-site-development)
* [Deployment](#deployment)
  * [Cloning](#cloning)
* [Credits](#credits)

## UX (User Experience)

### User Stories
* As a user
  * I want to know where the dentist practice is located
  * I want to see what kind of service the dentist practice offer.
  * I want to be able to book an appointment
  * I want to be able to cancel an appointment
  * I want to know a bit more about the company
  * I want to be able to contact the company with random question
  * I want to get a confirmation email with my appointment time

### Site Owner Goals
* As a site owner
  * I want to make it easy for customer to make an appointment
  * I want to be able to confirm appointments
  * I want to be able to cancel appointments
  * I want to be able to change a appointment date
  * I want to have a clear overview of the customers details
  * I want to let people see the services we offer with prices
  * I want to be able to get email from customers trough a contact form
  * I want to get a email when someone makes a new booking
  * I want to show where the dentist office is located

* I planned the project [here](https://github.com/andrezeitz/z_dentist/projects/2)
## Design

### Fonts
I have chosen Lato for the header and logo as it is easy to read and has sufficient contrast to the main body font. The small caps style is used by Roboto that I feel look very clean in the quiz.

### Colors
The site features complementary Blue Crayola Forest Green Web, Pacific Blue, white and black to create a good contrast and improve readability.

The colors chosen are:

<img width="827" alt="coloruus" src="https://user-images.githubusercontent.com/85236391/138835210-20530ccc-21f9-4577-b707-32b788908f36.png">

### Wireframe

#### Desktop
![WEB](https://user-images.githubusercontent.com/85236391/138857007-9be5dc7e-8d19-484e-9e75-9ae931427271.png)

#### Mobile
![MOBILE](https://user-images.githubusercontent.com/85236391/138857025-d1437a26-1820-4f8d-8343-c2e2031f0e5e.png)

## Technologies

### Languages
* HTML
* CSS
* Python

### Frameworks and Tools
* GitHub
* Gitpod
* Django
* Heroku
* Postgres
* Google Fonts
* [Font Awesome](https://fontawesome.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [Am I responsive](http://ami.responsivedesign.is/)
* [WebAim](https://webaim.org/resources/contrastchecker/)

### Contrast Checker
All colors was checked in a contrast checker and pass the test.

<img width="733" alt="contrast" src="https://user-images.githubusercontent.com/85236391/138835792-aaeb12b5-5531-432a-bf4a-f22061d0ea8f.png">

## Features
The website has the following features:
### Navigation bar
Navigation bar is visible on the top of the website with a logo that is clickable to update the site. When someone is logged in the navigation bar will change so the user can see there username and a logout button om the right top side. The registration and login links will also disappear once logged in. The navigation links will collapse on smaller screens.

### Home
The home page contains a big hero picture with a "Book an Appointment" button on it.
It also have information about the company like how the work and how focus on quality is very important.

### Services
The service page contains a table with all the treatments the company is doing and price information about each service.

### Contact us
The contact page has a large google maps window to show the customer where the dentist company is located. After that it's a contact box with the address, phone number and email of the company. Last there is a contact form where the customer can enter there name, email and a message to be able to contact the company with any questions. After the message is sent it will show a success message so the customer know we have received the email.

### Appointment
On the appointment page the customer will be able to make a booking within the form. Here the user have two choices. Either they can be logged in to the site and will then be able to manage there booking after. If they dont want to register it works fine to make an appointment as well. They will then put in the required  information, then they can choose from a list what kind of treatment they would like to book with price information. After that they can choose a desired date for there appointment. Finally there is a field that is not required, but they can enter any additional information they would like. As soon as they make the reservation there will be a success message telling them the appointment have been sent to the dentist.

### Manage
This page is only visible if you are logged in as a user or admin.

#### User
If you are logged in as a user and make an appointment your bookings will be showed here. First it will just show your information and a message that the booking is still not confirmed. Once the admin confirm the appointment the card will change and instead show the confirmed date with time and also a delete button to let the customer cancel there appointment up to 24 hours prior to the appointment. If the booking is deleted an email will be sent out to both the customer and Admin confirming the appointment is canceled. The booking will then disappear from the manage site.

#### Admin
If you are logged in as a Admin, this page will show you all the bookings that have been made and information on all customers. In the navigation bar it will show a notice clock and a number for how many bookings that haven't been accepted yet. The admin can then see the desired date the customer would like for there appointment and confirm it with date and time. Once the admin press the "Accept" button an email will be sent to the customer confirming the appointment with date and time. The user card will then show a button where the admin can change the already approved date. When clicked a collapsible div will open up with the date time input and a button saying "Accept New Appointment". After the date is changed a new email will be sent to both the user and the admin. Last the admin will have a delete button to be able to delete a booking. If the booking is deleted an email will be sent out to both the customer and Admin confirming the appointment is canceled. The booking will then be deleted from the database.

### Registration
This link is visible in the top right corner of the navigation bar if there is no user logged in to the page. If user is already logged in it will be hidden.

### Login/Logout
Login and logout link is placed in the top right corner and will change if the user is logged in or not.

### Footer
The footer contains the opening hours and contact information about the company.

## Testing

1. As a user, I want to easily determine what kind of website it is.
* Result: TEST PASSED

2. As a user, I want to see what services and prices the dental clinic offers.
* Result: TEST PASSED

3. As a user, I want to be able to book an dentist appointment.
* Result: TEST PASSED

4. As a user, I want to know where the dental clinic is located.
* Result: TEST PASSED

5. As a user, I want to know the phone number to the dental clinic.
* Result: TEST PASSED

6. As a user, I want to get a email with my confirmed appointment time.
* Result: TEST PASSED

7. As a user, I want to be able to manage my bookings.
* Result: TEST PASSED

8. As a user, I want see when my booking is confirmed on the manage page.
* Result: TEST PASSED

9. As a user, I want to get an email to show me my contact email was receive and what my messages was.
* Result: TEST PASSED

10. As a site admin, I want to be able to manage appointment
* Result: TEST PASSED

11. As a site admin, I want to be able to confirm appointment times and send out confirmation email to the customer.
* Result: TEST PASSED

12. As a site admin, I want to be able to delete appointments and send out confirmation email to the customer about the cancellation
* Result: TEST PASSED

13. As a site admin, I want to be able to receive email when new bookings is being made.
* Result: TEST PASSED

14. As a site admin, I want to be able to receive email when someone is contacting us from the contact page.
* Result: TEST PASSED

15. As a site admin, I want to be able to change the appointment time without to cancel the booking.
* Result: TEST PASSED

16. As a site admin, I want to see how many bookings still havent been accepted with a date yet.
* Result: TEST PASSED 

### Code Validation

### HTML
The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.

##### Home Page
![Skärmavbild 2021-11-16 kl  14 09 47](https://user-images.githubusercontent.com/85236391/141992257-0c38442a-1ec8-44e3-b0eb-00c152d26c7d.png)

##### Service Page
![Skärmavbild 2021-11-16 kl  14 14 57](https://user-images.githubusercontent.com/85236391/141992290-91f67f70-0adb-4a93-8cee-0b7e64e3d0ce.png)

##### Contact-Us Page
![Skärmavbild 2021-11-16 kl  14 15 21](https://user-images.githubusercontent.com/85236391/141992304-15b31d71-6b80-48d3-ab2b-0e16efb26219.png)

##### Appointment Page
![Skärmavbild 2021-11-16 kl  14 15 48](https://user-images.githubusercontent.com/85236391/141992314-df39f742-7d3a-4c57-b3e9-26b29b0593ce.png)

##### Manage-Appointment Page
![Skärmavbild 2021-11-16 kl  14 16 06](https://user-images.githubusercontent.com/85236391/141992323-5925d6a7-867b-4607-b495-2e3c42945c2b.png)

### CSS
The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.
![Skärmavbild 2021-11-16 kl  13 33 34](https://user-images.githubusercontent.com/85236391/141992519-c7f7b21d-b992-4ada-afdd-9b31dbd687d6.png)

### Python
The PEP8 Online Check was used to validate the Python code in both .views files. No errors or warnings to show

![Skärmavbild 2021-11-16 kl  13 29 57](https://user-images.githubusercontent.com/85236391/141985864-00a3c2e9-69a1-4ca6-9eaf-521b60beb425.png)

![Skärmavbild 2021-11-16 kl  13 30 37](https://user-images.githubusercontent.com/85236391/141985872-8760bd91-9828-4257-84fa-843cf3b33921.png)


### Different Screen Size
The site is optimized for all screen sizes and tested with a Macbook Pro 13" and iPhone 13 Pro.
I use media queries to make everything look and feel good on mobile devices.

### Issues found during site development
1. There was an issue to send confirmation emails out to the user and Admin. I use <code>send_mail</code> from Django and added subject and body straight in to it. In the body I added the first name of the user and also the confirmation date and I kept getting error message that it could not read the first name or the confirmation date. I then change it to defined both the subject and body before the <code>send_mail</code> and then just let the <code>send_mail</code> read from the variables. It made the errors go away.

![Skärmavbild 2021-11-09 kl  12 40 18](https://user-images.githubusercontent.com/85236391/140917835-994ea11c-79dd-4959-a85c-477b5d45a03e.png)

2. I had this problem when I tested to send email when the site was deployed to the Heroku platform it gave me an error that was not showed in Gitpod. The issue was that I forgot to add the Secret API key from Send Grid in to the config on Heroku. After adding the key to the config vars the problem went away.

<img width="660" alt="Skärmavbild 2021-10-28 kl  10 28 39" src="https://user-images.githubusercontent.com/85236391/140926748-d576da00-ff7d-48e9-89d1-41eb1fd59ee6.png">

3. When a user was going to make a second appointment they get a error message saying "IntegrityError". The reason was I had a onetoone relationship with the user and the appointment. So I changed the User model to a ForeignKey instead and get rid of the error right away.

###### New:
![Skärmavbild 2021-11-09 kl  13 04 34](https://user-images.githubusercontent.com/85236391/140921303-082c13bb-1c07-4036-954d-2f8afb6b417f.png)
###### Old:
![Skärmavbild 2021-11-09 kl  13 05 25](https://user-images.githubusercontent.com/85236391/140921310-1ae4f280-244c-45b4-abe7-c5d34dba752e.png)

After the change I got another problem that users that did not login would get an error saying this:

<img width="1323" alt="Skärmavbild 2021-11-17 kl  15 22 09" src="https://user-images.githubusercontent.com/85236391/142243977-99350f84-f678-468f-a817-b8e8f4c3733f.png">

I fixed the error by using if/else statments in the function that was calling the form. If the user is not logged in the <code>user=request.user</code> will not be used.

<img width="350" alt="Skärmavbild 2021-11-17 kl  17 41 56" src="https://user-images.githubusercontent.com/85236391/142244147-21c66cc4-81ad-4a2d-84cb-6cbb2c5ea678.png">

4. The datetime was not rendering correct from the model so I split it up to make it look better.
##### Old:
![Skärmavbild 2021-11-04 kl  12 41 42](https://user-images.githubusercontent.com/85236391/140941868-edf7654f-6e8b-4be8-a49e-9220ec22c639.png)
##### New:
![Skärmavbild 2021-11-09 kl  15 18 21](https://user-images.githubusercontent.com/85236391/140941883-56fa2e61-2c1b-42ef-b88f-f4e1802c0df2.png)
##### Solution:
![Skärmavbild 2021-11-09 kl  15 26 30](https://user-images.githubusercontent.com/85236391/140941993-09fefea0-177f-4048-b0ac-3226fb42b143.png)

5. My success messages was bugging when people was logging in and out. It was showing inside the "Manage" page even when that was only for the confirmation of appointments. I fixed it to delete the automatic messages Allauth send out when it's a successful login/out to any page since I was not using it.

![Skärmavbild 2021-11-08 kl  12 53 44](https://user-images.githubusercontent.com/85236391/140918482-a06366fe-84e6-48b4-872d-d80e00bb99a2.png)

6. I was getting some error message when trying to add a edit button to the manage appointment form. Once the edit button was clicked it would work as a submit button for the datetime form and say that the date is not set. To work around it I added a collapse div from bootstrap and then added the <code>{app.id}</code> on the div so each card would know which edit button was clicked.

![Skärmavbild 2021-11-12 kl  14 33 34](https://user-images.githubusercontent.com/85236391/141792406-f4c717a8-2917-4182-81f5-0cbf3e184b22.png)

##### Solution:
![Skärmavbild 2021-11-15 kl  14 46 42](https://user-images.githubusercontent.com/85236391/141792545-009587b1-dada-4c10-a101-ea41984c91fd.png)


## Deployment
1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser

The program is set to be deployed automatically after each push from gitpod.

### Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

## Credits
* I learned how to make drop down menus in Models from this page [Stackoverflow](https://stackoverflow.com/questions/31130706/dropdown-in-django-model)
* I use code from this card widget [Bootdey](https://www.bootdey.com/snippets/view/events-card-widget)
* I learned how to send emails with Django from this website [Blog](https://sandeepsajan0.medium.com/send-email-in-django-app-with-sendgrid-a009bf19a389)
* I use Django docs to understand more about classed based views [Django Docs](https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/)
* I use Django docs to understand more about sending emails [Django Docs](https://docs.djangoproject.com/en/3.2/topics/email/)
* I use Django docs to understand more about how pagination works [Django Docs](https://docs.djangoproject.com/en/3.2/topics/pagination/)
* I use Django docs to understand more about how to protect a page to only authentic users [Django Docs](https://docs.djangoproject.com/en/3.2/topics/auth/default/)
* I use this bootstrap code to be able to collapse divs [Bootstrap](https://getbootstrap.com/docs/5.0/components/collapse/)
* I learned how to make colums in the admin panel with [Dev2ga] https://www.dev2qa.com/how-to-show-custom-model-columns-using-django-admin/
