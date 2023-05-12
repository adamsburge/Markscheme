# Welcome to Markscheme

Markscheme is an online ecommerce store that allows teachers and tutors to advertise and sell educational products to children and teenages who are preparing for exams. 


# Project Planning 

## Wireframes
I used [balsamiq wireframes](https://balsamiq.com/) to design the UX and UI of the site. 

### Home Page

![Home Page Wireframe](static/images/Home%20Page.png)

### About Us

![Post Page Wireframe](static/images/Archaeological%20Site%20Page.png)

### Staff Page

![About Page Wireframe](static/images/About.png)

**Note**: This page is not yet completed and could be a future development of the site.

### Register

![Register Page Wireframe](static/images/Register.png)

### Sign in

![Log in Page Wireframe](static/images/Log%20in.png)

### User Stories
To access and read the user stories for this project, see my Github project [Markscheme User Stories](https://github.com/users/adamsburge/projects/4/views/1). Many of these user stories were taken from the Code Institute 'Boutique Ado' walkthrough project. However, some are unique to this project.

![User Stories](static/images/user_stories.png)


### Databse Structures
The database models used for this project were expanded from the models used in Code Institute's 'Boutique Ado' walkthrough project. However, these have been adjusted and added to for the purpose of the current project. Notably, this project uses polymorphism to allow for inherited models which extend the use of the product model thereby allowing for more than one kind of product (i.e., Workshops and Digital Products). Additionally, this project expands the user model beyond that created Code Institute's in the Boutique Ado project.

![Database Models](static/images/Database%20Models.png)

# Features

## General Features

### Sign up, Sign in, Sign Out
Any site visitor can register for an account. Once they have done so, they can sign in and out.

![Signup](static/images/signup.png)

![Mobile Sign up](static/images/mobile_sign_up.png)

![Signin](static/images/sign_in.png)

![Mobile Signin](static/images/mobile_sign_in.png)

![Sign out](static/images/sign_out.png)

![Mobile signout](static/images/sign_out_mobile.png)

## Features for Site Visitors and Normal Users

### Browse the Website, Purchase Products
All site visitors can access the home, about, staff pages as well as the checkout process. Site visitors have the option to registor for an account when checkout out and consequently keep track of their purchases.

![Normal Home Page](static/images/non-admin_user_home.png)

## Features Users with Profiles


### Update Billing Details and Purchase History
Users who have signed up for an account have access to their account and can update their billing details and see their previous orders. Additionally, in their order history, they will find all the information they need for attending workshops (i.e., location, date, time, teachers) as well as the download links for any purchased digital files.

![Comments](static/images/comments.png)


![Likes](static/images/likes.png)

![Mobile likes](static/images/mobile_post_contents.png)

## Features for Admin Only

### Add, Update and Delete Posts
The home page for site admins allows them to add, update and delete posts.
![Admin Dashboard](static/images/admin_dashboard.png)

![Add post](static/images/add-post.png)

![Update post](static/images/update_post.png)

# Technologies

### Languages
- HTML
- CSS
- Python
- Javascript
- Postgresql

### Libraries, Frameworks, Programmes & Tools
- Github - Version control and storing code 
- Gitpod - Coding platform
- Django - Primary coding framework
- Psycopg2 - Databse adapter between Postgreql and Python
- Cloudinary - Media storage
- Herokuapp - Web app deployment
- Allauth - Building user registration 
- Gunicorn - Python Web Server Gateway Interface HTTP server
- Django-Summernote - Allow forms to have customisable input
- Django-Crispy-Forms - Build comment forms
- Bootstrap - General Styling
- FontAwesome - Icons for webapp
- Google Fonts - Fonts


# Testing
To read about the manual testing employed in this project, read the [TESTING.md file](TESTING.md).

# Deployment
This project is deployed using Heroku.

Steps for Deployment:
1. Fork or Clone this Depository
2. Create new Heroku app
3. Install django, cloudinary, gunicorn, psycopg2, django-summernote, django-crispy-forms and django-allauth
4. Create a Cloudinary account, get your secret url and put it into the env.py file
5. Create a free account with Elephantsql, obtain a database url and put it into the env.py file
6. Create a unique secret key and put that into the env.py file 
7. Make migrations
8. Link the Heroku app to the repository
9. Click Deploy


# Credits
- Deployment aesthetic:
    - The color theme came from Adobe Color.
    - The layout of the Post-Detail view was inspired by Wikipedia's recent interface update.
- Concept:
    - The concept of this app is my own.
- Content:
    - The content (both text and images) of the current blog posts on the site are taken, usually word for word, from the Wikipedia pages associated with the archaeological sites.
- Code: 
    - Much of the code for this project was based on the Code Institue walkthrough project 'I think therefore I blog'. Much of this project has been changed, but that project provided an outline for this one.
    - I spent several hours watching videos by John Elder on his channel [Codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy), particularly his Django Wednesdays playlist. It would be impossible to list every line of my code that was influenced by his videos, though his most significant influence was in helping solidify my understanding of the Django framework as a whole.
    - Various forums such as Stack Exchange and Stack Overflow helped to solve small problems when I was stuck on a line of code.
- Individuals:
    - My Mentor, [Adegbenga Adeye](https://github.com/deye9), provided comments and feedback.
    - My wife, Megan, provided wonderful feedback, and, most importantly, saw me through the project by making every break a delight.
