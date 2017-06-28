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
    ELIGIBLE_NATIONS = (
        ('ALL', 'All'),
        ('INDIA', 'India'),
    )

    # scholarship data
    scholarship_name = models.CharField(max_length=1000)
    iitg_scholarship = models.CharField(max_length=1, choices=IITG_SCHOLARSHIP, default='N')
    maximum_income_annual = models.PositiveIntegerField(blank=True, null=True)
    maximum_income_monthly = models.PositiveIntegerField(blank=True, null=True)
    maximum_lump_sum_or_installments = models.PositiveIntegerField(blank=True, null=True)
    minimum_percent = models.PositiveIntegerField(blank=True, null=True)
    minimum_cpi = models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)
    minimum_disability_percent = models.PositiveIntegerField(blank=True, null=True)
    eligible_nations = models.CharField(max_length=20, choices=ELIGIBLE_NATIONS, default='ALL')
    scholarship_link = models.URLField(blank=True)

    # stages of education eligible for scholarship
    level_0001_hostellers = models.BooleanField(default=False)                  # for hostellers
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
    level_0001_day_scholars = models.BooleanField(default=False)                # for day scholars
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
    level_ug = models.BooleanField(default=False)                               # higher education
    level_pg = models.BooleanField(default=False)
    level_mphil = models.BooleanField(default=False)
    level_phd = models.BooleanField(default=False)

    # extra
    level_a1 = models.BooleanField(default=False)
    level_a2 = models.BooleanField(default=False)
    level_a3 = models.BooleanField(default=False)
    level_a4 = models.BooleanField(default=False)
    level_a5 = models.BooleanField(default=False)

    # religions eligible for scholarship
    hinduism = models.BooleanField(default=True)
    islam = models.BooleanField(default=True)
    christianity = models.BooleanField(default=True)
    sikhism = models.BooleanField(default=True)
    buddhism = models.BooleanField(default=True)
    jainism = models.BooleanField(default=True)
    zoroastrianism = models.BooleanField(default=True)
    other_religions = models.BooleanField(default=True)

    # category
    oc = models.BooleanField(default=True)
    sc = models.BooleanField(default=True)
    st = models.BooleanField(default=True)
    pwd = models.BooleanField(default=True)
    obc = models.BooleanField(default=True)

    # workers
    beedi = models.BooleanField(default=True)
    cine = models.BooleanField(default=True)
    iomc = models.BooleanField(default=True)
    lsdm = models.BooleanField(default=True)



'''
table that contains profile of the user.
'''
class Person(models.Model):
    # choices
    GENDER = (
        ('E', '-EMPTY-'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O','Other'),
    )
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    CATEGORY = (
        ('E', '-EMPTY-'),
        ('GEN','General'),
        ('SC','Scheduled Class'),
        ('ST','Scheduled Tribe'),
        ('PWD','Person With Disability'),
        ('OBC', 'Other Backward Class'),
    )
    EDUCATION = (
        ('E', '-EMPTY-'),
        ('L0001', 'Class I'),
        ('L0002', 'Class II'),
        ('L0003', 'Class III'),
        ('L0004', 'Class IV'),
        ('L0005', 'Class V'),
        ('L0006', 'Class VI'),
        ('L0007', 'Class VII'),
        ('L0008', 'Class VIII'),
        ('L0009', 'Class IX'),
        ('L0010', 'Class X'),
        ('L0011', 'Class XI'),
        ('L0012', 'Class XII'),
        ('UG', 'Under Graduate'),
        ('PG', 'Post Graduate'),
        ('MPHIL', 'M.Phil'),
        ('PHD', 'Ph.D'),
    )
    CITIZEN_INDIA = (
        ('E', '-EMPTY-'),
        ('Y','Yes'),
        ('N','No'),
    )
    RELIGION = (
        ('E', '-EMPTY-'),
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
        ('E', '-EMPTY-'),
        ('H', 'Hosteller'),
        ('D', 'Day Scholar'),
    )

    # website private data
    gmail_id = models.CharField(max_length=50, primary_key=True)
    IITG_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')

    # user's scholarship list
    marked_scholarships = models.ManyToManyField(Scholarship)

    # user data
    person_name = models.CharField(max_length=100, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='E')
    family_income = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default='E')
    education = models.CharField(max_length=5, choices=EDUCATION, default='E')
    current_cpi = models.DecimalField(null=True, decimal_places=2, max_digits=4, blank=True)
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='E')
    religion = models.CharField(max_length=1, choices=RELIGION, default='E')
    student_type = models.CharField(max_length=1, choices=STUDENT_TYPE, default='E')


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
        fields = ['person_name', 'birth_date', 'gender', 'family_income', 'category', 'education', 'current_cpi', 'citizen_india', 'religion', 'student_type']
