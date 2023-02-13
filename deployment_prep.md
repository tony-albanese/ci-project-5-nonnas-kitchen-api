
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

#### Adding the root route
This will display a welcome message if a user navigates to the home page of the api.
> create views.py in the main kitchen app and add the following code:
```
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        "message": "Nonna's Kitchen API"
    })

```

> Update urls.py in main kitchen app to link the root to the view.
```
urlpatterns = [
    …,
    path('', root_route)
]

```

#### Add Pagination, JSON renderer, and default DateTime format

> Update the REST_FRAMEWORK variable in settings.py for pagination and formatting the DateTime

```
REST_FRAMEWORK = {
    ...,
    'DEFAULT_PAGINATION_CLASS':  'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y'
    }

```

> Add the following to settings.py to set the JSON renderer
```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```