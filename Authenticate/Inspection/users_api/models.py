from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):


    def create_user(self,email,name,role,password=None):

        if not email:
            raise ValueError('User Must have an Email Address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name,role=role)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,name,role,password):
        user=self.create_user(email,name,role,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email



class Packaging_line(models.Model):
    line_id=models.AutoField(primary_key=True)
    description=models.TextField(max_length=100)

    def __str__(self):
        return self.description+str(self.line_id)

class Line_control_details(models.Model):
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    line_id=models.ForeignKey(Packaging_line,on_delete=models.CASCADE)

    def __str__(self):
        return 'user:'+str(self.user_id)+' line:'+str(self.line_id)


class Batch_details(models.Model):
    test_id=models.AutoField(primary_key=True)
    start_dateTime=models.DateTimeField(auto_now_add=True)
    end_datetime=models.DateTimeField(auto_now=True)
    line_id=models.ForeignKey(Packaging_line,on_delete=models.CASCADE)
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.start_dateTime)+str(self.line_id)

class Batch_Test_results(models.Model):
    strip_id=models.AutoField(primary_key=True)
    result_status=models.CharField(max_length=20,default="valid")
    test_id=models.ForeignKey(Batch_details,on_delete=models.CASCADE)

    def __str__(self):
        return self.result_status




