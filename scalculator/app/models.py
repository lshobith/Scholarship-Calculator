from django.db import models
from django.forms import ModelForm


'''
table that contains scholarships and their details.
'''
class Scholarship(models.Model):
    # choices
    IITG_SCHOLARSHIP = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    # scholarship data
    scholarship_name = models.CharField(max_length=1000)
    maximum_income = models.PositiveIntegerField(default=0)
    iitg_scholarship = models.CharField(max_length=1, choices=IITG_SCHOLARSHIP, default='N')


'''
table that contains profile of the user.
'''
class Person(models.Model):
    # choices
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
    )
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
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
    CITIZEN_INDIA = (
        ('Y','Yes'),
        ('N','No'),
    )

    # website private data
    gmail_id = models.CharField(max_length=50, primary_key=True)
    IITG_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')

    # user's scholarship list
    marked_scholarships = models.ManyToManyField(Scholarship)

    # user data
    person_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='')
    family_income = models.IntegerField(default=0)
    category = models.CharField(max_length=3, choices=CATEGORY, default='GEN')
    programme = models.CharField(max_length=3, choices=PROGRAMME, default='P')
    current_cpi = models.DecimalField(default=0.00, decimal_places=2,max_digits=4)
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='N')


'''
form for Person class.
this is not a database.
this form is used for editing the database.
'''
class PersonForm(ModelForm):
    class Meta:
        # the model form is based on.
        model = Person

        # Should not contain 'IITG_student', 'gmail_id' and 'marked_scholarships'.
        fields = ('person_name', 'birth_date', 'gender', 'family_income', 'category', 'programme', 'current_cpi', 'citizen_india')
