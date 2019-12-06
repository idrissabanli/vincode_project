from django.db import models


class Vincode(models.Model):
	vin=models.CharField(max_length=50)
	make=models.CharField(max_length=50)
	model=models.CharField(max_length=50)
	odometr=models.CharField( max_length=50)
	engine=models.CharField(max_length=50)
	year=models.CharField(max_length=50)
	color=models.CharField(max_length=50)
	primary_damage=models.CharField(max_length=100)
	secondary_damage=models.CharField(max_length=100)
	def __str__(self):
		return self.make




class Image(models.Model):
	image=models.ImageField(upload_to="vin_code",blank=True, null=True)
	Vin=models.ForeignKey("Vincode", on_delete=models.CASCADE,related_name='vincode',blank=True, null=True)

	def __str__(self):
		return self.Vin.vin