from django.db import models
from django.forms import ModelForm

# Create your models here.


'''
table that contains scholarships and their details.
'''


class Scholarship(models.Model):
    scholarship_name = models.CharField(max_length=1000)
    IITG_SCHOLARSHIP = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    iitg_scholarship = models.CharField(max_length=1, choices=IITG_SCHOLARSHIP, default='N')
    '''minimum_cpi = models.DecimalField(max_digits=4, decimal_places=2, default='')'''

    def __str__(self):
        return self.scholarship_name
'''
table that contains details of the user.
'''


class Person(models.Model):
    person_name = models.CharField(max_length=100, null=True)
    gmail_id = models.CharField(max_length=50, primary_key=True)
    birth_date = models.DateField(null=True)
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
    family_income = models.IntegerField(default=0)
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
    current_cpi = models.DecimalField(default=0.00, decimal_places=2,max_digits=4)
    CITIZEN_INDIA = (
        ('Y','Yes'),
        ('N','No'),
    )
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='N')


    def __str__(self):
        return self.person_name + '-' + self.gender
    marked_scholarships = models.ManyToManyField(Scholarship)

'''
form for Person class
'''
class PersonForm(ModelForm):
    class Meta:
        model = Person

        # fields in Person class except 'IITG_student', 'gmail_id' and 'marked_scholarships' can be present
        fields = ('person_name', 'birth_date', 'gender', 'family_income', 'category', 'programme', 'current_cpi', 'citizen_india')
