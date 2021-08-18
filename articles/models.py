from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add = True)
    # in add thumbnail
    # addmin author
    def __str__(self):
        return self.title

    def snippet (self) :
        return self.body[0:50] + '...'
