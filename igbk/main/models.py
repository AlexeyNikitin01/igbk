from django.db import models

from django.contrib.auth.models import User


class TextToCreateImg(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client', blank=True)
    created_date = models.DateField(auto_now_add=True)
    gender = models.TextField(max_length=50)
    skin_color = models.TextField(max_length=50)
    age = models.TextField(max_length=50)
    hair = models.TextField(max_length=50)
    eyes = models.TextField(max_length=50)
    eyebrows = models.TextField(max_length=50)
    jaw = models.TextField(max_length=50)
    nose = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.client} && date {self.created_date}'

    class Meta:
        verbose_name = 'keywords'
        verbose_name_plural = 'keywords'
        ordering = ['-created_date']


class UploadGenerateImageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.ForeignKey(TextToCreateImg, on_delete=models.CASCADE)
    generate_img_by_user = models.ImageField(upload_to='', blank=False)
