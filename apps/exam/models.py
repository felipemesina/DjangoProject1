from __future__ import unicode_literals
from django.db import models
import bcrypt


# Create your models here.
class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        if len(self.filter(username = post_data['username'])) > 0:
            user = self.filter(username = post_data['username'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('Invalid Email/Password')
        else:
            errors.append('Invalid Email/Password')

        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        if len(post_data['name']) < 3:
            errors.append('Username must be at least 3 characters')
        if len(post_data['username']) < 3:
            errors.append('Username must be at least 3 characters')
        if len(post_data['password']) < 8:
            errors.append('password must be at least 8 characters long')
        if post_data['password'] != post_data['confirm_password']:
            errors.append('passwords do not match')

        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name = post_data['name'],
                username = post_data['username'],
                password = hashed
            )
            return new_user
        return errors

class TravelManager(models.Manager):
    def validate_travel(self, post_data):
        errors = []
        if len(post_data['destination']) == 0:
            errors.append('Destination is required.')
        if len(post_data['desc']) == 0:
            errors.append('Description is required.')
        if len(post_data['date_from']) == 0:
            errors.append('Travel Date From field required.')
        if len(post_data['date_to']) == 0:
            errors.append('Travel Date To field required.')

        return errors


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.username

class Travel(models.Model):
    destination = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    user = models.ForeignKey(User, related_name="trip")
    booked_users = models.ManyToManyField(User, related_name="booked_trips")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()
