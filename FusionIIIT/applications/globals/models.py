# imports
from django.contrib.auth.models import User
from django.db import models

# Class definations:


# # Class for various choices on the enumerations
class Constants:
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    USER_CHOICES = (
        ('student', 'student'),
        ('staff', 'staff'),
        ('compounder', 'compounder'),
        ('faculty', 'faculty')
    )

    DESIGNATIONS = (
        ('academic', 'Academic Designation'),
        ('administrative', 'Administrative Designation')
    )

class Designation(models.Model):
    name = models.CharField(max_length=50, unique=True,blank=False, default='student')
    full_name = models.CharField(max_length=100, default='Computer Science and Engineering')

    type = models.CharField(max_length=30, default='academic', choices=Constants.DESIGNATIONS)

    def __str__(self):
        return self.name

class HoldsDesignation(models.Model):
    user = models.ForeignKey(User, related_name='holds_designations', on_delete=models.CASCADE)
    working = models.ForeignKey(User, related_name='current_designation')
    designation = models.ForeignKey(Designation, related_name='designees', on_delete=models.CASCADE)
    held_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.user.username, self.designation)

class DepartmentInfo(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ExtraInfo(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=2, choices=Constants.SEX_CHOICES, default='M')
    age = models.IntegerField(default=18)
    address = models.TextField(max_length=1000, default="")
    phone_no = models.BigIntegerField(default=0)
    user_type = models.CharField(max_length=20, choices=Constants.USER_CHOICES)
    # designation = models.ForeignKey(Designation, on_delete=models.CASCADE,
                                    # related_name='holds_designation', null=True)
    department = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    about_me = models.TextField(default='', max_length=1000, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.user.username)


# TODO : ADD additional staff related fields when needed
class Staff(models.Model):
    id = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)


# TODO : ADD additional employee related fields when needed
class Faculty(models.Model):
    id = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)
