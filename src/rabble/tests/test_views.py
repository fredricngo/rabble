import pytest
from django.urls import reverse
from django.core.management import call_command
from rabble.models import User, Community, SubRabble, Post
from rabble.forms import PostForm
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory


@pytest.mark.django_db
def test_index_view(client):
    # Create and log in a user
    user = UserFactory()
    client.force_login(user)
    #we need to create a default community for the index view to work
    default_community = CommunityFactory(community_name="default")
    subrabbles = SubRabbleFactory.create_batch(5) #Create 5 subrabble instances
    #subrabbles need to be associated with the default community
    for subrabble in subrabbles:
        subrabble.community_id = default_community
        subrabble.save()
    response = client.get(reverse("index"))

    assert "subrabbles" in response.context
    assert len(response.context["subrabbles"]) == len(subrabbles)
    assert response.status_code == 200
    
    html = response.content.decode()
    for subrabble in subrabbles:
        assert subrabble.subrabble_name in html


@pytest.mark.django_db
def test_subrabble_detail_view(client):
    # Create and log in a user
    user = UserFactory()
    client.force_login(user)
    #Generates a fake subRabble, at least five posts in the subRabble, where
    #each post has at least one comment and verifies that the details view 
    #correctly displays all the posts and numbers of comments

    #we have to createa a fake subRabble, and not use the cs-courses one specifically

    subrabble = SubRabbleFactory(subrabble_name="test_subrabble")
    posts = PostFactory.create_batch(5, subrabble_id=subrabble)

    #create at least one comment for each post
    for post in posts:
        post.comment_count = 1
        post.save()
    
    response = client.get(reverse("subrabble-detail", args=[subrabble.subrabble_name]))
    assert response.status_code == 200
    assert "subrabble" in response.context
    assert "posts" in response.context
    assert response.context["subrabble"] == subrabble
    assert len(response.context["posts"]) == len(posts)

    html = response.content.decode()
    for post in posts:
        assert post.post_title in html
        assert str(post.comment_count) in html
        assert str(post.author) in html

    
@pytest.mark.django_db
def test_post_create_view(client):
    # Create and log in a user
    user = UserFactory()
    client.force_login(user)
    #emulates submission of creating a post
    #verifies that pos was created 
    subrabble = SubRabbleFactory(subrabble_name="test_subrabble")
    data = {
        'post_title': "Test Post",
        'post_body': "This is a test post.",
        'comment_count': 0,
        'author': user.id,
        'subrabble_id': subrabble.id,
    }

    response = client.post(reverse("post-create", args=[subrabble.subrabble_name]), data)

    assert response.status_code == 302  # expects redirect
    post = Post.objects.latest('id')
    assert post.post_title == data['post_title']
    assert post.post_body == data['post_body']
    assert post.comment_count == data['comment_count']
    assert post.author == user
    assert post.subrabble_id == subrabble
