This project is deployed using Heroku and AWS S3

Steps for Deployment:
1. Fork or Clone this Depository
2. Create new Heroku app
3. Install django
4. Create a free account with Elephantsql, obtain a database url and put it into the env.py file
5. Create a unique secret key and put that into the env.py file
6. Set up account with Amazon S3:
   1. Create bucket
   2. Give bucket permissions 
7. Make migrations
8. Link the Heroku app to the repository
9. Push to Heroku