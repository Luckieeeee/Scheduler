from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView, 
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='add-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='add-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='add-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='add-update'),
    path('post/new/', PostCreateView.as_view(), name='add-create'),
    path('about/', views.about, name='add-about'),
]
