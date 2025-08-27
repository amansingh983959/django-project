from django.shortcuts import render
from django.http  import HttpResponse
from blog.models import post
# Create your views here.

def blog_index(request):
    return render(request=request, template_name='blog_index.html')
def get_post(request):
    return render(request=request, template_name='blog_index.html')
def get_post(request):
    all_posts = post.objects.all()
    return render(request,'blog/post.html', context={'all_posts': all_posts})


def create_post(request):
    print("test",dir(request))
    title = request.POST.get('title_form')
    content = request.POST.get('content_form')

    post1=post()
    post1.title = title
    post1.content = content
    post1.save()
    
    new_post = post(title=title, content=content)
    new_post.save()
    return render(request=request, template_name='blog/post/newpost.html')