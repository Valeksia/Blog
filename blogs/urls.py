from django.urls import path, include
from blogs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/create_post/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('blogs/blog/', views.blog_view, name='blog'),
    path('users/', include('users.urls')),

]

app_name = 'blogs'