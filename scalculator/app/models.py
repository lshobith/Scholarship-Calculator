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
        ('Y', 'yes')
        ('N', 'no')
    )
    marked_scholarships = models.ManyToManyField(Scholarship)
