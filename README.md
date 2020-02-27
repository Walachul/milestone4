[![Build Status](https://travis-ci.org/Walachul/milestone4.svg?branch=master)](https://travis-ci.org/Walachul/milestone4)

# **Romanian Alpine Club**
## Full Stack Django Milestone project 4

At the request of the **Romanian Alpine Club**, I have developed an application which will go live and be a shared platform for guest users, members and admins. A new website/application was needed in order to allow users(members) to register, share information and communicate, share events, buy personalized merchandise online, participate in courses organized by the Club and pay for them online. The application also meets the requirement of automatically creating a membership card for a new member, functionality which was upgraded by also adding a QR code with discounts from Club's parteners.

Old live site here:  [ClubulAlpinRoman](https://www.clubulalpinroman.net/)

New site living on Heroku: [RomanianAlpineClub](https://clubul-alpin-roman.herokuapp.com/)

# **Table of Contents**
- [User experience](https://github.com/Walachul/milestone4#user-experience)
- [User stories](https://github.com/Walachul/milestone4#user-stories)
- [Features](https://github.com/Walachul/milestone4#features)
- [Database design](https://github.com/Walachul/milestone4#database-design)
- [Wireframes](https://github.com/Walachul/milestone4#database-design)
- [Technologies used](https://github.com/Walachul/milestone4#technologies-used)
- [Testing](https://github.com/Walachul/milestone4#testing)
- [Deployment](https://github.com/Walachul/milestone4#deployment)
- [Version control](https://github.com/Walachul/milestone4#version-control)
- [Resources](https://github.com/Walachul/milestone4#resources)
- [Content](https://github.com/Walachul/milestone4#content)
- [Credits](https://github.com/Walachul/milestone4#credits)

# **User Experience**

The app/website is build primarily for the actual members and admins of the Romanian Alpine Club, who needed an upgrade to a platform, where they can login, interact, share information about hikes and other climbing events and workshops,  and also an admin panel where they can check activity of the members, delete posts, check incoming orders from users who bought merchandise or course. 


One of the most important requirements that was asked from a new site was that to be mobile friendly, organized and to be accessible for anyone on every device they would use, so that was my main goal when started building it.

The app had to be user friendly and colorful, and the information needed to be displayed in eye-friendly mode.

# **User Stories**

In general, a user who is not registered will visit the site if he is interested in finding information regarding hiking, climbing and other mountain/outdoor activies and events, but also to find information regarding the history and pioneers of climbing in Romania.

##### Professional/Semi-Professional User

This type of user will generally want to find more information than what is displayed in the public section and more often he will want to become a member if he is not already one and get involved in the Club's activities and also do volunteering.

He will be able to register and access the available apps. 

In the blog app, he will be able to add, edit and delete information.

In the merchandise app/shop, he will be able to purchase custom made merchandise with the Romanian Alpine Club logo, using Stripe payment functionality.

In the courses app, he will be able to buy a course and participate on a given date.

In the account app, he will be able update his profile information (name, address, profile picture), download his membership card, view history of orders if any.

##### Amateur/Guest User

They share a passion for mountains.

More often, they will want to search for information which interests them and will want to register and from time to time get involved in activies and hikes.


##### Administrator

Another important requirement was that of the future website/app to have an administrator(or more), that can verify members information, what is the content they are posting and to be able to monitor the overall activity.

Also, the administrator should be able to add other admins as well, and to check information of the members that are buying merchandise or courses.

This functionality is possible with Django admin panel, in which I registered the required models from different apps.

# **Features**

## Home app

* Home page - Index page of the project. Users can read what the site is about(mission statement) and have a call to action button(Join the community) which redirects them to registration page.
* About - Contains two subpages:
          
    - History page - Users can read about the history of the Romanian Alpine Club and can see old pics of the founder and main members. To improve UI for reading, I have used AOS scroll library.
    - MISSION VISION VALUES page - Users can read more about the mission, values and vision of the Romanian Alpine Club

* Login button - Users who are already members can login and access available additional apps. If they don't have an account, they can register with a Sign Up button that will redirect to register page. 

    Here they can also reset their password by completing a form which requires valid email address(currently using personal email address to send emails from Django app , but will be switched in future with the Club's own email address).
    

* Registration - Users who want to become members can register by completing a form. If they are already a member, they have a Sign In which will redirect them to login page.

* Footer 
    
    - Home link to return to index
    - Social links to visit the social media pages of the Romanian Alpine Club
    - Partners page - to visit the partners page where users can view logos of the partners and visit their website(s)

* Partners page - Allows users/members to view logos of partners and visit their website(s).

## Users(accounts) app

* Registration page - Allows users to register to the site by filling the registration form (Username, email, full name, password, home address) 

  - Registration form - When submitting the form, the users will be prompted if the username or email is taken and to choose another one and if the passwords match. Also, they will be notified when they didn't fill a  field. When successful, a flash message will prompt the user that registration was successful and they can login.
* Login - Allows users to login to the site and have access to the other apps created(users/profile, blog,  merchandise shop, courses, search), by going to the login page and typing their credentials(username and password).

     The form created will notify the user if their credentials are wrong or forgot to fill a field. Also a prompt with successful message will pop if the login was correct and will redirect the user to the home page of the site or to another app(if he tried to access it without being logged in).

* Password reset - If the user forgets his password, he can access the *Forgot password* function offered by Django. This will redirect him to a form which will require his email. If the registered user that requires password change had entered a valid email address, he will receive on that email address a link from the app that will redirect him to a form to change his password. (Currently using personal email address to send emails from Django app , but will be switched in future with the Club's own email address)

    **Example:** ![password_reset_1](https://user-images.githubusercontent.com/42890101/75277583-8f934f00-5808-11ea-97d8-bc426abb84e9.PNG)
            ![password_reset_2](https://user-images.githubusercontent.com/42890101/75277708-d1bc9080-5808-11ea-8460-8b58cf255269.PNG)


## All the functionalities mentioned below require the user to be logged in

* Logout - Allows users to logout from the website. They are redirected to the logout template. If they had any cart items stored in session, they will lose it.

* Profile page - Users can see their information that they had entered in the registration form.

* Profile features:

  - General information obtained from the registration form and a default profile image;
  - Edit profile - Users can edit their personal information entered in the registration form(personal info and update their profile picture);
  - Resizable profile picture - The user's profile picture is resized in the background with python function and uploaded to Amazon's S3 bucket;
  - Membership Card - The card is automatically created in the profile and contains member name, when he joined and also QR Code. The membership Card updates automatically when user changes first or last name.
  - QR Code - The QR Code is placed inside the membership card and this contains useful information regarding discounts to different stores offered on behalf of the Club, name of the member and expiry date of the card. Member can visit a store with his card and after it was scanned, can get the right discount.
        
    To implement the membership card it took lots of research and trial&error + usage of django shell on how to create an image with Python and Pillow package, how to insert data from the user into it and how to position everything in the image. When the card was completed in the profile view and I could check it the local files, I realized that it was not a Django file, but a PIL image, which could not be saved in the membershipCard field from Profile Model. After some other research days, I tweaked the code from these two posts on stackoverflow( 1.[How to save pillow image object to Django ImageField](https://stackoverflow.com/questions/32945292/how-to-save-pillow-image-object-to-django-imagefield); 2. [How to convert PIL image to Django File](https://stackoverflow.com/questions/3723220/how-do-you-convert-a-pil-image-to-a-django-file) ) and I was succesful, while the card was saved accordingly to the folder and stored in S3 bucket.
    
    Another challenge was generating the membership card after the project beying deployed to Heroku. 
    By testing locally and re-enabling Debug in production, I found that Heroku was not finding the path to the Logo which was used for the creation of the membership card, altough the logo.png was stored in the s3 bucket, and thus getting a 500 error for the profile page.

    After some trial&error and research, I found the stackoverflow question: [How to read image file from s3 bucket directly into memory](https://stackoverflow.com/questions/44043036/how-to-read-image-file-from-s3-bucket-directly-into-memory#47910352), which helped me get the logo from the bucket.

    After this, membership card was generated successfully in production on Heroku platform.

    Example Membership Card
        ![membership_card](https://user-images.githubusercontent.com/42890101/75280365-96709080-580d-11ea-9de1-abb640ac0f1b.PNG)

    QR Code related to this membership card
    ![qr_code_test](https://user-images.githubusercontent.com/42890101/75280762-5d84eb80-580e-11ea-8d9d-e3ac3f6f763b.jpg)

    Implementing QR code had its own research time, due to the fact that I wanted to add more data, but I got an error from Python
    
         "QRCODE Version: error: qrcode.exceptions.DataOverflowError: Code length overflow. Data size (1092) > size available (152) ".
    After reading this article, [Information capacity and versions of the QR Code](https://www.qrcode.com/en/about/version.html), I increased version to 10 and QR code image was successfully implemented.


  - History of orders - Member can view purchase information of merchandise or courses
  - History of orders/View Order - allows users to access an order and view details of that order(product name, price of an product, how many items, grand total)

## Blog app
* Blog page- The user can view and read all blog posts from other users, by navigating to the blog section in the navigation bar.
       

* View all posts from a specific user -  Users are able to view all posts from a specific user by clicking on the user's name.

* Add blog post - The user is able to add a blog post by navigating to the section Blog > New blog post.

* Edit blog post - Only the user that created a blog post can edit it, by navigating to his specific post, accessing Read more. Then he will be redirected to the section of that post, where the Update functionality is available.

* Delete blog post - Only the user that created a blog post can delete it, by navigating to his specific post, accessing Read more. Then he will be redirected to the section of that post, where the Delete functionality is available. By hitting delete, the user will be redirected to the Delete page to confirm or to cancel the deletion.

* Pagination - Functionality that paginates blog posts rendered on the page to 3

## Courses app

* Allows admin(s) to add specific courses that can be rendered in the courses template.

* Courses page - allows user to view all courses organized by the Romanian Alpine Club

* Courses Details page - allows users to find more information about a specific course and also pay for it if they want to participate.

    The courses app was implemented after the merchandise app. The challenge faced after implementing the models and views was the payment method, because I wanted to use the same checkout app for two different products(Courses and Merchandise items). A user can add 1 course to the basket and pay for it. After researching on how to implement this feature, I found this article [Modeling polymorphism django python](https://realpython.com/modeling-polymorphism-django-python/#concrete-base-model), which recommends several methods for creating a polymorphic model. After analyzing my project and needs, I have decided to create a **concrete base model**, due to its nature of being created in the database table and in order to reference multiple products with common fields(in my case title and price are common for the Merchandise model in the products app and Courses model in the courses app) and also to get a total price of the items from cart.

    **Polymorphic Product concrete base model**

        class Product(models.Model):
            title = models.CharField(max_length=200, default="")
            price = models.DecimalField(max_digits=6, decimal_places=2, default="0")

            def __str__(self):
                return self.title
    How the Product model looks in the database: 
    ![polymorphic_model](https://user-images.githubusercontent.com/42890101/75283039-519b2880-5812-11ea-8767-b530c0726ec4.PNG)

    How the Courses model looks in the database:
    ![courses_courses](https://user-images.githubusercontent.com/42890101/75283285-d5edab80-5812-11ea-803a-a006c1526e50.PNG)

    **product_ptr_id**  acts as both primary key in the Courses table and foreign key in the concrete base model.

    And the Courses model from models file:

        class Courses(Product):

            description = models.TextField()
            dateAdded = models.DateTimeField(default=timezone.now)
            # Time period in which the course is organized
            periodOfTime = models.CharField(max_length=100)
            location = models.CharField(max_length=200)

            # Participants
            participants = models.CharField(max_length=20)
            """In order to get the correct video_url and render it in the iframe,
                you have to get the Embed Video from YouTube and get link as:
                https://www.youtube.com/embed/exampleVideo
                and paste it in the admin panel
            """
            video_url = models.CharField(max_length=200, null=True, blank=True)
            trainer = models.CharField(max_length=100)

            def __str__(self):
                return self.title

    After implementing the polymorphic model, I had to modify the contexts file of the cart app and import the Product model, so that instead of merchandise ID, the cart will store the products id.
  
    The next challenge was to modify **add_to_cart view** in order to get the cart items stored in session and redirect the user to a corresponding template after purchasing an item from Merchandise shop or Course from courses app, instead of always redirecting to merchandise template. Researching the django error code from debug, I found that if I can get the key of the item stored in session, that represents the ID of the item in the database, based on known value, I can do a query check to see if that item is in Merchandise table or Courses table.

    After researching and testing different methods, I found this response from stackoverflow, [Get key by value in dictionary](https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary), which separates the dictionary's values in a list, finds the position of that value(cart[id] in my case) and gets the key at that position in the keys list, and applied to my project as follows:
       
        itemInCart = list(cart.keys())[list(cart.values()).index(cart[id])]

    Then the query check and redirection accordingly:

        # Check to see if item in cart belongs to merchandise table
        productStored = Merchandise.objects.filter(id=itemInCart).first()
        # Get a list of all merchs in the table
        productsMerch = Merchandise.objects.all()

        request.session["cart"] = cart
        # Redirect the user to the page according to the item stored in cart session
        if productStored in productsMerch:
            return redirect(reverse("products-home"))
        else:
            return redirect(reverse("courses-home"))

## Products app

 * Merchandise page - by navigating to the Merchandise button in the navigation bar, the user is able to visit the items template, where they can add to cart and buy several different items. An admin can add additional items from the admin panel.

## Cart app

* Add to cart - User is able to add merchandise items or courses to his cart, which are stored in the session while user is logged in.
The user can see the total number of items displayed in the cart button in the navigation bar. 

    This view was modified and explanation is above as of why, in the Courses app section.

* View cart - By accessing his cart, the user can see the items he bought. This has a check in for total price, as to not let the user go to checkout and submit an empty form if he did not buy anything and cart has 0 items.

    ![warning_cart](https://user-images.githubusercontent.com/42890101/75287305-6c719b00-581a-11ea-87d4-fd4cf80f84a6.PNG)


* Modify cart - User can reduce the quantity of items.
When quantity is 0, the item is deleted from cart and user gets a prompt message that the cart is empty and he can visit the merchandise shop.

## Checkout app

* Functionality to check if the cart is empty - If the total amount is 0, the user gets a message that his cart is empty and he has a button to visit the merchandise shop. Checkout button is disabled.

* Checkout - in the View cart page, user can access checkout app from the checkout button. He will be redirected to the checkout page.
Here he can view the items that he wants to buy and the total price.
In order to buy, he must complete 2 forms: one for Order, with personal information stored in the database and can be viewed only by admin(s), and second is the Stripe Payment form, which doesn't store any information on local server, but will communicate with the Stripe server.
If the card is accepted, the user will receive a success message and will be redirected to the items template.

    Example
        ![order_items_admin](https://user-images.githubusercontent.com/42890101/75287700-1e10cc00-581b-11ea-86d4-14277cc5f18b.PNG)


##### **Features left to implement**

The following requirements by the Romanian Alpine Club members are left to be implemented in the future, due to time constraints to submit the project:

1. Apps departments - This app will be created for different towns where the Romanian Alpine Club has departments in order to organize the members there and to share info if required only with that department's members.
2. Facebook API - to get the content dynamically from the Club's page.
3. Google API - to be able to select location and store it in the location field from Courses Model.
        

4. **Admin functionalities**
     - honeypot django app - in order to notify the admin if someone else is trying to access the admin panel;
     - mail to admin(s) when someone registers to get approval from him(django-registration-redux > admin approval backend);
     - mail to admin(s) when someone buys merchandise, in order to be shipped to the address mentioned in the order form;


# Database design

![data_store_integration](https://user-images.githubusercontent.com/42890101/75296445-7d77d780-582d-11ea-99c3-1ec46bc94508.PNG)

SQLite was used in the development process. Migrated to PostgreSQL when project was deployed to Heroku for production.

# Wireframes
![1-Homepage](https://user-images.githubusercontent.com/42890101/75480328-5f32e880-59a1-11ea-81ac-df370acaa0ae.png)

![2-Home-page-tablet-mode](https://user-images.githubusercontent.com/42890101/75480390-7d004d80-59a1-11ea-85d5-1d143c7f7852.png)

![3-Login-mobile](https://user-images.githubusercontent.com/42890101/75480423-8e495a00-59a1-11ea-8865-9bffc2e6e230.png)

![4-Login-tablet](https://user-images.githubusercontent.com/42890101/75480436-96a19500-59a1-11ea-98ad-6819f1201415.png)

![5-Register-mobile](https://user-images.githubusercontent.com/42890101/75480467-a620de00-59a1-11ea-9219-76965e4e647d.png)

![6-Register-tablet](https://user-images.githubusercontent.com/42890101/75480483-b042dc80-59a1-11ea-9ec9-f610bd0d5439.png)

![7-Profile-page-mobile](https://user-images.githubusercontent.com/42890101/75480511-bc2e9e80-59a1-11ea-8858-575c7ef801b8.png)

![8-Profile-page-tablet](https://user-images.githubusercontent.com/42890101/75480535-c2bd1600-59a1-11ea-8ac1-b24f474c6c72.png)

![9-Courses-Merchandise-mobile](https://user-images.githubusercontent.com/42890101/75480574-cf416e80-59a1-11ea-86e1-9496c6039655.png)

![10-Merchandise-tablet](https://user-images.githubusercontent.com/42890101/75483650-97d5c080-59a7-11ea-8c5a-40fc097eeb61.png)

![11-COURSE-DETAILS-mobile](https://user-images.githubusercontent.com/42890101/75483675-a328ec00-59a7-11ea-81bb-cb4e5852d714.png)

# Technologies Used
## Frontend

- Bootstrap 4

    Bootstrap is used in all the projects's apps from a base template, to create the User Interface and for better User Experience.

    The fluid grid and CSS Bootstrap classes, allows elements to be display in a harmonious way on different devices.

 - CSS3

    Used for personal styling

- Font Awesome

    To enhance the UI.
- jQuery and Mosaic gallery
    
    To organize logos of partners

- [Animate on Scroll Library](https://michalsnik.github.io/aos/)

    Improve UI and reading of the History page when user scrolls down.

- Google Fonts

    For personal styling

- Logo 

    The Romanian Alpine Logo was edited with GIMP v2 so that the elements will be white and background transparent.

##### For elements such as typography, colors, logo, font etc. I was following the Romanian Alpine Club Brand Manual & Guidelines.

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

## Unit testing
Apps in the project have their own automated tests for app configuration, views and forms.

 Testing was also performed in the Django shell.

 Used commands to run tests from a file in an app(example courses app):

        (venv)D:\Python\Django_Projects\ClubulAlpinRoman> python manage.py test courses.test_apps

Used commands to run tests from the django shell:

        (venv)D:\Python\Django_Projects\ClubulAlpinRoman> python manage.py shell
        >>> from django.contrib.auth.models import User
        >>> from django.test.utils import setup_test_environment
        >>> from django.test import Client
        >>> setup_test_environment()
        >>> client = Client()
        >>> response = c.get('/profile/')
        302
        >>> c.get('/profile/')
        <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/login/?next=/profile/">
        >>>exit()

## URLS
Manual tests performed
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

##### Courses app
        i. Try to access courses from navbar.
        ii. Verify it redirects to the /courses app and all courses are displayed correctly.
        iii. Try to access a course details from Read More button and verify it redirects to that specific course.
        iv. Try to pay for the course and verify that it redirects to the courses template.

##### Products app

        i. Try to access Merchandise from navbar.
        ii. Verify it redirects to the /products app and all items are displayed correctly.

##### Cart app

    1.1 Add to cart

        i. Try to access add button without any input and verify it displays an error message.
        ii. Try to access the add button and verify the Cart from the navbar displays a badge with one item and the user is redirected to the products or courses page.

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
        ##### Stripe  card test details:

            - card number 4242 4242 4242 4242
            - CVV any 3 number digits
            - Expiry date - any future expiry date

        v. Try to pay with all forms filled correctly except test card number and verify error message is displayed that card is invalid.
        vi. Try to pay with all forms correctly filled and verify that user is redirected to merchandise/products page and a successful message appears.
        vii. Verify Stripe dashboard and check that correct payment is displayd with the user's email.
        viii. Try to access admin panel and verify that the user's information for the order is displayed, together with what he ordered.

## Responsiveness
 The project was tested with the following browsers locally: Chrome, Firefox, Internet Explorer 11.

 For checking how the project and pages flow for different devices, I used Chrome's developer's tools.

 The project was tested after deployment to Heroku on Android and iPhone.

# Deployment

## Heroku deployment

[Install Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

Useful commands

To log in to Heroku

    (venv) C:\Python\Django_Project_Name>heroku login 
    
Create new unique app name for your project

    (venv) C:\Python\Django_Project_Name> heroku apps:create example-app 

To add Heroku Hobby-dev PostgreSQL to the project:

    (venv) C:\Python\Example> heroku addons:add heroku-postgresql:hobby-dev

OR you can add this addon by going to

    heroku dashboard of your app > resources tab and searching for Heroku Postgres

You need to copy all env variables in the Settings windows of the app in Heroku

**Procfile**

web: gunicorn Romanian_Alpine_Club.wsgi

Final deployment

    git commit -a -m "deployment to heroku changes"
    git push heroku master

If you encounter errors you can visit the app's logs from the dashboard.

If by any chance you need to delete migrations folder and __pycache__ for an app and need to modify a model and then makemigrations, you can use command

    python manage.py makemigrations --empty app-name.
After, you can run makemigrations normally.

I had to delete phoneNumber field because it was causing error with Postgres, but because it was copied in the first migration, I had to think of different things to get this sorted.

With some research, I have found this topic [How to force migrations to a DB if some tables already exists](https://stackoverflow.com/questions/43880426/how-to-force-migrations-to-a-db-if-some-tables-already-exist-in-django)



## Local installation 

1. First clone the project

        git clone https://github.com/Walachul/milestone4.git

2. Create a virtual environment in Windows. Navigate to where the project folder is and run:

            python -m venv venv

3. Activate the venv - Navigate to venv folder in the terminal window and inside run:

            C:\Python\Django_Project_Name\venv>Scripts\activate
    If activation was successful, you should see the name of the virtual environment in curly braces in the front of the path:
   
            (venv) C:\Python\Django_Project_Name\venv>

4. Install packages needed for the project:
    Navigate to the home folder and run:

            (venv) C:\Python\Django_Project_Name> pip install requirements.txt
5. Create your superuser(admin)

            python manage.py createsuper

6. Run command:

            python manage.py makemigrations

    which is responsible for creating new migrations based on the changes you have made to your models.

7. Run command:

            python manage.py migrate

     which is responsible for applying the changes to your database and create the SQLite database.


8. Create an env.py to store the env variables. The env variables needed for the project are: DATABASE_URL, SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_ADDRESS, EMAIL_PASSWORD

        
9. You will need your own S3 bucket for storing media.
        
10. In settings, set DEBUG=True. It is turned off in production.

11. To generate a random number for SECRET_KEY, in CMD:

            >>>import secrets
            >>>secrets.token_hex(16)
            >>>'15412c9e3e3ff5e03cac2270cc6fb57f'
            >>>exit()





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
