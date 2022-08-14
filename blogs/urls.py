from blogs.models import *
from django.urls import path
from blogs import views


urlpatterns = [
    path('home/',views.BlogList.as_view(),name='home'),
    path('create',views.Blog.as_view()),
    path('blog_detail/<int:pk>',views.Blogdetail.as_view(),name='detail'),
    path('catlist',views.CategoryList.as_view(),name='catergory'),
    path('cat/',views.Category.as_view(),name='detail'),
    path('comment/',views.CommentList.as_view(),name='comment'),
   
]

