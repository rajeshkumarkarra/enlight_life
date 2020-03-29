from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=5000)
    message = models.TextField()
    
    def __str__(self):
        return self.email
