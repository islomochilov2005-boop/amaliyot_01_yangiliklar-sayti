from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Kategoriyalar"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriyalar"


class Article(models.Model):
    """Maqolalar"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    summary = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True)

    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Maqolalar"
        ordering = ['-created_at']


class Contact(models.Model):
    """Bog'lanish xabarlari"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name_plural = "Xabarlar"
        ordering = ['-created_at']