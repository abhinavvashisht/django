from django.db import models

# Create your models here.

class Announcements(models.Model):
    title = models.CharField(  verbose_name='Announcement Title' , max_length=100)
    file = models.FileField( verbose_name='Upload File' ,upload_to='announcements', max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.title