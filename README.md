# Project 3

### Restaurant Reviewer App
#### Description and background of the app
* The Restaurant Reviewer App is a restaurant-focused promotion service which publishes restaurant profiles and crowd-sourced reviews.
* It lets users create their own restaurant, and share them to other users for promotion
* Users can also leave reviews on restaurants and add restaurant to their favorites.

### Screenshots
#### Screenshot #1 - Landing page before login
![Screenshot #1](https://i.imgur.com/SDe9aXg.png)

#### Screenshot #2 - Landing page after login
![Screenshot #2](https://i.imgur.com/qQ48cZi.png)

#### Screenshot #3 - View all published restaurants
![Screenshot #3](https://i.imgur.com/Cqy1Zgk.png)

#### Screenshot #4 - View a particular restaurant
![Screenshot #4](https://i.imgur.com/Z3PJMVI.png)

### Technologies Used
* Web languages
    * HTML
    * CSS
    * Python
* CSS framework
    * Bootstrap
* Server environment
    * Django
* Additional Django module installed
    * django-environ
* Authorization and authentication
    * Django built-in authentication (django.contrib.auth)
* Database
    * PostgreSQL (aka Postgres)

### Getting Started
#### Click on the following link to access the Restaurant Reviewer app
* [Trello board - project planning](https://trello.com/b/7OsKredW/team-django-fett)
* [Lucid chart - ERD](https://lucid.app/lucidchart/7362fe65-f761-4e9d-bfdc-737be7df7490/edit?invitationId=inv_7c563073-7549-4e2a-9613-91895e128912&referringApp=slack&page=0_0#)
* [Wireframes](https://imgur.com/QXSRgvE)
* [Project 3 - Site](#)

### Next Steps
#### The following functionality can be added 
* Profile
    * Add profile model (one-to-one relationship to user model) to allow users to input more profile details, such as user level (restaurant owners, premium users, regular users)
* Restaurant
    * Add map feature for location
    * Allow restaurant owners to upload more pictures of their store and foods
* Menu
    * Add menu model (one-to-one relationship to restaurant model) to improve menu item manipulation and user interface
* Hours
    * Add hours model (one-to-one relationship to restaurant model) to improve user interface
* Review
    * Allow users to edit their reviews
    * Allow users to add images in their reviews
* Favorite
    * Allow users to share their favorites
* User interface
    * Allow users to view all reviews in one page
* Other features
    * Allow users to change theme of the app
    * Add messaging function between users (e.g. between restaurants and customers)
    * Add ordering features to allow users to order directly from restaurants
    * Add delivery service features to allow restaurant owners to choose their desire delivery service
    * Consume third-party APIs for populating restaurants information to database
    * Consume API for Imgur
    * Upload images/assets to AWS S3






