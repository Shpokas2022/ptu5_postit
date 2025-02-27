from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Post(models.Model):
    title = models.CharField(_("title"), max_length=50)
    body = models.TextField(_("body"))
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='post',
    )
    image = models.ImageField(_('image'), upload_to='user_images/', blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

def __str__(self):
    return _("{title} by {user} posted at {created_at}").format(
        title=self.title,
        user=self.user,
        created_at=self.created_at,
    )

class Meta:
    ordering = ('-created_at',)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField(_('body'), max_length=10000)
    user = models.ForeignKey(
        User, 
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='comments',
    )

    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return _("Comment on {post_id} by {user} at {created_at}").format(
            post_id=self.post.id,
            user = self.user,
            created_at=self.created_at
        )

# Like-u lentele
class PostLike(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_("user"),
        on_delete=models.CASCADE,
        related_name='post_likes',
    )
    post = models.ForeignKey(
        Post,
        verbose_name=_('post'),
        on_delete=models.CASCADE,
        related_name='post_likes'
    )

    def __str__(self) -> str:
        return f"{self.user} likes {self.post}"