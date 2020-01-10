[![Build Status](https://travis-ci.org/Walachul/milestone4.svg?branch=master)](https://travis-ci.org/Walachul/milestone4)

# **Romanian Alpine Club**
###### Full Stack Milestone project 4

The idea/necessity for the project came alive when asked to construct from scratch the website of the Romanian Alpine Club and adding functionalities which now don't exist or need an upgrade.

Old live site here:  [ClubulAlpinRoman](https://www.clubulalpinroman.net/)

New site living here: [RomanianAlpineClub](heroku)

## **User Experience**

The app/website is build first and foremost for the actual members of the Romanian Alpine Club, who needed an upgrade to a platform, where they can login, interact, share information about hikes and other clibbing events and workshops, and also an admin(s) panel where they can check activity of the members.


One of the most important requirements that was asked for a new site was that to be mobile friendly, organized and to be accessible for anyone on every device they would use, so that was my main goal when started building it.

The app had to be user friendly and colorful, and the information needed to be displayed in eye-friendly mode.

## **User Stories**

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

## **Features**

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

## Testing

#####Users(accounts) app

1. Testing urls 

    1.1. Testing visible links while user is not logged in

        i. Accessing links from navbar(Home, About, Login, Register) and footer, also Join button from Home page, and verify that it routes to the desired page.
        ii. Accessing unauthorized pages while not logged in and check to see if it redirects to the login form.(for example accessing /profile,/products or /cart and check that it redirects to login form.)
    
    1.2 Testing accessible links when user is logged in
        
        i. Accessing links from navbar, footer and also all buttons from different pages, and verify that it routes to the desired page(for example from New blog post page to Merchandise).
        ii. While logged in, test to access routes that are accessible if not logged in(for example accessing /login from browser, will redirect user to home page)










