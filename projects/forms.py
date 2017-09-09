from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
    	model = Project
    	fields = '__all__'
class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		exclude = ['project']


class ContributorForm(forms.ModelForm):
	class Meta:
		model = Contributors
		fields = '__all__'

