from django.db import models

class Question(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField()
    qes = models.CharField(max_length=250)
    ans = models.CharField(max_length=400)
    answer_by = models.TextField()
    posted_date = models.DateField()
    picture = models.TextField()
    up_count = models.IntegerField()
    downvote_count = models.IntegerField()
