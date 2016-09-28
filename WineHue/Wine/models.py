from django.db import models

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
#class Expert_Ratings(models.Model):

	#wine_name = models.ForeignKey(Wine_Details, on_delete=models.CASCADE)
	#colour_rating = models.IntegerField(max_length=10)


