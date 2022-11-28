from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path("post/<int:pk>/like/", views.PostLikeCreate.as_view()),
    path('post/<int:pk>/comment', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentDetail.as_view()),
    path('signup/', views.UserCreate.as_view())
]
