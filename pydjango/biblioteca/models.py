from django.db import models
import uuid


class Book(models.Model):

    id=models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    code=models.CharField(max_length=255,unique=True)
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    amount=models.IntegerField()



class Borrow(models.Model):

    id=models.UUIDField(default=uuid.uuid4,editable=False, unique=True,primary_key=True)
    date_issue=models.DateTimeField(auto_now_add=True, null=True)
    date_devolution=models.DateTimeField(null=True,blank=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    user_email=models.CharField(max_length=255)

