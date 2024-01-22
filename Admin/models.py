from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    location = models.CharField(max_length=255)
    website = models.URLField(max_length=255)

    def __str__(self):
        return self.company_name

class Job(models.Model):
    job_position = models.CharField(max_length=255)
    job_description = models.TextField()
    closing_date = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.job_position

    
