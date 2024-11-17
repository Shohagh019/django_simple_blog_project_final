from django.shortcuts import render
from posts.models import Post
# Create your views here.
def home(request):
    data = Post.objects.all()
    return render(request, 'index.html', {'data': data})