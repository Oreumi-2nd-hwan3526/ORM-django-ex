from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def read_Post_data(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def add_Post_data(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        published_date = request.POST['published_date']

        post = Post(title=title, content=content, published_date=published_date)
        post.save()
        return redirect('index')
    
    return render(request, "add_page.html")