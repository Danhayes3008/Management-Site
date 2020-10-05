from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ('Complete', 'Complete'),
        ('To Do', 'To Do')
    )
    name = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='To Do')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=User)

    def __str__(self):
        return self.user.username