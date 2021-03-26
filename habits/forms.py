from django import forms
from .models import Habit
#from django.forms.widgets import ClearableFileInput


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = '__all__'


    #image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
