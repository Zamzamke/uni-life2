from django.db import models
from django.contrib.auth.models import User

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Opportunity(models.Model):
    CATEGORY_CHOICES = (
        ('job', 'Job'),
        ('internship', 'Internship'),
        ('scholarship', 'Scholarship'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    deadline = models.DateField()
    verified = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
