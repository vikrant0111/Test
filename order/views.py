from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request,
                  'order/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='publish',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'order/post/detail.html',
                  {'post': post})


def post_share(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status='published', )
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

        else:
            form = EmailPostForm()
        return render(request,
                      'order/post/share.html',
                      {'post': post,
                       'form': form})
