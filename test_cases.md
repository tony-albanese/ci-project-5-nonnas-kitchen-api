# Test Tables
## Profiles Endpoint Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Get all profiles|As a developer <br> When the /profiles endpoint is entered <br> A list of all profiles is returned with status code 200 <br> and in JSON format|PASS|
|Get indiviudal profile|As a developer <br> When the /profiles/id endpoint is entered <br> A the profile belonging to the given is returned with status code 200 <br> and in JSON format|PASS|
|Get indiviudal profile error|As a developer <br> When the /profiles/id endpoint is entered <br> And an invalid id is entered<br>A response is returned indicating a 404 error <br> and in JSON format|PASS|
|Update individual profile|As a developer <br> When the /profiles/id endpoint is entered <br> If I am the owner of the profile <br> I can send updated data to the profiles/id through a POST request <br> a response with code 200 and the updated data in JSON format is returned|PASS|
|Update own profile|As a developer <br> When the /profiles/id endpoint is entered <br> If I am not the owner of the profile <br> I cannot send updated data to the profiles/id through a POST request <br>If I try, a response with code 403 and and error message in JSON format is returned|PASS|


## Search and Filter Comments
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Filter By BlogPost||Pass|

## Search and Filter BlogPosts
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Filter By Category||Pass|
|Filter by Follower|||
|Filter by Author|||

## Search and Filter Profiles
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Filter By Follower||Pass|
|Filter by Following|||