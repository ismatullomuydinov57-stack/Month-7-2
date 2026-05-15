from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Name: {self.name} Pk: {self.pk}"

class Advertisement(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True,
                             validators=[FileExtensionValidator(['mp4', 'avi'], 'Faqat mp4 va avi formatlarga ruhsat')])
    category=models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Name: {self.title} Pk: {self.pk}"

class Comment(models.Model):
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    ad=models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"Name: {self.text} Pk: {self.pk}"

class AdLike(models.Model):
    ad=models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ad.name



