# Test Tables
## Profiles Endpoint Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Get all profiles|As a developer <br> When the /profiles endpoint is entered <br> A list of all profiles is returned with status code 200 <br> and in JSON format|PASS|
|Get individual profile|As a developer <br> When the /profiles/id endpoint is entered <br> A the profile belonging to the given is returned with status code 200 <br> and in JSON format|PASS|
|Get individual profile error|As a developer <br> When the /profiles/id endpoint is entered <br> And an invalid id is entered<br>A response is returned indicating a 404 error <br> and in JSON format|PASS|
|Update individual profile|As a developer <br> When the /profiles/id endpoint is entered <br> If I am the owner of the profile <br> I can send updated data to the profiles/id through a POST request <br> a response with code 200 and the updated data in JSON format is returned|PASS|
|Update own profile|As a developer <br> When the /profiles/id endpoint is entered <br> If I am not the owner of the profile <br> I cannot send updated data to the profiles/id through a POST request <br>If I try, a response with code 403 and and error message in JSON format is returned|PASS|

## Post search and filter
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|search|As a user <br> when I enter a search term in the /posts endpoint filter form <br> posts with author or titles that contain the search terms are displayed.|PASS|
|filter by category|As a user <br> when I select a category from the /posts endpoint dropdown filter <br> posts whose category matches the selected one are displayed.|PASS|
|filter by author|As a user <br> when I select an author from the /posts endpoint dropdown filter <br> posts whose author matches the selected one are displayed.|PASS|

## Recipe search and filter
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|search|As a user <br> when I enter a search term in the /recipes endpoint filter form <br> recipes with author or titles that contain the search terms are displayed.|PASS|
|filter by dish_type|As a user <br> when I select a dish_type from the /recipes endpoint dropdown filter <br> recipes whose dish_type matches the selected one are displayed.|PASS|
|filter by author|As a user <br> when I select an author from the /recipes endpoint dropdown filter <br> recipes whose author matches the selected one are displayed.|PASS|
|filter by difficulty|As a user <br> when I select an difficulty from the /recipes endpoint dropdown filter <br> recipes whose difficulty matches the selected one are displayed.|PASS|