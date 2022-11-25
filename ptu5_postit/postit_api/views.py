from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import models, serializers

class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    # importuojam4s permitions klases. Visi, kurie neprisijungę vartotojai negalės rašyti, tik skaityti
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.safe(user=self.request.user)


# darome delete metoda
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def delete(self, request, *args, **kwargs):
        post = models.Post.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(_('You cannot delete post not of your own.'))

    def put(self, request, *args, **kwargs):
        post = models.Post.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(_('You cannot delete post not of your own.'))


