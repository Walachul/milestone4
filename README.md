[![Build Status](https://travis-ci.org/Walachul/milestone4.svg?branch=master)](https://travis-ci.org/Walachul/milestone4)

# **Romanian Alpine Club**
## Full Stack Milestone project 4 for Code Institute

The idea/necessity for the project came alive when asked to construct from scratch the website of the Romanian Alpine Club and adding functionalities which now don't exist or need an upgrade.

Old live site here:  [ClubulAlpinRoman](https://www.clubulalpinroman.net/)

New site living here: [RomanianAlpineClub](heroku)

# **User Experience**

The app/website is build first and foremost for the actual members of the Romanian Alpine Club, who needed an upgrade to a platform, where they can login, interact, share information about hikes and other clibbing events and workshops, and also an admin(s) panel where they can check activity of the members.


One of the most important requirements that was asked for a new site was that to be mobile friendly, organized and to be accessible for anyone on every device they would use, so that was my main goal when started building it.

The app had to be user friendly and colorful, and the information needed to be displayed in eye-friendly mode.

# **User Stories**

In general, a user who is not registered will visit the site if he is interested in finding information regarding hiking, climbing and other mountain/outdoor activies and events, but also to find information regarding the history and pioneers of climbing in Romania.

##### Professional/Semi-Professional User

This type of user will generally want to find more information than what is displayed in the public section and more often he will want to become a member if he is not already one and get involved in the Club's activities and also do volunteering.

He will be able to register and access to the blog and merchandise section(for now). 

In the blog app, he will be able to add, edit and delete information with other users.

In the merchandise app, he will be able to purchase custom made merchandise with the Romanian Alpine Club logo, using Stripe payment functionality.

In the account app, he will be able update his profile information (name, address, profile picture) in order to get in future membership card automatically in his profile.

##### Amateur User

They share a passion for mountains, but they are not that hardcore.

More often, they will want to search for information which interests them and will want to register and from time to time get involved in activies and hikes.

They can also buy merchandise and update their profile information.

##### Administrator

Another important requirement was that of the future website/app to have an administrator(or more), that can verify members information, what is the content they are posting about and to be able to monitor that activity.

Also, the administrator should be able to add other admins as well, and to check information of the members that are buying merchandise.

This functionality is possible with Django admin panel, in which I registered the required models from different apps.

# **Features**

##### **Implemented features**

##### *Users(accounts) app*

* Registration - Allows users to register to the site by filling the registration form.(Username, email, full name, password, birth date, home address, phone number) 

  - Registration form - When submitting the form, the users will be prompted if the username is taken and to choose another one and if the passwords match. Also, they will be notified when they didn't fill a  field. When successful, a flash message will prompt the user that registration was successful and they can login.
* Login - Allows users to login to the site and have access to the other apps created(account, blog,  merchandise, search), by going to the login page and fill the form with their username and password. The form created will notify the user if their credentials mismatch or forgot to fill a field and also prompt with successful message if the login was correct and redirect the user to the home page of the app or to the blog app(if he tried to access it without being logged in).

* Password reset - If the user forgets his password, he can access the *Forgot password* function offered by Django. This will redirect him to a form which will require his email. If the registered user that requires password change had entered a valid email address, he will get on that email address a link from the app that will redirect him to a form to change his password.



###### **Below functionalities require the user to be logged in**

* Logout - Allows users to logout from the website. They are redirected to the logout template. If they had any cart items stored in session, they will lose it.

* Account page - Users can see their information that they had entered in the registration form.

* Edit profile - Users can edit their personal information entered in the registration form(personal info and update their profile picture)

* Resizable profile picture - The user's profile picture is resized in the background with python function and uploaded to Amazon's S3

##### *Blog app*
* Blog - The user can view and read all blog posts from other users, by navigating to the blog section in the navigation bar.
       

* View all posts from a specific user -  Users are able to view all posts from a specific user by clicking on the user's name.

* Add blog post - The user is able to add a blog post by navigating to the section Blog > New blog post.

* Edit blog post - Only the user that created a blog post can edit it, by navigating to his specific post, accessing Read more. Then he will be redirected to the section of that post, where the Update functionality is available.

* Delete blog post - Only the user that created a blog post can delete it, by navigating to his specific post, accessing Read more. Then he will be redirected to the section of that post, where the Delete functionality is available. By hitting delete, the user will be redirected to the Delete page to confirm or to cancel the deletion.

* Pagination - Functionality that paginates blog posts to 3

##### *Products app*

 * Merchandise - by navigating to the Merchandise button in the navigation bar, the user is able to visit the items template, where they can add to cart and buy items.

##### *Cart app*

* Add to cart - User is able to add items to his cart, which are stored in the session while user is logged in.
The user can see the total number of items displayed in the cart button in the navigation bar.

* View cart - By accessing his cart, the user can see the items he bought.

* Modify cart - User can reduce the quantity of items.
When quantity is 0, the item is deleted from cart.

##### *Checkout app*

* Functionality to check if the cart is empty - If the total amount is 0, the user gets a message that his cart is empty and he has a button to visit the merchandise shop. Checkout button is disabled.

* Checkout - in the View cart page, user can access checkout app from the checkout button. He will be redirected to the checkout page.
Here he can view the items that he wants to buy and the total price.
In order to buy, he must complete 2 forms: one for Order, with personal information stored in the database and can be viewed only by admin(s), and second is the Stripe Payment form, which doesn't store any information on local server, but will communicate with the Stripe server.
If the card is accepted, the user will receive a success message and will be redirected to the items template.

##### *Partners page*

* Now partners have their own dedicated page with logos that if clicked it will redirect to the partner's website.

##### **Features left to implement**

The following requirements are left to be implemented in the future:

1. Forum app - Necessity for the community members to talk about different topics. Topics need to be categorized and also moderated by admins.
2. Apps departments - This app will be created for different towns where the Romanian Alpine Club has departments in order to organize the members there and to share info if required only with that department's members.
3. Report app - Automatically generate a monthly/yearly report with different information
4. Membership card - This app will generate automatically a card with the member's details, that will be loaded in .jpeg format and can be downloaded from member's profile.
5. Membership app - App to automatically pay for a type of membership(yearly)(regular, standard, retired) and also payment for registration(only once). Whoever registers before a date mentioned, can get a -10% discount.

6. **Admin functionalities**
     - honeypot django app - in order to notify the admin if someone else is trying to access the admin panel;
     - mail to admin(s) when someone registers to get approval from him(django-registration-redux > admin approval backend);
     - mail to admin(s) when someone buys merchandise, in order to be shipped to the address mentioned in the order form;

7. eLearning - eLearning platform to share written information and/or video courses


# Technologies Used
## Frontend

- Bootstrap 4

    Bootstrap is used in all the projects's apps from a base template, to create the User Interface and for better User Experience.

    The fluid grid and CSS Bootstrap classes, allows elements to be display in a harmonious way on different devices.

 - CSS3

    Used for personal styling

 - jQuery and Mosaic gallery
    
    To organize logos of partners

- Font Awesome

    To enhance the UI.

- Google Fonts

    For personal styling

- Logo 

    The Romanian Alpine Logo was edited with GIMP v2 so that the elements will be white and background transparent.

##### For elements such as typography, colors, logo, font etc. I was given the Romanian Alpine Club Brand Manual & Guidelines.
##### I can share this if needed with Code Institute.
## Backend
- Django 1.11 

    Python framework which can scale and with it was built the project.

- Python 3.6

- SQLite database used for development

- Postgres used for production

- Stripe 1.7

    For taking online payments.

- Amazon S3 - For storing static files, mainly images, due to Heroku's ephemeral file system which deletes static images.

# Testing

##### URLS
1. Testing urls 

    1.1. Testing visible links while user is not logged in

        i. Accessing links from navbar(Home, About, Login, Register) and footer, also Join and SignUp button from Home page, and verify that it routes to the desired page.
        ii. Accessing unauthorized pages while not logged in and check to see if it redirects to the login form.(for example accessing /profile,/products or /cart and check that it redirects to login form.)
    
    1.2 Testing accessible links when user is logged in
        
        i. Accessing links from navbar, footer and also all buttons from different pages, and verify that it routes to the desired page(for example from New blog post page to Merchandise).
        ii. While logged in, test to access routes that are accessible if not logged in(for example accessing /login and /register routes from browser, will redirect user to home page).

##### Users(accounts) app

1. Registration form 
    
        i. Access registration page from Register link or Join button
        ii.Try to submit the empty register form and verify that an error message from Django appears with the required input.
        iii. Try to submit the register form with different passwords and verify that a relevant warning message appears.
        iv. Try to submit the register form with the same username as one already registered in the database and verify that a relevant warning message prompts the user to choose another one.
        v. Try to submit the register form with all inputs valid and verify that a successful registered message appears, redirecting user to login form.   

2. Login form 

        i. Go to "Login" page from the menu.
        ii. Try to submit the empty login form and verify that an error message from Django displays with the required input.
        iii. Try to submit the login form only with the user name and verify that a relevant warning message appears.
        iv.  Try to submit the login form only with the password and verify that a relevant warning message appears.
        v. Try to submit the login form with all inputs valid and verify that a successful logged in message appears that redirects to the home page or to the page the user tried to access while not logged in(example /profile).

3. Forgot password

        i. Access forgot password from Login page and verify it redirects to password-reset template
        ii. If registered user chose his valid email, he will get an email from Django with a link to reset his password and also get successful message that email was sent.
        iii. Accessing the reset password link directs user to password-reset-confirm on Romanian Alpine Club site where he is requested to change his password.
        iv. Verify warning message displays when submitting the empty form or with different passwords.
        v. If password change is successful, verify it redirects to password-reset-complete and a success message displays with a button to login.
        vi. Test login button redirects to login page.
        vii. Verify logging in with username and new password.
        viii. Tested token with link for password reset after a day and it is not functional anymore.
        viii. Future improvement to verify that the email typed is already in the database.

4. Logout 

        i. Go to Logout link
        ii. Logging out redirects the user to the logout template.
        iii. Try to access the Log In Again button and check it redirects to login page.

5. Account page

    5.1. Profile page

        i. Go to Account page from navbar.
        ii. Try to access profile page and check it redirects to profile.
        iii. Check that information from the user is there.
    
    5.2 Edit profile page

        i. Go to Account page from navbar.
        ii. Try to access edit page and check it redirects to template.
        iii. Try to update profile while submitting without username or email and check warning message displays.
        iv. Try to upload an image for profile pic and check the name of the uploaded pic displays in the input field.
        v. Try to update page with desired new information and picture and verify it redirects back to profile page. Verify a success message displays and the profile picture is changed and resized.
        vi. Check in developer tools that the new profile pic is stored in Amazon's s3 bucket.
        vii. If no update is required, try to access back to profile button and check it redirects to profile page.

##### Blog app

1. Blog

    1.1 Blog view all posts


        i. Go to Blog link from navbar
        ii. Try to access Blog and check it redirects to the page.
        iii. Check to see if blog page displays all blog posts from different users.
        iv. Check to see if pagination is active(>3 blog posts).
        v. Try to access next link and check if it displays the next page with blog posts.
        vi. Try to access first and last link and check if it redirects to desired pages.
        vii. Try to access the Read more link from a post and check it redirects to that blog post details.
        viii. Try to access Back to blog link and check it redirects to main blog page.
        ix. As a logged in user, check to see if Update and Delete  links are available for own post.
        x. Try to update a blog post and verify that it updates and redirects to the post page.
        xi. Try to delete a blog post and verify it redirects to delete page and it displays two links - Confirm delete and Cancel. 
        xii. Try to confirm delete and verify post is deleted and user is redirected to main blog page.
        xiii. Try to cancel and verify user is redirected back to post.
        xiv. Try to access the author of a post link and verify it redirects to that author's page and it displays all his posts.

    1.2 Add new blog post

        i. Go to Blog link from navbar
        ii. Try to access New blog post and verify it redirects to the blog/new page.
        iii. Try to add a post without Title or Content and verify a warning message displays.
        iv. Try to add a post with information and verify it redirects to the new blog post.
        v. Try to access the main blog page and verify the new post is displayed first.

##### Products app

        i. Try to access Merchandise from navbar.
        ii. Verify it redirects to the /products app and all items are displayed correctly.

##### Cart app

    1.1 Add to cart

        i. Try to access add button without any input and verify it displays an error message.
        ii. Try to access the add button and verify the Cart from the navbar displays a badge with one item and the user is redirected to the products page.

    1.2 View cart

        i. Try to access Cart link from navbar and verify it redirects to the user's cart page where he can see the item he bought.
        ii. Try to view cart when user has no added item and verify a info message appears that the cart is empty. Verify that Checkout button is disabled and that a Visit merchandise shop button is displayed.
        iii. Try to access visit merchandise shop button and verify it redirects to products page.

    1.3 Modify cart

        i. Try to access the Update link and if the Cart has more items, verify that the cart and total price adjusts to the new user change.
        ii. Try to have no items in Cart and verify it gives a message that cart is empty.
        iii. Verify that Checkout button is disabled and that a Visit merchandise shop button is displayed.


##### Checkout app

        i. Try to access the Checkout button if the Cart has more than one item and verify it redirects to checkout page.
        ii. On checkout page, verify that total number of items, total price, order details form and stripe form are visible and accessible.
        iii. Try to pay without any input and verify error messages are displayed
        iv. Try to pay with only Order information and verify that error message from Stripe displays.
        v. Try to pay with all forms filled correctly except test card number and verify error message is displayed that card is invalid.
        vi. Try to pay with all forms correctly filled and verify that user is redirected to merchandise/products page and a successful message appears.
        vii. Verify Stripe dashboard and check that correct payment is displayd with the user's email.
        viii. Try to access admin panel and verify that the user's information for the order is displayed, together with what he ordered.

##### Responsiveness

        The project was tested with the following browsers locally: Chrome, Firefox, Internet Explorer 11.
        For checking how the project and pages flow for different devices, I used Chrome's developer's tools.

        The project was tested after deployment to Heroku on Android and iPhone.

# Deployment

##### Local installation 

    1. First clone the project
        https://github.com/Walachul/milestone4

    2. To start developing the project:

        i. Make sure you have Python 3.6 installed.

        ii.For this project I have used Microsoft's Visual Studio Code.

        iii. Create a virtual environment in Windows:
            Navigate to where the project folder is and run:
            python -m venv venv

        iv. Activate the venv:
        Navigate to venv and inside run:
        C:\Python\Django_Project_Name\venv>Scripts\activate
         If successfuly, you should see the name of the virtual environment in curly braces in the front of the path:
             (venv) C:\Python\Django_Project_Name\venv>

        v. To install packages:
            Navigate to the home folder:
            (venv) C:\Python\Django_Project_Name> pip install requirements.txt

        vi. Don't forget to create your superuser(admin)
            python manage.py createsuper

        vii. Make sure that stripe version 1.7 is installed in order for the stripe.js to work

        viii. You will need your own S3 bucket for the profile and products images.
        
        ix. Don't forget to set in settings.py DEBUG=True. It is turned off in production.
 ##### Environment variables

        You can either create an env.py and store the env variables there and import them where needed or

        In Windows, you can navigate to Control Panel > System > Advanced system settings > Environment Variables > add new

        The env variables needed are for Stripe, Amazon's Secret key, Django's secret key, database_url.

        To generate a random number for SECRET_KEY :

        in CMD:
            >>>import secrets
            >>>secrets.token_hex(16)
            >>>'15412c9e3e3ff5e03cac2270cc6fb57f'
            >>>exit()

        Django is setup to either use a Heroku Postgres url or the local SQLite url.

##### Heroku deployment

[Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

Useful commands

    (venv) C:\Python\Django_Project_Name>heroku login //for log in to Heroku
    (venv) C:\Python\Django_Project_Name> heroku apps:create example-app // need of unique app name

To add Heroku Hobby-dev PostgreSQL to the project:

    (venv) C:\Python\Example> heroku addons:add heroku-postgresql:hobby-dev

OR you can add this addon by going to

    heroku dashboard of your app > resources tab and searching for Heroku Postgres

You can eddit the config vars in the Settings windows of the app.

**Procfile**

web: gunicorn Romanian_Alpine_Club.wsgi

Final deployment

    git commit -a -m "deployment to heroku changes"
    git push heroku master

If you encounter errors you can visit the app's logs from the dashboard.

If by any change you need to delete migrations folder and __pycache__ for an app and need to modify a model and then makemigrations, you can use command python manage.py makemigrations --empty app-name.
After, you can run makemigrations normally.

Had to delete phoneNumber field because it was causing error with Postgres, but because it was copied in the first migration, I had to think of different things to get this sorted.

With some research, I have found this topic [How to force migrations to a DB if some tables already exists](https://stackoverflow.com/questions/43880426/how-to-force-migrations-to-a-db-if-some-tables-already-exist-in-django)

# Version control

Github

# Resources

- Code Institute 
- Google
- Youtube
- Stack Overflow
- Django documentation
- Django-bootstrap-form
- Various Django websites
- Python Crash Course book

# Content 

Inspiration for creating the project was taken by visiting the [American Alpine Club](https://americanalpineclub.org/) and [UK Alpine Club](http://www.alpine-club.org.uk/).

The content was taken from the still live site of the Romanian Alpine Club.

##### Media

Background images were obtained using Google's Images search results and I use them only for educational purposes only.

Images for the products are taken from the Brand Manual.

All media is uploaded to Amazon's S3.

# Credits

Credit is due to the following names.

 I would like to thank each and every one who has helped or contributed to my project in any way. Please see list of names below:

- Code Institute for introducing me to Python and Django framework
- Romanian Alpine Club
 - Mentor Aaron Sinnott
 - Slack channel information
 - Youtuber Corey Schafer
 - Youtuber Pretty Printed
 - Youtuber JustDjango
 - Youtuber Mike Hibbert
 - [PythonProgramming](https://pythonprogramming.net/)
 - [DjangoGirls](https://djangogirls.org/)
 - Python Crash Course book

# License

This project is released under the MIT license.
[MIT LICENSE](LICENSE.md)
