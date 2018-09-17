from django.db import models
from django.contrib.auth.models import User
from . import Venue
from datetime import datetime


class Comment(models.Model):
    venue = models.ForeignKey('studywhereapp.Venue', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    class Meta:
        db_table = "comments"