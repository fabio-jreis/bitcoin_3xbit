from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(max_length=254)
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        email = cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Por favor coloque seu email!')