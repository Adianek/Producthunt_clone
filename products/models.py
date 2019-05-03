from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=40)
    url = models.TextField()
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date_better(self):
        return self.pub_date.strftime('%b %e %Y')

# hunter
