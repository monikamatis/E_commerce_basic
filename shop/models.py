from django.db import models


class Customer(models.Model):
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
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def __str__(self):
        return f'Customer {self.id}: {self.first_name} {self.last_name}'
