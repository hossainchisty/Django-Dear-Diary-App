from django.db import models

# Create your models here.
class Diary(models.Model):
    text = models.TextField(null=True,blank=True)
    data_created = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-data_created',)
        verbose_name_plural = 'Diary'