from django import forms
from django.core.validators import RegexValidator

class UserForm(forms.Form) :
    CHOICE = (
    ('DB値', '任意'),
    ...
)
    account_id_regex = RegexValidator(regex=r'^[a-zA-Z0-9_@]+$', message='This format is not allowed.')

    select = forms.ChoiceField(label='...', widget=forms.Select, choices=CHOICE)
    volume = forms.DecimalField(label='...', max_digits=7, decimal_places=2)
    account_id = forms.CharField(label='...', validators=[account_id_regex])

    def __str__(self) : 
        return self.account_id