from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{}: {}'.format(self.pk, self.name)

class Article(models.Model):
    user = models.ForeignKey(User, related_name='articles')
    title = models.CharField(max_length=1024)
    body = models.TextField()

    def __str__(self):
        return self.title
