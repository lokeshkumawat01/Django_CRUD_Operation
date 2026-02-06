from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    # Link task to a specific user (One-to-Many relationship)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Set time on create

    def __str__(self):
        return self.title

    class Meta:
        # Orders tasks by completion status (incomplete first)
        ordering = ['completed']