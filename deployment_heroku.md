### Deploying to Heroku

#### Create PostGres database
The first step is to create a new instance of a PostgreSQL database on ElephantSQL
+ Navigate to [ElephantSQL](https://www.elephantsql.com/)
+ Login or create an account
+ Go to the Dashboard
+ Click "Create New Instance"
+ Name the database
+ Select Tiny Turtle plan and region
+ Click **Review** button
+ Clicke **Create Instance** button
+ Copy the database URL


#### Create App in Heroku
+ Navigate to [Heroku]()
+ Login or create an account
+ Click on **Create new app**
+ Give the app a name
+ Click on **Create app**
+ Open Settings Tab
+ Add Config Var for DATABASE_URL and paste the url pointing to the newly created Postgres database from ElephantSQL

#### Setting up GitPod workspace
There are still a few more changes to make in the GitPod workspace before deploying to Heroku.
> Intall packages needed for Heroku to connect to external databases.
```
$ pip install dj_database_url==0.5.0 psycopg2
```
>  import dj_database in settings.py
```
import os
import dj_database_url
```

> Update the DATABASES section in settings.py to distinguish between the database used for development and the one used for production.
```
if 'DEV' in os.environ:
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
 else:
     DATABASES = {
         'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
     }
```


> Add the following line to env.py to link to the Postgres database url
```
 os.environ.setdefault("DATABASE_URL", "PostgreSQL URL")
```

#### Testing the database connection
> Comment out the DEV environment variable
```
 os.environ['CLOUDINARY_URL'] = "cloudinary://..."
 os.environ['SECRET_KEY'] = "Z7o..."
 # os.environ['DEV'] = '1'
 os.environ['DATABASE_URL'] = "postgres://..."
 ```

 > add a print("connected") statement to else clause in DATABASES in settings.py to verify connection.

 > Make a dry-run migration to confirm connection to external database. If it works the print statement can be removed.
 ```
 $  python manage.py makemigrations --dry-run
 ```

 > Migrate the database
 ```
 $ python manage.py migrate
 ```

> Create a super user
```
 $ python manage.py createsuperuser
```

#### Continuing with GitPod workspace setup
> install gunicorn and update requirements.txt
```
$ pip install gunicorn django-cors-headers
$ pip freeze --local > requirements.txt
```

> Create Procfile and add the following lines:
```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn kitchen.wsgi
```

> Add allowed hosts to settings.py
```
ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']
```

> Add corsheaders to INSTALLED_APPS
```
INSTALLED_APPS = [
    ...
    'dj_rest_auth.registration',
    'corsheaders',
    ...
 ]
 ```

 > Add corsheaders middleware to the TOP of the MIDDLEWARE

```
 MIDDLEWARE = [
     'corsheaders.middleware.CorsMiddleware',
     ...
 ]
 ```

 > Under the MIDDLEWARE list, set the ALLOWED_ORIGINS for the network requests made to the server with the following code:
 ```
  if 'CLIENT_ORIGIN' in os.environ:
     CORS_ALLOWED_ORIGINS = [
         os.environ.get('CLIENT_ORIGIN')
     ]
 else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]
```

> Enable sending cookies in cross-origin requests so that users can get authentication functionality
```
 else:
     CORS_ALLOWED_ORIGIN_REGEXES = [
         r"^https://.*\.gitpod\.io$",
     ]

 CORS_ALLOW_CREDENTIALS = True
 ```

> To be able to have the front end app and the API deployed to different platforms, set the JWT_AUTH_SAMESITE attribute to 'None'. Without this the cookies would be blocked
 ```
  JWT_AUTH_SAMESITE = 'None'
 ```


> To be able to have the front end app and the API deployed to different platforms, set the JWT_AUTH_SAMESITE attribute to 'None'. Without this the cookies would be blocked
```
 # SECURITY WARNING: keep the secret key used in production secret!
 SECRET_KEY = os.getenv('SECRET_KEY')
```


> Set a NEW value for your SECRET_KEY environment variable in env.py, do NOT use the same one that has been published to GitHub in your commits
```
 os.environ.setdefault("SECRET_KEY", "CreateANEWRandomValueHere")
```

> Set the DEBUG value to be True only if the DEV environment variable exists. This will mean it is True in development, and False in production
```
DEBUG = 'DEV' in os.environ
```

> Comment DEV back in env.py

```
 import os

 os.environ['CLOUDINARY_URL'] = "cloudinary://..."
 os.environ['SECRET_KEY'] = "Z7o..."
 os.environ['DEV'] = '1'
 os.environ['DATABASE_URL'] = "postgres://..."
```

Ensure the project requirements.txt file is up to date. In the Gitpod terminal of your DRF API project enter the following
```
$ pip freeze --local > requirements.txt
```

#### Heroku Deployment
+ Add SECRET_KEY amd CLOUDINARY_URL to config vars. The SECRET_KEY value is a made up string. The CLOUDINARY_URL is copied from settings.py.

+ The dj-rest-auth logout bug was fixed by copying the solution from Code Institute's walkthrough project. A custom logout view was created which will send an expired token to force logout. The code was taken from [this repo](https://github.com/Code-Institute-Solutions/drf-api/blob/master/drf_api/views.py#L16) and the urls updated from this [urls](https://github.com/Code-Institute-Solutions/drf-api/blob/5210e34d25111e1556d10e895206e255d990e4bb/drf_api/urls.py#L25) file.

+ ALLOWED_HOSTS was modified to make the heroku host an environmental variable to prevent multiple instances.
```
ALLOWED_HOSTS = [
   os.environ.get('ALLOWED_HOST'),
   'localhost',
]
```
The value for the heroku app name was added as an addtional config var named ALLOWED_HOST in Heroku. The value is the name of the app.

+ CLIENT_ORIGIN_DEV was added to make development of the front end with GitPod possible. The following block replacced the else statement in the if "CLIENT_ORIGIN..." statement

```
if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```
+ Changes were commited and pushed to GitHub
+ In Heroku, the Deploy tab was selected.\
+ Connect to GitHub was chosen
+ The project repo was selected
+ Click on **Connect**
+ Deploy Branch from the Manual Deploy section was used
+ The main branch was selected and **Deploy** was clicked