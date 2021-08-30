from django import forms
from django.core import validators
from view_url_app import models


class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"































#
# class user_form(forms.Form):
#     # # user_name = forms.CharField(label='My Name', widget=forms.TextInput(attrs={'Placeholder': 'Your Name', 'class': 'form-control'}))
#     # #
#     # # user_email = forms.EmailField(label='Email', initial='Efaz@....', widget=forms.TextInput(attrs={'Class': 'form-control', 'Placeholder': 'Enter Your Email'}))
#     # #
#     # # user_dob = forms.DateField(label='User Birth Date', widget=forms.TextInput(attrs={'type':'date'}))
#     #
#     # # boolean_field = forms.BooleanField(required=False)
#     # # char_field = forms.CharField(max_length=15, min_length=5)
#     # choices = (('','--Select Option--'), ('1', 'First'), ('2', 'Second'), ('3', 'Third'))
#     # # field = forms.ChoiceField(choices=choices, required=False, widget=forms.RadioSelect)
#     # field = forms.MultipleChoiceField(choices=choices, required=False, widget=forms.CheckboxSelectMultiple)
#
#     # Form Validation
#
#     # name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
#     #
#     # number = forms.IntegerField(validators=[validators.MaxValueValidator(10)])
#
#     # Custom Form Validation
#
#     # def even_or_not(value):
#     #     if value%2 == 1:
#     #         raise forms.ValidationError("Not Even")
#     #
#     #
#     # number = forms.IntegerField(validators=[even_or_not])
#
#     # input match valodation
#
#     user_email = forms.EmailField()
#     user_vmail = forms.EmailField()
#
#     def vlean(self):
#         all_cleaned_data = super().vlean()
#         user_email = all_cleaned_data['user_email']
#         user_vmail = all_cleaned_data['user_vmail']
#
#         if user_email != user_vmail:
#             raise forms.ValidationError("Does nt match")
