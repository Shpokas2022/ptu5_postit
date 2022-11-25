from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path('post/<int:pk>/', views.PostDetail.as_view()),
]
