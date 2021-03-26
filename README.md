# Code Institute Module 11 Full Stack Frameworks Milestone Project

## Fitness That Fits 

Fitness That Fits is a web site for people looking to adopt a healthier lifestyle. The
idea behind the site is to help users make small but permanent changes which they can fit into 
their schedules rather than quick fixes which might lead to temporary changes but 
which will be abandoned later. The typical user is assumed to be an individual 
in average physical condition.

### Project Aims

Fitness That Fits is the fourth milestone project for Code Institute's Full Stack Frameworks
module. The goal of the project is to incorporate an authentication process, purchasing capability,
exercise plans, and user profiles. The site is designed to address the following user stories:

    - As a user, I would like to be able to look for fitness gear I can use at home.
    - As a user, I would like to be able to purchase fitness gear.
    - As a user, I would like to be able to select the quantity of the items I am purchasing.
    - As a user, I would like to be able to search for products, workout plans, and habits on the site.
    - As a user, I would like to be able to find different exercise plans.
    - As a user, I would like to be able to make healthy changes in my life that I will stick with.
    - As a user, I would like to be able to search for items on the site.
    - As an administrative user on the site I would like to be able to add, delete, and edit products
    on the site as well as habits and workout plans.
    - As an administrative user on the site I would like to be able to change images.
    - As a user, I would like to be able to register on the site
    - As a user, I would like to be able to review my order history.
    - As a user, I would like to be able to place an order with or without creating a profile.
    - As a user, I would like to receive an email confirmation if I place an order.
    - As a user, I would like to receive an email confirmation if I register on the site.
    - As a user, I would like to be able to add items to my shopping bag.
    - As a user, I would like to be able to read more about the details of specific products, 
    exercise plans, and healthy habits.
   
   ### Features 

   The site has the following features:

   1) A homepage which allows users to see an overview of the site
   2) Links to social media sites
   3) A page listing all of the products for sale
   4) Individual pages for seeing the details of the specific products and
   purchasing them.
   5) A page listing all of the exercise plans
   6) Individual pages for each of the exercise plans
   7) A page with an overview of healthy habits
   8) Individual pages with more information about healthy habits
   9) A page for the user profile
   10) A page to update products, habits and workout plans on the site
   11) A page for adding new products to the site
   12) A search function for both names and descriptions

### Features to be implemented later

Future improvements to the site would include adding a forum for users to communicate with other users, 
adding a way for users to enter their individual goals on the site and track their progress, 
adding a way for users to enter ratings of exercise plans and products, and adding the capability to
add, update, and delete exercise plans for administrative users. For the exercise plans videos or images
would also be added to demonstrate the exercises. Also, the appearance of the site would be improved 
with more consistent photographs and other visual improvements and auto-fill would be added to the search. 

### Technologies Used

- [Django](https://www.djangoproject.com/) 
The project uses the Django framework to provide the major capabilities such as dictionaries, 
views, search, email, and authentication.

- [Stripe](https://stripe.com/en-gb-se)
Stripe was used for the payment functionality.

- [Python](https://www.python.org/)
Python was used for the backend functionality with Django.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
Javascript was used for functionalities such as changing the quantity of items, toast pop-ups, and Stripe.

- [JQuery](https://jquery.com/)
JQuery was used for interactivity on the site.

- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
Bootstrap was the framework used.

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
HTML was used for the structure of the web pages.

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
CSS was used for styling the web pages.

- [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=EAIaIQobChMIkdW79aL57QIVUBV7Ch3UKQM2EAAYASAAEgJ8BPD_BwE)
Heroku was used to deploy the web site.

- [Whitenoise](http://whitenoise.evans.io/en/stable/)
Whitenoise was used (instead of AWS) for the static files.

- [Github](github.com)
Github was used for version control.

- [Gitpod](gitpod.io)
Gitpod was used for the development environment.

- [Balsamiq](balsamiq.com)
The wireframe was created on Balsamiq.

### Code

Most of the code came from the boutique ado project. Code to make the hyperlinks black was found on W3 schools and code for the 
search function was from the boutique ado project, Stack Overflow (https://stackoverflow.com/questions/55468722/django-chain-list-objects-filter), 
and Coding for Entrepreneurs (https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine).


### Testing
The site was tested on a laptop and mobile phone and the links were checked and the purchasing functionality was tested. 
The site was also viewed in the following browsers:
  - Google Chrome
  - Safari
  - Microsoft Edge

In addition, the checkout and registration functions were tested with invalid information (too many characters or the wrong type
of data, such as numbers instead of characters or vice versa). The email function was also tested for both registering and placing
an order. The ability to add, delete, and edit products was also tested on the site.
 
### Deployment
The site was deployed on Heroku with a pipeline created to the Git repository so that commits to Git are automatically added 
to Heroku. Whitenoise was used for the static files.

### Media and Content
The photos are from Pixabay [link to Pixabay](https://pixabay.com/) and Shutterstock [link to Shutterstock](https://shutterstock.com/):

https://www.shutterstock.com/image-photo/smiling-group-diverse-friends-standing-gym-788222044



### Acknowledgements
Thank you to the tutors and my mentor Aaron for all their help and patience and sorry I was so slow.
The inspiration was from various articles on behavioral research in weight loss and the structure and
the majority of the source code came from the Boutique Ado project.






