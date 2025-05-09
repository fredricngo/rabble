import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient 
from rabble.models import User, Community, SubRabble, Post
from rabble.forms import PostForm
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory

@pytest.fixture 
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_subrabble_get(api_client):
    #Generates a fake subRabble
    #verifies that a GET request to /api/subrabbles/!<str:identifier> 
    #correctly returns info about the subRabble 
    subrabble = SubRabbleFactory(subrabble_name="test_subrabble")
    #create a user and log in
    user = UserFactory()
    api_client.force_authenticate(user=user)
    #create a community and associate it with the subrabble
    community = CommunityFactory(community_name="default")
    subrabble.community_id = community
    subrabble.save()

    #make a get request to subrabble 
    response = api_client.get(reverse("api-subrabble-detail", args=[subrabble.subrabble_name]))

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == subrabble.id 
    assert response.data["subrabble_name"] == subrabble.subrabble_name
    assert response.data["description"] == subrabble.description
    assert response.data["community_id"] == subrabble.community_id.id

@pytest.mark.django_db
def test_post_post(api_client):
    #sends a POST request to /api/subrabbles/!<str:identifier>/posts
    #verifies that the post was correctly created 

    #create a user and log in
    user = UserFactory()
    api_client.force_authenticate(user=user)
    # Create a community and associate it with the subrabble
    community = CommunityFactory(community_name="default")
    subrabble = SubRabbleFactory(subrabble_name="test_subrabble")
    subrabble.community_id = community
    subrabble.save()
    #ceate a post
    data = {
        "post_title": "Test Post",
        "post_body": "This is a test post.",
        "subrabble_id": subrabble.id,
        "author": user.id,
    }
    response = api_client.post(
        reverse("api-subrabble-posts", args=[subrabble.subrabble_name]),
        data=data)
    
    print(response.status_code)
    print(response.data)
    assert response.status_code == status.HTTP_201_CREATED

    #confirm the objects was created
    post = Post.objects.get(post_title="Test Post")
    assert post.post_title == data["post_title"]
    assert post.post_body == data["post_body"]
    assert post.subrabble_id.id == data["subrabble_id"]
    assert post.author.id == data["author"]


@pytest.mark.django_db
def test_post_patch(api_client): 
    #generates a fake post 
    #sends a PATCH request to /api/subrabbles/!<str:identifier>/posts/<int:pk>
    #verifies that the post was correctly updated

    #create a user and log in
    user = UserFactory()
    api_client.force_authenticate(user=user)
    #create a community and associate it with the subrabble
    community = CommunityFactory(community_name="default")
    subrabble = SubRabbleFactory(subrabble_name="test_subrabble")
    subrabble.community_id = community
    subrabble.save()
    #ceate a post
    post = PostFactory(subrabble_id=subrabble, author=user)
    data = {
        "post_title": "Updated Post Title",
        "post_body": "This is an updated test post.",
    }

    response = api_client.patch(
        reverse("api-subrabble-post-detail", args=[subrabble.subrabble_name, post.pk]),
        data=data,
    )
    assert response.status_code == status.HTTP_200_OK

    #Verify the course was updated on the database 
    post.refresh_from_db()
    assert post.post_title == data["post_title"]
    assert post.post_body == data["post_body"]



