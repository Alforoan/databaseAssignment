from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, db_index=True)
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)

class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    body = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)

class Follow(models.Model):
    following_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE, db_index=True)
    followed_user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(db_index=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, db_index=True)
    created_at = models.DateTimeField(db_index=True)

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, db_index=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, db_index=True)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images/')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)
    expires_at = models.DateTimeField(db_index=True)

class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    color = models.CharField(max_length=50)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)
