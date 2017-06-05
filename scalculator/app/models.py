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
    family_income = models.IntegerField(max_length=30)
    CATEGORY = (
        ('GEN','General'),
        ('SC','Scheduled Class'),
        ('ST','Scheduled Tribe'),
        ('PWD','Person With Disability'),
        ('OBC', 'Other Backward Class'),
    )
    PROGRAMME = (
        ('P','Preparatory'),
        ('B1','B.Tech 1st Year'),
        ('B2','B.Tech 2nd Year'),
        ('B3','B.Tech 3rd Year'),
        ('B4','B.Tech 4th Year'),
        ('MA1','MA 1st Year'),
        ('MA2','MA 2nd Year'),
        ('MS1','MSc 1st Year'),
        ('MS2','MSc 2nd Year'),
    )
    current_cpi = models.IntegerField(max_length=5)
    CITIZEN_INDIA = (
        ('Y','Yes'),
        ('N','No'),
    )
    marked_scholarships = models.ManyToManyField(Scholarship)
