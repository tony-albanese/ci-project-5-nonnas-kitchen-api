
### Preparation
#### Setting up Jason Web Tokens  
> Install dj-rest-auth package.  
> Add to INSTALLED_APPS  

        ```
        INSTALLED_APPS = [
        ...
        'django_filters',

        'rest_framework.authtoken', 
        'dj_rest_auth', 

        ‘profiles’,
        ...
        ]   

        ```
> Update urls.py
```
urlpatterns = [
    ...
  path('dj-rest-auth/', include('dj_rest_auth.urls')),
    ...
  ]
```
> Migrate the database.

```
python manage.py migrate
```
#### User registration

> Install django all-auth and update INSTALLED_APPS
```
$ pip install 'dj-rest-auth[with_social]'

INSTALLED_APPS = [
    …,
    'dj_rest_auth',
     
    'django.contrib.sites', 
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'dj_rest_auth.registration',

    'profiles',
    ...,
]

```

> Update settings.py
```
SITE_ID = 1
```

> Add registration urls to urls.py
```
urlpatterns = [
    …,
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

   …,
]
```


#### JWT Functionality
> Install simplejwt app
```
$ pip install djangorestframework-simplejwt
```

> Create session authentication value for dev mode.
```
os.environ['DEV'] = '1'
```

> Differentiate between dev mode and production mode authentication. Add the following to settings.py.
```
​​REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [( 
        'rest_framework.authentication.SessionAuthentication' 
        if 'DEV' in os.environ 
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
         )]
    }

```

> Add the following to settings.py to enable token authentication, HTTPS transmission, and declare names for refresh token cookies and access cookies.
```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
```
#### Add user details to returned data after login

> Create serializers.py in main app and add the following code:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```

> Override the default serializer in settings.py and then run migrations.
```
REST_AUTH_SERIALIZERS = {'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'}

$ python manage.py migrate
```

> update requirements.txt

```
$ pip freeze > requirements.txt
```