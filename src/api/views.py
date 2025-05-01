from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rabble.models import *
from .serializers import *
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def subrabble_list(request):
    if request.method == 'GET': 
        subrabbles = SubRabble.objects.all() 
        serializer = SubRabbleSerializer(subrabbles, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def subrabble_detail(request, identifier):
    try: 
        subrabble = SubRabble.objects.get(subrabble_name=identifier)
    except SubRabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': 
        serializer = SubRabbleSerializer(subrabble)
        return Response(serializer.data)
    
class SubrabblePostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        subrabble = get_object_or_404(SubRabble, subrabble_name=self.kwargs['identifier'])
        return Post.objects.filter(subrabble_id=subrabble)

    def perform_create(self, serializer):
        subrabble = get_object_or_404(SubRabble, subrabble_name=self.kwargs['identifier'])
        serializer.save(subrabble_id=subrabble)
    
class SubrabblePostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    
    def get_object(self):
        subrabble = get_object_or_404(
            SubRabble, 
            subrabble_name=self.kwargs['identifier']
        )
        return get_object_or_404(
            Post, 
            pk=self.kwargs['pk'], 
            subrabble_id=subrabble
        )