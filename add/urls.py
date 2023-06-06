from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='add-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='add-detail'),
    path('about/', views.about, name='add-about'),
]
