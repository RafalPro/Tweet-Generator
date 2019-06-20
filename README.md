Packages Used:
-	Django (third party package; For front-end/user interaction page)
-	Twitter (thrid party package; API for the accessing of past user tweets) 
-   Markovify  (third party package; For the genreation of the predicative model)
-   DateTime (first party package; For accessing current time to put at bottom of mock tweet)
-   Re (first party package; String package to help get rid of urls in the generated tweets)

Installation Instructions:
-   Use localhost:8000
-   See requirements.txt
-   How To Run:
    - python manage.py runserver in the terminal (cd into proper folder)

Code Structure:
-   Separated urls, rendering html methods, and text generation (NLP) into different files
-   All in django
-   Models.py:
    -   Made a TwitterUser class where objects contain a username and a string representing of all the tweets which were extracted from that user. This was done so that if a user has already been searched before, the runtime will be much smaller. This is because the getting of the tweets for that user does not have to happen with each call.
    -   Using markovify, the tweets of a particular twitter user are used to train the model which then generated a new sentence (tweet) based on the training set
    -   Accessed tweets through twitter's api, using given verification keys
-   How it all connects:
    -   In urls.py, we define three routes: /, /tweet, /exception. These correspond to the home page, page that generates the tweet, and an error page respectively. These call methods in views.py
    -   In views.py, we handle the requests, either by rendering the html pages or by handling post requests by calling a method in models.py to generate a tweet which will then circle back to views.py to display the tweet.
    -   In models.py, the method generate_tweet takes in a string representing the requested user and gives back a string that the model generated. If this method throws and error, it is caught in views.py