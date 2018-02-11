from django.db import models



# Create your models here.

class Soci(models.Model):
	cognome = models.CharField(max_length=50)
	nome = models.CharField(max_length=50)
	luogo = models.CharField(max_length=50)
	data = models.DateField()
	slug = models.SlugField()

# pytnon3	
	def __str__(self):
		return self.cognome
		


# pytnon2
	def __unicode__(self):
		return self.cognome

