# Test Driven Development
To save space, only the descriptive test names are given.
## posts/ endpoint test cases

```
class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='password')
    
    def test_user_can_list_posts(self):

        
    def test_logged_in_user_can_create_post(self):


    def test_user_cant_post_if_not_logged_in(self):                



class PostDetailViewTests(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

    def test_can_retrieve_post_using_valid_id(self):


    def test_cannot_retrieve_post_with_invalid_id(self):


    def test_user_can_update_own_post(self):


    def test_user_cant_update_another_users_post(self):


    def test_user_can_delete_their_own_post(self):


    def test_user_cannot_delete_post_not_their_own(self):

```

## likes/ endpoint test cases

```

class TestLikeView(APITestCase):
    def setUp(self):
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

        blog_post_a = BlogPost.objects.get(id=1)
        blog_post_b = BlogPost.objects.get(id=2)

        Like.objects.create(owner=user_a, blog_post=blog_post_a)
        Like.objects.create(owner=user_a, blog_post=blog_post_b)
      
    def test_user_can_get_likes(self):


    def test_logged_in_user_can_like_post(self):


    def test_unauthenticated_user_cant_like_post(self):

    def test_user_can_delete_own_like(self):


    def test_user_cannot_delete_other_likes(self):


    def test_cant_have_duplicate_likes(self):
 

```

## comments/ endpoint test cases

```
class CommentViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='test_user', password='password')
        user_a = User.objects.create_user(username='user_a', password='pass')
        user_b = User.objects.create_user(username='user_b', password='pass')

        BlogPost.objects.create(author=user_a, title='Test Title A', body='A')
        BlogPost.objects.create(author=user_b, title='Test Title B', body='B')

    def test_view_all_comments(self):

        
    def test_can_create_comment_if_logged_in(self):


    def test_cannot_create_comment_if_anonymous(self):


    def test_user_can_update_their_own_comment(self):

    
    def test_user_cannot_update_comment_if_not_owner(self):


    def test_user_can_delete_their_own_comment(self):


    def test_user_cannot_delete_comment_if_not_owner(self):
   

```

## followers/ endpoint test cases
```
    def setUp(self):
        pass

    def test_get_all_followers(self):
        pass

    def test_follow_a_user(self):
        pass

    def test_cant_follow_if_not_logged_in(self):
        pass
      
    def test_cant_follow_user_twice(self):
        pass

```
