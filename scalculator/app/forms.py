from django import forms

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