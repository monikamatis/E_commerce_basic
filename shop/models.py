from django.db import models


# class Customer(models.Model):
#     id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=100,
#                                   help_text='First name.')
#     last_name = models.CharField(max_length=100,
#                                  help_text='Last name.')
#     email = models.EmailField(max_length=100,
#                               help_text='Please type in your email.')
#     password = models.CharField(max_length=100,
#                                 default=None,
#                                 help_text='Minimum length 8 characters')
#     phone = models.CharField(max_length=10,
#                              help_text='Contact number')
#     newsletter = models.BooleanField(default=True,
#                                      help_text='Sign up for our newsletter')
#
#     def register_customer(self):
#         self.save()
#
#     def if_exists(self):
#         if Customer.objects.filter(email=self.email):
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return f'Customer {self.id}: {self.first_name} {self.last_name}'
#

# Product catalog models Category and Product:
class Category(models.Model):
    """
    Create a 'Category' model for the product catalog.
    Field 'name' and unique 'slug' field.
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        """
        Defines ordering by the 'name' field
        and index on field 'name'.
        It also defines the correct singular and plural for the name of the class.
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),

        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        :return: descriptive title
        """
        return self.name


class Product(models.Model):
    """
    Create a 'Product' model of the product catalog.
    Create with the field 'category' one-to-many relationship with the 'Category' model.
    Fields 'name', 'slug', 'price', 'available' are required;
    fields 'created' and 'updated' are automatically filled with creating/modification date.
    Fields 'image' and 'description' are optional.
    """
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Define ordering on 'name' field.
        Also, define indexes on fields 'id', slug', 'name' and 'created'
        """
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['created']),
        ]

    def __str__(self):
        """
        :return: descriptive title
        """
        return self.name
