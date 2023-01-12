from django.db import models


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,
                                  help_text='First name.')
    last_name = models.CharField(max_length=100,
                                 help_text='Last name.')
    email = models.EmailField(max_length=100,
                              help_text='Please type in your email.')
    password = models.CharField(max_length=100,
                                default=None,
                                help_text='Minimum length 8 characters')
    phone = models.CharField(max_length=10,
                             help_text='Contact number')
    newsletter = models.BooleanField(default=True,
                                     help_text='Sign up for our newsletter')

    def register_customer(self):
        self.save()

    def if_exists(self):
        if Customers.objects.filter(email=self.email):
            return True
        else:
            return False

