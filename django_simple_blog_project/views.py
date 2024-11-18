from django.shortcuts import render
from posts.models import Post
from categories.models import Category
from authors.models import Author
# Create your views here.
def home(request, category_slug=None):
    author = Author.objects.all()
    data = Post.objects.all()
    if category_slug is not  None:
        # category = Category.objects.get(slug=category_slug)
        data = Post.objects.filter(category__slug=category_slug)
    categories = Category.objects.all()
    return render(request, 'index.html', {'data': data, 'category': categories})