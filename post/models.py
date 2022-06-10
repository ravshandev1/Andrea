from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TYPE = (
    (0, 'Fashion'),
    (1, 'Travel'),
)


class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.IntegerField(choices=TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    author_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='author')
    author_commit = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='comment', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
