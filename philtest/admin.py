from django.contrib import admin
from .models import *

class QuoteAdmin:
	list_display = ('author', 'text')

admin.site.register(Quote)