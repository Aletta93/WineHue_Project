from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator


class Cultivar(models.Model):
	GRAPES = (
		('Sauvignon Blanc', 'Sauvignon Blanc'),
		('Chardonnay', 'Chardonnay'),
		('Chenin Blanc', 'Chenin Blanc'),
		('Cabernet Sauvignon', 'Cabernet Sauvignon'),
		('Shiraz', 'Shiraz'),
		('Merlot', 'Merlot'),
		('Pinot Noir', 'Pinot Noir'),
		('Pinotage', 'Pinotage'),
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
	wine_year = models.PositiveIntegerField(default=timezone.now().year)
	price = models.DecimalField(max_digits=10,decimal_places=2, default=0.00)
	picture = models.ImageField(upload_to='bottle_images')
	flavour_picture = models.ImageField(upload_to='flavour_images')
	colour_red = models.PositiveIntegerField(validators=[MaxValueValidator(254),], default=254)
	colour_green = models.PositiveIntegerField(validators=[MaxValueValidator(254),], default=254)
	colour_blue = models.PositiveIntegerField(validators=[MaxValueValidator(254),], default=254)


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

class Characteristic(models.Model):
	wine_name = models.ForeignKey(Wine_Detail, on_delete=models.CASCADE)
	characteristic_name = models.CharField(max_length=30)

	def __str__(self):
		return self.characteristic_name

