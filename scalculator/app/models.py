from django.db import models
from django.forms import ModelForm
from django import forms


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
    scholarship_link = models.URLField(blank=True)
    iitg_scholarship = models.CharField(max_length=1, choices=IITG_SCHOLARSHIP, default='N')
    maximum_income_annual = models.PositiveIntegerField(blank=True, null=True)
    maximum_income_monthly = models.PositiveIntegerField(blank=True, null=True)
    maximum_lump_sum_or_installments = models.PositiveIntegerField(blank=True, null=True)
    minimum_percent = models.PositiveIntegerField(blank=True, null=True)
    minimum_cpi = models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)
    minimum_disability_percent = models.PositiveIntegerField(blank=True, null=True)
    eligible_nations = models.CharField(max_length=20, choices=ELIGIBLE_NATIONS, default='ALL')

    male = models.BooleanField(default=True)
    female = models.BooleanField(default=True)

    # stages of education eligible for scholarship
    level_l0001 = models.BooleanField(default=False)
    level_l0002 = models.BooleanField(default=False)
    level_l0003 = models.BooleanField(default=False)
    level_l0004 = models.BooleanField(default=False)
    level_l0005 = models.BooleanField(default=False)
    level_l0006 = models.BooleanField(default=False)
    level_l0007 = models.BooleanField(default=False)
    level_l0008 = models.BooleanField(default=False)
    level_l0009 = models.BooleanField(default=False)
    level_l0010 = models.BooleanField(default=False)
    level_l0011 = models.BooleanField(default=False)
    level_l0012 = models.BooleanField(default=False)
    level_lug = models.BooleanField(default=False)
    level_lpg = models.BooleanField(default=False)
    level_lmphil = models.BooleanField(default=False)
    level_lphd = models.BooleanField(default=False)

    # extra
    level_post_matriculation = models.BooleanField(default=True)
    level_diploma_certificates = models.BooleanField(default=True)
    level_bachelors_degree = models.BooleanField(default=True)
    level_diploma_india = models.BooleanField(default=True)
    level_masters_degree = models.BooleanField(default=True)

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
    gen = models.BooleanField(default=True)
    sc = models.BooleanField(default=True)
    st = models.BooleanField(default=True)
    pwd = models.BooleanField(default=True)
    obc = models.BooleanField(default=True)

    # workers
    beedi = models.BooleanField(default=True)
    cine = models.BooleanField(default=True)
    iomc = models.BooleanField(default=True)
    lsdm = models.BooleanField(default=True)

    # armed
    armed = models.BooleanField(default=True)
    rifles = models.BooleanField(default=True)

    data_about = models.TextField(blank=True)

    def unique_id_collapse(self):
        return 'collapse' + str(self.id)

    def unique_id_save(self):
        return 'save' + str(self.id)

    def unique_id_remove(self):
        return 'remove' + str(self.id)

    def unique_id_badge(self):
        return 'badge' + str(self.id)

'''
table that contains profile of the user.
'''
class Person(models.Model):
    # choices
    GENDER = (
        ('E', '-EMPTY-'),
        ('male', 'Male'),
        ('female', 'Female'),
    )
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    CATEGORY = (
        ('E', '-EMPTY-'),
        ('gen','General'),
        ('sc','Scheduled Class'),
        ('st','Scheduled Tribe'),
        ('pwd','Person With Disability'),
        ('obc', 'Other Backward Class'),
    )
    EDUCATION = (
        ('E', '-EMPTY-'),
        ('l0001', 'Class I'),
        ('l0002', 'Class II'),
        ('l0003', 'Class III'),
        ('l0004', 'Class IV'),
        ('l0005', 'Class V'),
        ('l0006', 'Class VI'),
        ('l0007', 'Class VII'),
        ('l0008', 'Class VIII'),
        ('l0009', 'Class IX'),
        ('l0010', 'Class X'),
        ('l0011', 'Class XI'),
        ('l0012', 'Class XII'),
        ('lug', 'Under Graduate'),
        ('lpg', 'Post Graduate'),
        ('lmphil', 'M.Phil'),
        ('lphd', 'Ph.D'),
    )
    CITIZEN_INDIA = (
        ('E', '-EMPTY-'),
        ('Y','Yes'),
        ('N','No'),
    )
    RELIGION = (
        ('E', '-EMPTY-'),
        ('hinduism', 'Hinduism'),
        ('islam', 'Islam'),
        ('christianity', 'Christianity'),
        ('sikhism', 'Sikhism'),
        ('buddhism', 'Buddhism'),
        ('jainism', 'Jainism'),
        ('zoroastrianism', 'Zoroastrianism'),
        ('other_religions', 'Others'),
    )
    EXTRA_EDUCATION = (
        ('E', '-EMPTY-'),
        ('post_matriculation', 'Post Matriculation'),
        ('diploma_certificates', 'Diploma Certificates'),
        ('bachelors_degree', 'Bachelors Degree'),
        ('diploma_india', 'Diploma India'),
        ('masters_degree', 'Masters Degree'),
    )
    WORKERS = (
        ('E', '-EMPTY-'),
        ('beedi', 'Beedi'),
        ('cine', 'Cine'),
        ('iomc', 'IOMC'),
        ('lsdm', 'LSDM'),
    )
    ARMED = (
        ('E', '-EMPTY-'),
        ('armed', 'Central Armed Police Forces'),
        ('rifles', 'Assam Rifles'),
    )

    # website private data
    gmail_id = models.CharField(max_length=50, primary_key=True)
    iitg_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')

    # user's scholarship list
    marked_scholarships = models.ManyToManyField(Scholarship)

    # user data
    person_name = models.CharField(max_length=100, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER, default='E')
    annual_income = models.PositiveIntegerField(null=True, blank=True)
    monthly_income = models.PositiveIntegerField(null=True, blank=True)
    lump_sum = models.PositiveIntegerField(null=True, blank=True)
    category = models.CharField(max_length=3, choices=CATEGORY, default='E')
    education = models.CharField(max_length=6, choices=EDUCATION, default='E')
    extra_education = models.CharField(max_length=20, choices=EXTRA_EDUCATION, default='E')
    current_cpi = models.DecimalField(null=True, decimal_places=2, max_digits=4, blank=True)
    marks_percentage = models.PositiveIntegerField(null=True, blank=True)
    disability_percent = models.PositiveIntegerField(null=True, blank=True)
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='E')
    religion = models.CharField(max_length=15, choices=RELIGION, default='E')
    workers = models.CharField(max_length=15, choices=WORKERS, default='E')
    armed = models.CharField(max_length=6, choices=ARMED, default='E')


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
        fields = ['person_name', 'birth_date', 'gender', 'annual_income', 'monthly_income', 'lump_sum', 'category', 'education', 'extra_education', 'current_cpi', 'marks_percentage', 'disability_percent', 'citizen_india', 'religion', 'workers', 'armed']

        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'annual_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'lump_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'extra_education': forms.Select(attrs={'class': 'form-control'}),
            'current_cpi': forms.NumberInput(attrs={'class': 'form-control'}),
            'citizen_india': forms.Select(attrs={'class': 'form-control'}),
            'religion': forms.Select(attrs={'class': 'form-control'}),
            'workers': forms.Select(attrs={'class': 'form-control'}),
            'armed': forms.Select(attrs={'class': 'form-control'}),
            'marks_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'disability_percent': forms.NumberInput(attrs={'class': 'form-control'}),
        }
