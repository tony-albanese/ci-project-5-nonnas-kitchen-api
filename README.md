![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Nonna's Kitchen Backend


# Version Control Strategy
Git was employed in this project and the project code hosted on GitHub. I used branches in order to keep the main branch as "pure" as possible. The strategy was to have each branch dedicated to one feature or fix. Once I was satisfied at a particular stage of a branch, I would navigate to GitHub, click on my repository, select the branch, and create a pull request. GitHub would then check if there are no conflicts and indicate if the branch could be merged into main. (One can choose which branch to merge into.) Once the pull request is created, I navigated down, wrote a comment, and clicked on the green Merge button and the commits would be merged into the main branch. I tried to keep commits as atomic as possible - focusing only on one element or feature at a time. This was not always the case, but most of the commits are relatively small changes. In addition, I tried not to mix features in a branch. Small tweaks to other features were allowed, but the majority of the work on each branch was dedicated to that one feature. This is in line with the agile method of tackling a project - the team (in this case me) should only work on one feature at a time. 


# Deployment
## Technology Used
+ [Cloudinary](https://cloudinary.com/) - Media cloud storage service to serve static files
+ [ElephantSQL](https://www.elephantsql.com/) - An online service running a PostgreSQL server as a service.
+ [Pillow](https://pillow.readthedocs.io/en/stable/) A Python imaging library to help process images.

## Project Creation
+ Cloned Code Institute Repository and gave the new respositry the name [ci-project-5-nonnas-kitchen-backend](https://github.com/tony-albanese/ci-project-5-nonnas-kitchen-backend)
+ Initialized GitPod Workspace by clicking on the GitPod button on the respository
+ Installed support libraries and Django according to the walkthrough on Code Institute the steps of which are outlined as follows:

    + Install django
    + Create project
    + Install Cloudinary Storage and Pillow
    ```
    pip install ‘django<4’
    django-admin startproject nonnas_kitchen .
    pip install django-cloudinary-storage
    pip install Pillow
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