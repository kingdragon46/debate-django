from authentication.models import UserRoles
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from authentication.models import *

# Create your models here.


class Discussion(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    title = models.TextField()
    participant1 = models.ForeignKey(User, on_delete=models.SET_NULL , blank=True, null=True, related_name='pt1')
    p1like = models.IntegerField(_("P1 likes"), null=True, blank=True, default=0)
    p1dislike = models.IntegerField(_("P1 likes"), null=True, blank=True, default=0)
    participant2 = models.ForeignKey(User, on_delete=models.SET_NULL , blank=True, null=True, related_name='pt2')
    p2like = models.IntegerField(_("P2 likes"), null=True, blank=True, default=0)
    p2dislike = models.IntegerField(_("P2 likes"), null=True, blank=True, default=0)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL , blank=True, null=True, related_name='winr')
    loser = models.ForeignKey(User, on_delete=models.SET_NULL , blank=True, null=True, related_name='loser')
    is_closed = models.BooleanField(_("Closed"), default=False)
    is_deleted = models.BooleanField(_("Deleted"), default=False)

    def __str__(self):
        return f'{self.title}' or ''


type_choices=(
    ("1","For Motion"),
    ("2","Against Motion"),
)

class Claim(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    ctype = models.CharField(_('Claim Type'), choices=type_choices , max_length=50, null=True)
    text = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    for_discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='discs')
    is_deleted = models.BooleanField(_("Deleted"), default=False)

    suggested = models.IntegerField(default=0)

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    for_claim = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(_("Deleted"), default=False)


class Vote(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    for_claim = models.ForeignKey(Claim, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()