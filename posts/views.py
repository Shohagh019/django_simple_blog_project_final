from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
# @login_required
# def add_post(request):
#     if request.method == 'POST':
#         post_form = forms.postForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author = request.user # manually author setting
#             messages.success(request, 'Your post added successfully!')
#             post_form.save()
#             return redirect('add_post')
#     else:
#         post_form = forms.postForm()    
#     return render(request, 'post.html', {'form': post_form}) 
method_decorator(login_required, name= 'dispatch')
class CreatePost(CreateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post.html'
    success_url = reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user 
        # because when i add post i dont need to see ar add my own name.it will do automatically
        return super().form_valid(form)

# @login_required
# def edit_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     post_form = forms.postForm(instance=post)
#     if request.method == 'POST':
#         post_form = forms.postForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.instance.author = request.user # manually author setting
#             messages.success(request, 'Your post edited successfully!')
#             post_form.save()
#             return redirect('profile')   
#     return render(request, 'post.html', {'form': post_form})  
#       
method_decorator(login_required, name= 'dispatch')
class EditPost(UpdateView):
    model = models.Post
    form_class = forms.postForm
    template_name = 'post.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'
# @login_required
# def delete_post(request, id):
#     post = models.Post.objects.get(pk=id)
#     messages.success(request, 'Your post deleted successfully!')
#     post.delete()
#     return redirect('profile')
method_decorator(login_required, name= 'dispatch')
class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'