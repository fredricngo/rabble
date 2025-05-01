from django.urls import path 
from . import views 

urlpatterns = [
    path('subrabbles/', views.subrabble_list, name='api-subrabble-list'),
    path('subrabbles/!<str:identifier>/', views.subrabble_detail, name='api-subrabble-detail'),
    path('subrabbles/!<str:identifier>/posts/', views.SubrabblePostList.as_view(), name='api-subrabble-posts'),
    path('subrabbles/!<str:identifier>/posts/<int:pk>/', 
         views.SubrabblePostDetail.as_view(), 
         name='api-subrabble-post-detail'),
]