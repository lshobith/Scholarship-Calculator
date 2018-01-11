from django import forms
from .models import Person

class WebmailVerifyForm(forms.Form):
    webmail_id = forms.CharField(label='Webmail ID', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    SERVERS = (
        ('teesta.iitg.ernet.in', 'Teesta'),
        ('naambor.iitg.ernet.in', 'Naambor'),
        ('disang.iitg.ernet.in', 'Disang'),
        ('tamdil.iitg.ernet.in', 'Tamdil'),
        ('dikrong.iitg.ernet.in', 'Dikrong'),
    )
    server = forms.ChoiceField(
        label='Webmail Server',
        choices=SERVERS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

'''
form for Person class.
this is not a database.
this form is used for editing the database.
'''
class PersonForm(forms.ModelForm):
    class Meta:
        # the model form is based on Person.
        model = Person

        # Should not contain 'IITG_student', 'gmail_id' and 'marked_scholarships'.
        fields = [
            'person_name',
            'birth_date',
            'annual_income',
            'monthly_income',
            'lump_sum',
            'current_cpi',
            'citizen_india',
            'marks_percentage',
            'is_disabled',
            'disability_percent',
            'eligible_genders',
            'eligible_categories',
            'eligible_religions',
            'eligible_education',
            'eligible_workers',
            'eligible_states_of_india']

        widgets = {
            'person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'annual_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'monthly_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'lump_sum': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_cpi': forms.NumberInput(attrs={'class': 'form-control'}),
            'citizen_india': forms.Select(attrs={'class': 'form-control'}),
            'marks_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'disability_percent': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_disabled': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'eligible_genders': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'eligible_categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'eligible_religions': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'eligible_education': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'eligible_workers': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'eligible_states_of_india': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
