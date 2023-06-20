from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

from django.contrib.auth.models import (BaseUserManager)

# book_types = (
#   ("Action and Adventure", "Action and Adventure"),
#     ("Classics", "Classics"),
#     ("Comic Book or Graphic Novel","Comic Book or Graphic Novel"),
#     ("Detective and Mystery","Detective and Mystery")
#     ("Fantasy","Fantasy"),
#     ("Historical Fiction","Historical Fiction"),
#     ("Horror","Horror")
# )


class UserManager(BaseUserManager):
    def create_user(self, email,  username, password=None,**extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
,
            username=username,
            **extra_fields

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('account_status', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError((
                'Super user must have is_staff'
            ))

        return self.create_user(email,username,password,**extra_fields)


class User(AbstractUser):
    account_status= models.BooleanField(default=True)
    profile_img=models.ImageField('image',null=True,blank=True,upload_to='profile',validators=[FileExtensionValidator(['png','jpg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]



# class Author(AbstractUser):
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email
    
class Author(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=5)
    birth_place=models.CharField(max_length=100)
    birth_date=models.DateField()
    death_date=models.DateField()
    country=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    book_price=models.CharField(max_length=10)
    book_language=models.CharField(max_length=20)
    book_type=models.CharField(max_length=50)
    publish_date=models.DateField()
    book_image=models.ImageField('image',null=True,blank=True,upload_to='book',validators=[FileExtensionValidator(['png','jpg'])])
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    book_status=models.BooleanField(default=True)
    



    def __str__(self):
        return self.book_name