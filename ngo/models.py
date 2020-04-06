from django.db import models

# Create your models here.
# class for dynamic content displyed in index.htm
class Fundraise(models.Model):
    #properties
    
    dis= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    goal= models.FloatField()
    raised= models.FloatField()
    # if skill count True then only shows the skill bar in index.html
    skillcount= models.BooleanField(default=False)

