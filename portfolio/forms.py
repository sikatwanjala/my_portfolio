from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=100
#     )

#     email = forms.EmailField()

#     subject = forms.CharField(
#         max_length=200
#     )

#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'rows': 6
#             }
#         )
#     )


# from django import forms
# from .models import ContactMessage

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = ContactMessage
#         fields = ['name', 'email', 'subject', 'message']