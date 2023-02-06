![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Nonna's Kitchen Backend

## Developer User Stories
### Profiles
+ As a developer using Nonna's Kitchen backend to build applications, I want to fetch a list of profiles so that I can display them to the user in my application.
+ As a developer using Nonna's Kitchen backend to build applications, I want to fetch the data from one profile so that I can display it to the user for them to edit.
+ As a developer using Nonna's Kitchen backend to build applications, I want and endpoint to modify profile data so that I can provide profile editing features to end users.
+ As a developer using Nonna's Kitchen backend to build applications, I want to fetch profile data with permissions so that I protect sensitive user data from exposure and compromise.

### Posts
+ As a developer using Nonna's Kitchen backend to build applications, I want an endpoint to get all posts so that I do not have to manually query the database to get the data.
+ As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to save a Post object to the database so that users of my application can share their content.
+ As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to delete a Post so that I do not have to manually update the database when a user deletes their post.
+ As a developer using Nonna's Kitchen backend to build applications, I want to and endpoint to update a Post so that I do not have to manually update the database when a user updates their post.
+ As a developer using Nonna's Kitchen backend to build applications, I want the backend to prevent users from modifiying or deleting posts that they did not author so that I do not have to check for permissions manually.

### Comments
+ As a developer using Nonna's Kitchen backend to build applications, I want an endpoint for users to comment on a post so that I do not have to manually write to the database on the front end.
+ As a developer using Nonna's Kitchen backend to build applications, I want an endpoint for users to update a comment on a post so that I do not have to manually write to the database on the front end.
+ As a developer using Nonna's Kitchen backend to build applications, I want an endpoint to get all of the comments so that I do not have to query the database manually.
+ As a developer using Nonna's Kitchen backend to build applications, I want the backend to prevent the user from modifying or deleting comments that they are not the author of so that I do not have to implement these checks on the front end.

### Likes
As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to add a like to a BlogPost so that I do not have to query the database manually.
As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to delete a like so that I do not have to query the database manually.
As a developer using Nonna's Kitchen backend to build applications, I want to the backend to prevent users from deleting a like they did not create so that I do not have to perform this check on the front end..

# Database Design
## Models
The **User** model is an extension of the **AbstractUser** model from Django authorization app. The reason for doing so is to make it easier to customize the User model should the need arize. In Django, it is exceedingly difficult, if not impossible, to modify the User object in the middle of a project without resetting the database. Using a custom model from the start, even if unmodified, should make future changes much less painful. 

settings.py was modified with the following setting so that django authorizaton uses this custom model.
```
AUTH_USER_MODEL = 'kitchen_user.User'
```

The **Profile** model encapsulates the extra data to enhance the standard information in the User model. The Profile contains additional fields for a biography, an avatar, and a cooking speciality.
|Profile ||
|-----|----|
|type|field name|
|ForeignKey(User) |owner|
|DateTimeField|created_on|
|CharField|first_name|
|CharField|last_name|
|TextField|bio|
|CharField|specialty|
|ImageField|avatar|

The **BlogPost** model encapsulates the information a user wants to share on the site. The idea behind a **BlogPost** object is that is supposed to be realtively short (1 to 2 paragraphs) and is supposed to represent a memory or anecdote connected to food from their ancestors. In addition to content, the user can (and should) attach a photo to the post. In addition, they must categorize the post as a history, anecdote, or tip. 

|BlogPost ||
|-----|----|
|type|field name|
|ImageField|cover_image|
|User|author|
|DateTimeField|created_on|
|CharField|title|
|TextField|content|
|UrlField|link|
|CharField|category|

The **Comment** model encapsulates the information required for a User to leave a comment on a BlogPost. The author field is a one-to-many realationhip with a User since each Comment can only have one author. There is a also a one-to-money relationship with the BlogPost because each Comment can only belong to one BlogPost but a BlogPost can have many Comments.
|Comment ||
|-----|----|
|type|field name|
|ForeignKey(User)|author|
|ForeignKey(BlogPost)|blog_post|
|DateTimeField|created_on|
|TextField|body|


# Features
## Profiles Endpoint
```
GET profiles/
```
This endpoint will return all of the profiles.
![All Profiles](repo_images/all_profiles.png)
> As a developer using Nonna's Kitchen backend to build applications, I want to fetch a list of profiles so that I can display them to the user in my application.

```
GET profiles/<int:id>
PUT profiles/<int:id>
```
This endpoint will retrieve the details for a particular Profile. The id (which serves as the primary key), is used to determine which Profile to fetch. If the current user is the owner of the Profile, they are allowed to edit it and save the changes. Otherwise, they can only view it. In the following screenshots, one Profile belongs to the user and the other not. They can edit the one that belongs to them.
![Individual Profile Is Owner](repo_images/profile_is_owner.png)  
![Individual Profile Not Owner](repo_images/profile_not_owner.png)
> + As a developer using Nonna's Kitchen backend to build applications, I want to fetch the data from one profile so that I can display it to the user for them to edit.  
> + As a developer using Nonna's Kitchen backend to build applications, I want and endpoint to modify profile data so that I can provide profile editing features to end users.  
> + As a developer using Nonna's Kitchen backend to build applications, I want to fetch profile data with permissions so that I protect sensitive user data from exposure and compromise.  

## Posts endpoint
```
GET posts/
POST posts/
```
This endpoint fetches all of the posts from the database. If the user is authenticated, they are allowed to add a post.
![get all posts screenshot](repo_images/get_posts.png)
> + As a developer using Nonna's Kitchen backend to build applications, I want an endpoint to get all posts so that I do not have to manually query the database to get the data.  
> + As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to save a Post object to the database so that users of my application can share their content.

```
GET posts/<int:id>
PUT posts/<int:id>
DELETE posts/<int:id>
```
These endpoints are to view the details for an individual post. If the user is authenticated, they can modify or delete the post ONLY if they are the author of the post.
![modify delete post if owner](repo_images/post_detail_isauthor.png)
> + As a developer using Nonna's Kitchen backend to build applications, I want to have an endpoint to delete a Post so that I do not have to manually update the database when a user deletes their post.
> + As a developer using Nonna's Kitchen backend to build applications, I want to and endpoint to update a Post so that I do not have to manually update the database when a user updates their post.
> + As a developer using Nonna's Kitchen backend to build applications, I want the backend to prevent users from modifiying or deleting posts that they did not author so that I do not have to check for permissions manually.

## Comment Endpoint
```
GET comments/
POST comments/
```
These endpoints return all of the comments in the database (GET) and allow a user to add a comment to a particular BlogPost if they are logged in.
![get and post comment](repo_images/comment_list.png)

> + As a developer using Nonna's Kitchen backend to build applications, I want an endpoint for users to comment on a post so that I do not have to manually write to the database on the front end.
> + As a developer using Nonna's Kitchen backend to build applications, I want an endpoint to get all of the comments so that I do not have to query the database manually.
> + As a developer using Nonna's Kitchen backend to build applications, I want the backend to prevent the user from modifying or deleting comments that they are not the author of so that I do not have to implement these checks on the front end.

```
GET comments/<int:id>
PUT comments/<int:id>
DELETE comments/<int:id>
```
These endpoints allow a user to modify a comment if they are logged in AND are the author of the comment. 
![comment detail](repo_images/comment_detail.png)
> + As a developer using Nonna's Kitchen backend to build applications, I want an endpoint for users to update a comment on a post so that I do not have to manually write to the database on the front end.
> + As a developer using Nonna's Kitchen backend to build applications, I want the backend to prevent the user from modifying or deleting comments that they are not the author of so that I do not have to implement these checks on the front end.

# Testing
## Behavior Driven Development (BDD)
The testing done here is BDD - each test is described as a story in which a description of the software requirements, the user actions, and the expected outcome are given along with a result of PASS or FAIL. To reduce the length of the readme, here is a link to the [testing tables](test_cases.md) describing the various test cases.

# Version Control Strategy
Git was employed in this project and the project code hosted on GitHub. I used branches in order to keep the main branch as "pure" as possible. The strategy was to have each branch dedicated to one feature or fix. Once I was satisfied at a particular stage of a branch, I would navigate to GitHub, click on my repository, select the branch, and create a pull request. GitHub would then check if there are no conflicts and indicate if the branch could be merged into main. (One can choose which branch to merge into.) Once the pull request is created, I navigated down, wrote a comment, and clicked on the green Merge button and the commits would be merged into the main branch. I tried to keep commits as atomic as possible - focusing only on one element or feature at a time. This was not always the case, but most of the commits are relatively small changes. In addition, I tried not to mix features in a branch. Small tweaks to other features were allowed, but the majority of the work on each branch was dedicated to that one feature. This is in line with the agile method of tackling a project - the team (in this case me) should only work on one feature at a time. 


# Deployment
## Technology Used
+ [Cloudinary](https://cloudinary.com/) - Media cloud storage service to serve static files
+ [ElephantSQL](https://www.elephantsql.com/) - An online service running a PostgreSQL server as a service.
+ [Pillow](https://pillow.readthedocs.io/en/stable/) A Python imaging library to help process images.
+ [django-taggit](https://django-taggit.readthedocs.io/en/latest/)A django app for storing and searching tags

## Project Creation
+ Cloned Code Institute Repository and gave the new respositry the name [ci-project-5-nonnas-kitchen-backend](https://github.com/tony-albanese/ci-project-5-nonnas-kitchen-backend)
+ Initialized GitPod Workspace by clicking on the GitPod button on the respository
+ Installed support libraries and Django according to the walkthrough on Code Institute the steps of which are outlined as follows:

    + Install django
    + Create project
    + Install Cloudinary Storage and Pillow
    ```
    $ pip install ‘django<4’
    $ django-admin startproject nonnas_kitchen .
    $ pip install django-cloudinary-storage
    $ pip install Pillow
    ```
    
    + Add these apps to settings.py
    ```
    INSTALLED_APPS = [
    (...)
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    ]
    ```

    + Create env.py, add import os, and add variable for CLOUDINARY_STORAGE
    ```
    import os
    os.environ['CLOUDINARY_URL'] = 'url copied from cloudinary'
    ```
    + Update settings.py
    ```
    if os.path.exists('env.py'):
    import env

    CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }
    ```
    + Created profiles app and added it to settings.py
    ```
    $ python manage.py startapp profiles

    INSTALLED_APPS = [
        (...),
        'profiles',
    ]
    ```
    + Install Django REST Framework and update settings.py
    ```
    $ pip install djangorestframework

    INSTALLED_APPS = [
        'cloudinary',
        'rest_framework'
        'profiles'
    ]
    ```

# Credits
Default avatar: <a href="https://www.flaticon.com/free-icons/user" title="user icons">User icons created by logisstudio - Flaticon</a>
Default BlogPost image: <a href="https://www.freepik.com/free-vector/plate-cuttlery-graphic-illustration_2685788.htm#query=meal&position=1&from_view=search&track=sph">Image by rawpixel.com</a> on Freepik

The code for implementing a ratings bar came from this Medium blog post: [Django: Implementing Star Rating](https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c)