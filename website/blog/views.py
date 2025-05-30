from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from website.blog.models import BlogPost, Category, Tag, Comment
from django.utils.text import slugify
from django.utils import timezone


class BlogListView(ListView):
    """
    Render the blog list view.
    """
    model = BlogPost
    context_object_name = "blog_posts"
    paginate_by = 10  # Number of posts per page
    ordering = ['-published_at']  # Order by published date, most recent first

    template_name = "website/blog/blog_list.html"
    extra_context = {
        "title": "Blog List",
        "description": "Welcome to the blog list page.",
    }

class BlogPostDetailView(DetailView):
    """
    Render the blog post detail view.
    """
    model = BlogPost
    context_object_name = "blog_post"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    template_name = "website/blog/blog_post_detail.html"
    extra_context = {
        "title": "Blog Post Detail",
        "description": "Detailed view of the blog post.",
    }