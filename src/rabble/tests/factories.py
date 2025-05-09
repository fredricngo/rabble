import string

import factory
from factory import Sequence, Faker, SubFactory
from factory.django import DjangoModelFactory
from rabble.models import User, Community, SubRabble, Post, Comment 

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    
    username = Sequence(lambda n: f"user{n}")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    email = Faker("email")
    biography = Faker("text", max_nb_chars=200)
    # profile_picture = Faker("image_url")
    interests = Faker("text", max_nb_chars=100)


class CommunityFactory(DjangoModelFactory):
    class Meta:
        model = Community
    
    community_name = Sequence(lambda n: f"community{n}")

class SubRabbleFactory(DjangoModelFactory):
    class Meta:
        model = SubRabble
    
    subrabble_name = Sequence(lambda n: f"subrabble{n}")
    community_id = SubFactory(CommunityFactory)
    description = Faker("text", max_nb_chars=200)
    is_private = Faker("boolean")

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    
    post_title = Sequence(lambda n: f"Post Title {n}")
    post_body = Faker("text", max_nb_chars=500)
    comment_count = Faker("random_int", min=0, max=100)
    author = SubFactory(UserFactory)
    like_count = Faker("random_int", min=0, max=100)
    is_anon = Faker("boolean")
    subrabble_id = SubFactory(SubRabbleFactory)



class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    body = Faker("text", max_nb_chars=200)
    publisher = SubFactory(UserFactory)
    post = SubFactory(PostFactory)
    like_count = Faker("random_int", min=0, max=100)
    comment_count = Faker("random_int", min=0, max=100)

    #should be wary of the fact that the timestamp is set to the current time when the object is created
    timestamp = Faker("date_time")

    @factory.post_generation 
    def set_username(self, create, extracted, **kwargs):
        if extracted: 
            self.username = extracted

