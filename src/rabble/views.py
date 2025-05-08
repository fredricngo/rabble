from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post, Community, SubRabble
from .forms import PostForm

def index(request):
    default_community = Community.objects.get(community_name="default")
    subrabbles = SubRabble.objects.filter(community_id=default_community)
    context = {"subrabbles": subrabbles,}
    return render(request, "rabble/index.html", context)

#when the index path is accessed, the function will render the rabble/index.html template with the context provided.

def profile(request):
    return render(request, "rabble/profile.html")

#when the profile path is accessed, this function will render the rabble/profile.html template.

def subrabble_detail(request, identifier):
    subrabble = SubRabble.objects.get(subrabble_name=identifier)
    context = {
        "subrabble": subrabble,
        "posts": subrabble.post_set.all()  # Get all posts for this subrabble
    }
    return render(request, "rabble/subrabble-detail.html", context)

def post_detail(request, identifier, pk):
    post = get_object_or_404(Post, pk=pk)
    subrabble = get_object_or_404(SubRabble, subrabble_name=identifier)
    
    context = {
        'post': post,
        'subrabble': subrabble,
    }
    return render(request, "rabble/post-detail.html", context)

@login_required
def post_create(request, identifier):
    subrabble = get_object_or_404(SubRabble, subrabble_name=identifier)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.subrabble_id = subrabble
            post.save()
            return redirect('post-detail', identifier=subrabble.subrabble_name, pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'rabble/post-form.html', {
        'form': form,
        'subrabble': subrabble
    })


def post_edit(request, identifier, pk):
    subrabble = get_object_or_404(SubRabble, subrabble_name=identifier)
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', identifier=subrabble.subrabble_name, pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, 'rabble/post-form.html', {
        'form': form,
        'subrabble': subrabble
    })