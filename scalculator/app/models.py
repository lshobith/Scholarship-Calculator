from django.db import models

# Create your models here.


'''
table that contains scholarships and their details.
'''
class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=1000)

'''
table that contains details of the user.
'''


class Person(models.Model):
    person_name = models.CharField(max_length=100)
    #gmail_id = models. TODO
    birth_date = models.DateField()
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    FAMILY_INCOME=(
        ('B15','Below Rs.1,50,000'),
        ('15T25','Rs. 1,50,000 to Rs. 2,50,000'),
        ('25T35','Rs. 2,50,000 to Rs. 3,50,000'),
        ('35T45','Rs. 3,50,000 to Rs. 4,50,000'),
        ('45A','Rs. 4,50,000 - Above'),
    )
    marked_scholarships = models.ManyToManyField(Scholarship)
