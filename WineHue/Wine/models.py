from django.db import models
from django.utils import timezone

class Cultivar(models.Model):
	GRAPES = (
		('Sauvignon Blanc', 'Sauvignon Blanc'),
		('Chardonnay', 'Chardonnay'),
		('Cabernet Sauvignon', 'Cabernet Sauvignon'),
		('Shiraz', 'Shiraz'),
		('Merlot', 'Merlot'),
		('Pinot Noir', 'Pinot Noir'),
	)
	
	cultivar = models.CharField(max_length=30, choices=GRAPES)

	def __str__(self):
		return self.cultivar

class Wine_Detail(models.Model):
	COLOUR = (
		('White', 'White'),
		('Red', 'Red'),
		('Rose', 'Rose'),
	)

	name = models.CharField(max_length=60)
	vineyard = models.CharField(max_length=30)
	colour = models.CharField(max_length=5, choices=COLOUR)
	cultivar = models.ManyToManyField(Cultivar)
	wine_year = models.PositiveIntegerField(max_length=4, default=timezone.now().year)
	price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)


	def __str__(self):
		return self.name

class Flavour(models.Model):
	#Should the flavours be a STATIC table to choose from? 
	STRENGTH = (
		(0, 'None'),
		(1, 'Barely Noticeable'),
		(2, 'Somewhat Noticeable'),
		(3, 'Very Noticeable'),
		(4, 'Dominant'),
		(5, 'Overpowering'),
		
	)
	wine_name = models.ForeignKey(Wine_Detail, on_delete=models.CASCADE)
	flavour_name = models.CharField(max_length=30)
	flavour_strength = models.IntegerField(choices=STRENGTH)

	def __str__(self):
		return self.flavour_name



