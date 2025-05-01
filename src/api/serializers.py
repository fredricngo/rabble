from rest_framework import serializers 
from rabble.models import *

class SubRabbleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubRabble
        fields = ['id', 'subrabble_name', 'community_id', 'description', 'is_private']

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Post 
        fields = ['post_title', 'post_body', 'comment_count', 'author', 'like_count', 
                  'timestamp', 'is_anon', 'subrabble_id', 'reactions']
        
