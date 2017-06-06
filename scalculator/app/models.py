from django.db import models

# Create your models here.


'''
table that contains scholarships and their details.
'''


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=1000)
    '''minimum_cpi = models.DecimalField(max_digits=4, decimal_places=2, default='')'''

    def __str__(self):
        return self.scholarship_name
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
        ('O','Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default='')
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    IITG_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')
    family_income = models.IntegerField(default="")
    CATEGORY = (
        ('GEN','General'),
        ('SC','Scheduled Class'),
        ('ST','Scheduled Tribe'),
        ('PWD','Person With Disability'),
        ('OBC', 'Other Backward Class'),
    )
    category = models.CharField(max_length=3, choices=CATEGORY, default='GEN')
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
    programme = models.CharField(max_length=3, choices=PROGRAMME, default='P')
    current_cpi = models.DecimalField(default='', decimal_places=2,max_digits=4)
    CITIZEN_INDIA = (
        ('Y','Yes'),
        ('N','No'),
    )
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='N')


    def __str__(self):
        return self.person_name + '-' + self.gender
    marked_scholarships = models.ManyToManyField(Scholarship)
