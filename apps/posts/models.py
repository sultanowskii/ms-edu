from django.db import models


class Post(models.Model):
    title = models.TextField(max_length=64)
    text = models.TextField(max_length=1024)
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)

