from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Text')
    data = models.DateTimeField('Data publication')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'