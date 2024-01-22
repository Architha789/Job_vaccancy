from django.db import models
from django.contrib.auth.models import User
from Admin.models import Job


# Create your models here.
class AppliedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
     return f"{self.user.username}"
 