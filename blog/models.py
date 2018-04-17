from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):

    #Fields
    title = models.CharField(max_length=250, primary_key=True)
    text = models.TextField()
    author = models.CharField(max_length=100, default='Zachary Faddis')
    published = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = [ 'published' ]

    def get_absolute_url(self):
        return reverse('article' , args=[self.title])

    
    def __str__(self):
        return self.title

    def get_summary(self):
        sumLen = len(self.text)
        if sumLen > 250:
            sumLen = 250
        return self.text[:sumLen]
