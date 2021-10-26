# Z Dentist
Z Dentist is a dentist practice for everyone.

This website can not be used as a template for a business since it's a project for educational purposes.

Live website: [Z Dentist](https://z-dentist.herokuapp.com/)


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
  * [Java Script](#java-script)
  * [Different Screen Size](#different-screen-size)
* [Issues found during site development](#issues-found-during-site-development)
* [Deployment](#deployment)
  * [GitHub Pages](#github-pages)
  * [Cloning the project locally](#cloning-the-project-locally)
  * [Forking the repository](#forking-the-repository)
* [Credits](#credits)

## UX (User Experience)

### User Stories
* As a user
  * I want to know where the dentist practice is located
  * I want to see what kind of service the dentist practice offer.
  * I want to be able to book an appointment
  * I want to know a bit more about the company
  * I want to be able to contact the company with random question
  * I want to get a confirmation email with my appointment time

### Site Owner Goals
* As a site owner
  * I want to make it easy for customer to make an appointment
  * I want to be able to confirm appointments
  * I want to have a clear overview of the customers details
  * I want to let people see the services we offer with price
  * I want to be able to get email from customers trough a contact form
  * I want to show where the dentist office is located

## Design

### Fonts
I have chosen Lato for the header and logo as it is easy to read and has sufficient contrast to the main body font. The small caps style is used by Roboto that I feel look very clean in the quiz.

### Colors
The site features complementary Blue Crayola Forest Green Web, Pacific Blue, white and black to create a good contrast and improve readability.

The colors chosen are:

<img width="827" alt="coloruus" src="https://user-images.githubusercontent.com/85236391/138835210-20530ccc-21f9-4577-b707-32b788908f36.png">

### WireframE

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
Navigation bar is visible on the top of the website with a logo that is clickable to update the site. The navigation links will collapse on smaller screens.

### Home
The home page contains a big hero picture with a "Book an Appointment" button on it.
It also have information about the company like how the work and how focus on quality is very important.

### Services
The service page contains a table with all the threatments the company is doing and price information about each service.

### Contact us
The contact page is having a large google maps window to show the customer where the dentist company is located. After that its a contact box with the adress, phone number and email of the company. Last there is a contact form where the customer can enter there name, email and a message to be able to contact the company with any questions. After the message is send it will show a success message so the customer know we have recived the email.

### Appointment
On the appointment page the customer will be able to make a booking within the form. They will put it there information then they can choose from a list what kind of threatment they would like to book with price information. After that they can choose a desired date for there appointment. Finally there is a field that is not required but they can enter any additional information they would like. As soon as they make the reservation there will be a success message telling them the appointment have been send to the dentist.

### Manage Appointment(Admin)
This page is only visable if you are logged in as a admin. It will show all the bookings that have been made and information on each customer. The admin can then see the disired date the customer would like for there appointment and confirm it with date and time. Once the admin press the "Accept" button an email will be send to the customer confirming the appointment with date and time. On the manage page the booking will then show up as "Appointment accepted" with the date and time and a big "Confirmed" button will show up instead.

### Footer
The footer contains the opening hours and contact information about the company.

## Testing

1. As a user, I want to easily determine what kind of website it is.
* Result: TEST PASSED


### Code Validation
### HTML
The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.


### CSS
The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.

### Python

### Different Screen Size

### Issues found during site development
Problem to import from Database
Problem with email
Problem with server to be able to send emails, had to verify your account
Problem with define the email 

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
https://stackoverflow.com/questions/31130706/dropdown-in-django-model
https://www.bootdey.com/snippets/view/events-card-widget
https://sandeepsajan0.medium.com/send-email-in-django-app-with-sendgrid-a009bf19a389
https://docs.djangoproject.com/en/3.2/topics/pagination/


