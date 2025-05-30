from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog-list"),
    path("post/<slug:slug>/", views.BlogPostDetailView.as_view(), name="blog-post-detail"),


]