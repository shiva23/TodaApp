from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_list(request):
	queryset = Post.objects.all()
	query = request.GET.get("q")
	if query:
		queryset = queryset.filter(Q(tags__icontains=query) | Q(bookmarks__icontains=query))

	context= {"obj_list": queryset , "tags":"List"}

	return render(request, "index.html", context)



def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Added!")
	context = {"form":form }
	return render(request, "form_page.html", context)




def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully Saved!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context= {"tags": instance.tags , "instance":instance, "form":form}
	return render(request, "form_page.html", context)




def post_delete(request, id=None):
	instance = Post.objects.get(id=id)
	instance.delete()
	return redirect("posts:list")




def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)	
	context= {"tags": instance.tags , "instance":instance,}
	return render(request, "details_page.html", context)