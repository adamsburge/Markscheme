# Deployment Guide

This project was coded locally on VS Code and is deployed using Heroku. The static files are hosted on AWS using S3. Should you wish to to recreate this app, you could code locally or in your own IDE. Additionally, hosting with Heroku and AWS are only two options out there. 

## Steps for Deployment:
#### Initial Setup
1. If you do not have an account with [Github](https://github.com/), create an account, log in, and then return to this page.
2. At the top of this page, click the button that says 'Fork' and copy this repository to your own account.
3. At this point you will need to decide if you want to code locally (using a locally IDE like [VS Code](https://code.visualstudio.com/)) or use an online IDE (such as [Gitpod](https://www.gitpod.io/)).
   1. If you decide to use an online IDE like [Gitpod](https://www.gitpod.io/), navigate to the IDE's website, create an account and follow all the instructions they provide on how to connect your Gitpod account to your Github account. Once you have done this, you can return to your Github account, navigate to the newly created repository forked from this one, and then click the green button in the top right corner that says 'Gitpod'. Clicking on this will launch your online IDE and get you set up to code.
   2. If you decide to code locally, it's a bit more complicated. 
      1. Firstly, you need to make sure you have [VS Code](https://code.visualstudio.com/) or your preferred IDE installed on your computer. You will then need to clone your Github repository to your computer. If you need help doing this, [this video](https://www.youtube.com/watch?v=icfevBYas9s&ab_channel=LearnToCode) provides a good overview of how to do this.
      2. After cloning the repository to your local device, you can open it in VS Code (or your chosen editor). Before you begin coding, you will need to set up a virtual environment. [This article by VS Code](https://code.visualstudio.com/docs/python/environments) provides a great overview of how to set up the virtual environment. It is important that you do not skip this step since, if you go on to install any package or third-party apps on this project, you could install them onto your local device which could potentially affect how other projects you work on operate.
      3. Once your virtual environment is set up, you should install django by typing the command `python -m pip install Django` in your terminal where the virtual enviroment is running. Any time you install another third-party app, make sure to freeze it to your requirements.txt file with the line `pip freeze > requirements.txt`.
4. Now you can make any changes to the project so that it matches your desired goals. Whenever you wish to push (i.e., save) your project, do so with this series of commands in the terminal:
   1. `git add .`
   2. `git commit -m "Type your message here explaining the changes you've made"`
   3. `git push`

#### Setting up a Database
1. Create a free account with [Elephantsql](https://www.elephantsql.com/), or log in if you already have an account. This is where your databases will be hosted.
2. Obtain a database url. To do this, first click the 'create new instance' button on the home/dashboard page of Elephantsql. Name the database what you like (ideally the same name as the app you're making), select the 'Tiny Turtle' or free plan, select your region and then submit the form. After this, you can obtain the database url by clicking on your new database and lookin under where it says 'URL'. Make sure to copy this database url as it will be needed later.

#### Set Up Stripe
1. Sign into [Stripe](https://dashboard.stripe.com/login), or create an account and then sign in and then go to the home tab.
2. Go to the developers section. Here you will find two values–1. the stripe secret key and 2. the stripe public key. You will need to copy these and have them ready later.
3. In the developer section, click on webhooks and add a new end point. The url for this end point should be https://nameofyourwebsite.com/checkout/wh/. Then select the events this webhook will receive and add the end point.
4. Run tests to make sure your webhook is working. As stripe is always updating their system, it is best to read their current documentation if you get confused.


#### Set Up Heroku
1. Sign into [Heroku](https://www.heroku.com/home), or create an account and then sign in.
2. Create a new app by clicking on the box in the top right corner that says 'New' and then selecting 'Create New App'. Fill out the information required by giving the app a name and selecting your preferred region.

3. Create a unique secret key and put that into the env.py file




#### Set up Amazon S3
3. Set up account with Amazon S3:
   1. Create bucket
   2. Give bucket permissions 
4.  Make migrations
5.  Link the Heroku app to the repository
6.  Push to Heroku