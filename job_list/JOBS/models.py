# JOBS/models.py
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='job_images/', null=True, blank=True)

    def __str__(self):
        return self.title

