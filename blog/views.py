from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

from blog.models import Post

# Create your views here.

class PostLV(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 4


class PostDV(DetailView):
    model = Post


class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'mod_date'


class PostYAV(YearArchiveView):
    model = Post
    date_field = 'mod_date'
    make_object_list=True


class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'mod_date'
    month_format = '%m'


class PostDAV(DayArchiveView):
    model = Post
    date_field = 'mod_date'
    month_format = '%m'


class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'mod_date'


class CreatePost(CreateView):
    model = Post
    fields = ['title', 'content', 'pub_date',]
    template_name = 'blog/create_post.html'


class UpdatePost(UpdateView):
    model = Post
    fields = ['title', 'content', 'pub_date',]
    template_name = 'blog/update_post.html'


# class DeletePost(DeleteView):
#     model = Post
#     template_name = 'blog/delete_post.html'


def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('blog:post_list')
