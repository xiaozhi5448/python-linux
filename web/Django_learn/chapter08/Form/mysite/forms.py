from django import forms


class ContactForm(forms.Form):
    CITY = [
        ['TP', 'Taipei'],
        ['TY', 'Taoyuang'],
        ['TC', 'Taichung'],
        ['TN', 'Tainan'],
    ]
    user_name = forms.CharField(label='name', max_length=50, initial='xiaoming')
    user_city = forms.ChoiceField(label='city', choices=CITY)
    user_school = forms.BooleanField(label='graduator', required=False)
    user_email = forms.EmailField(label='email')
    user_message = forms.CharField(label='you recommendation', widget=forms.Textarea)


class LoginForm(forms.Form):
    user_name = forms.CharField(label='username', max_length=20)
    user_email = forms.EmailField(label='email')
