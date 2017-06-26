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
    SCHOLARSHIP_FOR_DISABLED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    ELIGIBLE_NATIONS = (
        ('ALL', 'All'),
        ('INDIA', 'India'),
    )

    # scholarship data
    scholarship_name = models.CharField(max_length=1000)
    maximum_income_annual = models.PositiveIntegerField(blank=True)
    maximum_income_monthly = models.PositiveIntegerField(blank=True)
    minimum_percent = models.PositiveIntegerField(blank=True)
    minimum_cpi = models.DecimalField(blank=True, decimal_places=2, max_digits=4)
    iitg_scholarship = models.CharField(max_length=1, choices=IITG_SCHOLARSHIP, default='N')
    scholarship_for_disabled = models.CharField(max_length=1, choices=SCHOLARSHIP_FOR_DISABLED, default='N')
    minimum_disability_percent = models.PositiveIntegerField(blank=True)
    eligible_nations = models.CharField(max_length=20, choices=ELIGIBLE_NATIONS, default='ALL')
    #scholarship_link = models.URLField()

    # stages of education eligible for scholarship
    # for hostellers
    level_0001_hostellers = models.BooleanField(default=False)
    level_0002_hostellers = models.BooleanField(default=False)
    level_0003_hostellers = models.BooleanField(default=False)
    level_0004_hostellers = models.BooleanField(default=False)
    level_0005_hostellers = models.BooleanField(default=False)
    level_0006_hostellers = models.BooleanField(default=False)
    level_0007_hostellers = models.BooleanField(default=False)
    level_0008_hostellers = models.BooleanField(default=False)
    level_0009_hostellers = models.BooleanField(default=False)
    level_0010_hostellers = models.BooleanField(default=False)
    level_0011_hostellers = models.BooleanField(default=False)
    level_0012_hostellers = models.BooleanField(default=False)
    # for day scholars
    level_0001_day_scholars = models.BooleanField(default=False)
    level_0002_day_scholars = models.BooleanField(default=False)
    level_0003_day_scholars = models.BooleanField(default=False)
    level_0004_day_scholars = models.BooleanField(default=False)
    level_0005_day_scholars = models.BooleanField(default=False)
    level_0006_day_scholars = models.BooleanField(default=False)
    level_0007_day_scholars = models.BooleanField(default=False)
    level_0008_day_scholars = models.BooleanField(default=False)
    level_0009_day_scholars = models.BooleanField(default=False)
    level_0010_day_scholars = models.BooleanField(default=False)
    level_0011_day_scholars = models.BooleanField(default=False)
    level_0012_day_scholars = models.BooleanField(default=False)

    # religions eligible for scholarship
    hinduism = models.BooleanField(default=True)
    islam = models.BooleanField(default=True)
    christianity = models.BooleanField(default=True)
    sikhism = models.BooleanField(default=True)
    buddhism = models.BooleanField(default=True)
    jainism = models.BooleanField(default=True)
    zoroastrianism = models.BooleanField(default=True)
    other_religions = models.BooleanField(default=True)


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
    RELIGION = (
        ('H', 'Hinduism'),
        ('I', 'Islam'),
        ('C', 'Christianity'),
        ('S', 'Sikhism'),
        ('B', 'Buddhism'),
        ('J', 'Jainism'),
        ('Z', 'Zoroastrianism'),
        ('O', 'Others'),
    )
    STUDENT_TYPE = (
        ('H', 'Hosteller'),
        ('D', 'Day Scholar'),
    )

    # website private data
    gmail_id = models.CharField(max_length=50, primary_key=True)
    IITG_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')

    # user's scholarship list
    marked_scholarships = models.ManyToManyField(Scholarship)

    # user data
    person_name = models.CharField(max_length=100, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    family_income = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default='GEN') #
    programme = models.CharField(max_length=3, choices=PROGRAMME, default='P') #
    current_cpi = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='N')
    religion = models.CharField(max_length=1, choices=RELIGION, null=True)
    student_type = models.CharField(max_length=1, choices=STUDENT_TYPE, null=True)


'''
form for Person class.
this is not a database.
this form is used for editing the database.
'''
class PersonForm(ModelForm):
    class Meta:
        # the model form is based on Person.
        model = Person

        # Should not contain 'IITG_student', 'gmail_id' and 'marked_scholarships'.
        fields = ['person_name', 'birth_date', 'gender', 'family_income', 'category', 'programme', 'current_cpi', 'citizen_india', 'religion', 'student_type']
