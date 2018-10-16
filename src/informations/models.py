from django.db import models

class Division(models.Model):
	title = models.CharField(max_length=128)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['title']

	def get_divisions(self):
		return Division.objects.all()

class City(models.Model):
	division = models.ForeignKey(Division, on_delete=models.CASCADE)
	title    = models.CharField(max_length=128)

	def __str__(self):
		return self.division.title + " - " + self.title
	class Meta:
		ordering = ['title']

	def get_cities_choice(self):
		cities  = self.get_cities()
		choices = []
		for c in cities:
			choices.append((c, c))
		return tuple(choices)
		
	def get_cities(self):
		citiesObj = City.objects.all()
		cities    = []
		for obj in citiesObj:
			cities.append(obj.title)
		return cities