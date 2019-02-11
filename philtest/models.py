from django.db import models

class Quote(models.Model):
	author   = models.CharField(max_length=255, verbose_name="author", default="")
	text     = models.CharField(max_length=255, verbose_name="text", default="")

	def __str__(self):
		return ("\"" + self.text + "\" - " + self.author) 

	def info(self):
		return ("\"" + self.text + "\" - " + self.author) 