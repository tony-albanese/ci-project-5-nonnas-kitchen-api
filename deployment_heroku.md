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