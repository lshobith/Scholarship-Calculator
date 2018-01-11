from django.db import models

'''
table for states in india
'''
class IndiaState(models.Model):
    state_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.state_name

'''
table containing list of workers
'''
class Worker(models.Model):
    worker_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.worker_name

'''
table containing list of educational courses
'''
class Education(models.Model):
    education_name = models.CharField(max_length=5000)

    def __str__(self):
        return self.education_name

'''
table containing various religions
'''
class Religion(models.Model):
    religion_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.religion_name

'''
table containing list of categories
'''
class Category(models.Model):
    category_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.category_name

'''
table containing list of genders
'''
class Gender(models.Model):
    gender_name = models.CharField(max_length=10)

    def __str__(self):
        return self.gender_name

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

    # fields with relations
    s_eligible_genders = models.ManyToManyField(Gender)
    s_eligible_categories = models.ManyToManyField(Category)
    s_eligible_religions = models.ManyToManyField(Religion)
    s_eligible_education = models.ManyToManyField(Education)
    s_eligible_workers = models.ManyToManyField(Worker)
    s_eligible_states_of_india = models.ManyToManyField(IndiaState)

    data_about = models.TextField(blank=True)

    def unique_id_collapse(self):
        return 'collapse' + str(self.id)

    def unique_id_save(self):
        return 'save' + str(self.id)

    def unique_id_remove(self):
        return 'remove' + str(self.id)

    def unique_id_badge(self):
        return 'badge' + str(self.id)

    def __str__(self):
        return self.scholarship_name

'''
table that contains profile of the user.
'''
class Person(models.Model):
    # choices
    IITG_STUDENT = (
        ('Y', 'yes'),
        ('N', 'no'),
    )
    CITIZEN_INDIA = (
        ('E', ''),
        ('Y','Yes'),
        ('N','No'),
    )

    # website private data
    gmail_id = models.CharField(max_length=50, primary_key=True)
    iitg_student = models.CharField(max_length=1, choices=IITG_STUDENT, default='N')

    # user's scholarship list
    marked_scholarships = models.ManyToManyField(Scholarship)

    # fields with relations
    eligible_genders = models.ManyToManyField(Gender)
    eligible_categories = models.ManyToManyField(Category)
    eligible_religions = models.ManyToManyField(Religion)
    eligible_education = models.ManyToManyField(Education)
    eligible_workers = models.ManyToManyField(Worker)
    eligible_states_of_india = models.ManyToManyField(IndiaState)

    # user data
    person_name = models.CharField(max_length=100, blank=True, default='')
    birth_date = models.DateField(null=True, blank=True)
    annual_income = models.PositiveIntegerField(null=True, blank=True)
    monthly_income = models.PositiveIntegerField(null=True, blank=True)
    lump_sum = models.PositiveIntegerField(null=True, blank=True)
    current_cpi = models.DecimalField(null=True, decimal_places=2, max_digits=4, blank=True)
    marks_percentage = models.PositiveIntegerField(null=True, blank=True)
    is_disabled = models.BooleanField(default=False)
    disability_percent = models.PositiveIntegerField(null=True, blank=True)
    citizen_india = models.CharField(max_length=1, choices=CITIZEN_INDIA, default='E')

    def __str__(self):
        return "[" + self.person_name + "] " + self.gmail_id
