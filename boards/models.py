from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=False, related_name='topics')
    starter = models.ForeignKey(User, on_delete=False, related_name='topics')

    def __str__(self):
        return self.board.name + ' : ' + self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=False, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=False, related_name='posts')
    updated_by = models.ForeignKey(User,
                                   null=True,
                                   on_delete=False,
                                   related_name='+')

    def __str__(self):
        return self.topic.subject + ' : ' + self.message


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    message = models.TextField(max_length=4000)

    def __str__(self):
        return self.full_name + ' : ' + self.message[:75]


class Student(models.Model):
    std_id = models.CharField(max_length=7, unique=True)
    name = models.CharField(max_length=200)
    attendance = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    ct1 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    ct2 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    ct3 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    ct4 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    ct = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    secA = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    secB = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    final300 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    final100 = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    gpa = models.DecimalField(decimal_places=2, max_digits=5)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return self.name+'('+self.std_id+')'