from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('admin', 'Admin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    course = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.role}"
