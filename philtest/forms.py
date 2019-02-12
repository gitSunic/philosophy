from django import forms
from .models import *

class QuoteForm(forms.ModelForm):

	class Meta:
		model = Quote
		fields = ('author', 'text')