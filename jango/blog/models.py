from django.db import models

class user(models.Model):
    username = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} ({self.name})"

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    pub_date = models.DateTimeField("date published")
    modified_date = models.DateTimeField("date published")
    user = models.ForeignKey(user, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    