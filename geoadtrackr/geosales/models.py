from django.db import models

# Create your models here.
# keys are built-in under hood of Model
#publisher
class Publisher(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	url = models.CharField(max_length=500)
	email = models.CharField(max_length=100)

#app
class App(models.Model):
	app_name = models.CharField(max_length=100)
	app_store_type = models.CharField(max_length=100)
	current_bid = models.IntegerField(default=0)
	app_balance = models.IntegerField(default=0)
	publisher = models.ForeignKey(Publisher)

#agent TO-DO agent
class Agent(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	email = models.CharField(max_length=100)

class Venue(models.Model):
	venue_name = models.CharField(max_length=100)
	agent_id = models.ForeignKey(Agent)

#Possible Tables
#App_to_Venue (App - Agent - rate)
class App_to_Venue(models.Model):
	app_id = models.ForeignKey(App)
	venue_id = models.ForeignKey(Venue)
	current_bid = models.IntegerField(default=0)

#Installs User_id - Date - App_id
class Install(models.Model):
	install_time = models.DateTimeField('datetime installed')
	app_id = models.ForeignKey(App)
	venue = models.ForeignKey(Venue)
	install_bid = models.IntegerField(default=0)
	lat = models.DecimalField(max_digits=15, decimal_places=10)
	lon = models.DecimalField(max_digits=15, decimal_places=10)
	accuracy = models.IntegerField(default=0)

#geofields
# class Geofield(models.Model):
# 	lat = models.DecimalField(max_digits=15, decimal_places=10)
# 	lon = models.DecimalField(max_digits=15, decimal_places=10)
# 	venue_id = models.OneToOneField(Venue)