from django.views import generic
from django.shortcuts import render
from .models import Post

# Create your views here.
def splash(request):
    return render(request, 'splash.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
