#from django.shortcuts import render
#from .models import Post
#
#def post_list(request):
#    posts = Post.objects.all()
#    return render(request, "post_list.html", {"posts": posts})

#from django.views.generic import ListView
#from .models import Post

#class PostList(ListView):
#    model = Post
#    template_name = "post_list.html"


from django.shortcuts import render, get_object_or_404  # new
from .models import Post 

def post_list(request): 
    posts = Post.objects.all() 
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, pk):  # new 
    post = get_object_or_404(Post, pk=pk) 
    return render(request, "post_detail.html", {"post": post})