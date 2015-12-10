from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime


# Create your models here.
class Stage(models.Model):
	name = models.CharField(max_length=200)
	order= models.IntegerField(help_text = 'The order displayed on the screen')
	description = models.TextField(blank = True, null = True)
	value = models.IntegerField(help_text = 'On a scale of 0 to 100')

	def __unicode__(self):
		return self.name

class Company(models.Model):
	name = models.CharField(max_length=200)
	website = models.URLField(max_length = 200, blank=True, null=True)
	address1 = models.CharField(max_length=200, blank=True, null=True)
	address2 = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=200, blank=True, null=True)
	zipcode = models.CharField(max_length=200, blank=True, null=True)
	country = models.CharField(max_length=200, blank=True, null=True)
	phone = models.CharField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'companies'

class Contact(models.Model):
	company = models.ForeignKey(Company, blank=True, null=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address1 = models.CharField(max_length=200, blank=True, null=True)
	address2 = models.CharField(max_length=200, blank=True, null=True)
	city = models.CharField(max_length=200, blank=True, null=True)
	state = models.CharField(max_length=200, blank=True, null=True)
	zipcode = models.CharField(max_length=200, blank=True, null=True)
	country = models.CharField(max_length=200, blank=True, null=True)
	phone = models.CharField(max_length=200, blank=True, null=True)
	email = models.EmailField(max_length=200, blank=True, null=True)

	def get_full_name(self):
		return str(self.first_name) + " " + str(self.last_name)

	def __unicode__(self):
		return self.get_full_name()

class Campaign(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank = True, null = True)

	def __unicode__(self):
		return self.name

class Opportunity(models.Model):
	stage = models.ForeignKey(Stage)
	company = models.ForeignKey(Company, blank=True, null=True)
	contact = models.ForeignKey(Contact)
	value = models.FloatField(help_text='how much this opportunity is worth')
	source = models.ForeignKey(Campaign)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	create_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'opportunites'

	def __unicode__(self):
		if self.company:
			return str(self.company)
		else:
			return str(self.contact)

class Reminder(models.Model):
	opportunity = models.ForeignKey(Opportunity)
	date = models.DateField()
	note = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.note)

class Report(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()

	def __unicode__(self):
		return self.name

class CallLog(models.Model):
	opportunity = models.ForeignKey(Opportunity)
	date = models.DateTimeField(auto_now_add=True)
	note = models.TextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL)

	def __unicode__(self):
		return str(self.opportunity) + " on " + str(self.date.strftime("%Y-%m-%d")) + " by " + str(self.user.get_full_name())

class OpportunityStage(models.Model):
	opportunity = models.ForeignKey(Opportunity)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	stage = models.ForeignKey(Stage)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return str(self.opportunity) + " moved to " + str(self.stage)

	class Meta:
		ordering = ['-timestamp']




              # <div>
              # <li>
              # <form method="GET" action="{% url 'crm:search' %}" class="navbar-form" role="search">
              # <div class="input-group">
              #     <input type="text" class="form-control" placeholder="Search" name="q">
              #     <div class="input-group-btn">
              #         <button class="btn" type="submit"><i class="glyphicon glyphicon-search" style="color:white;"></i></button>
              #     </div>
              # </div>
              # </form>
              # </li>
              # </div>
