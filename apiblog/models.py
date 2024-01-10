from django.db import models

class TodoApp(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    time_create = models.DateTimeField(auto_now=True)
    is_complected = models.BooleanField(default=False)

    def __str__(self):
        return self.title


