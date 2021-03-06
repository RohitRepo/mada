from __future__ import unicode_literals

from django.db import models

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	dated = models.DateField(unique=True)

	dau_total = models.IntegerField(default=0)
	dau = models.IntegerField(default=0)
	dau_compare = models.IntegerField(default=0)
	yesterday_dau = models.IntegerField(default=0)
	yesterday_dau_compare = models.IntegerField(default=0)
	before_dau = models.IntegerField(default=0)
	before_dau_compare = models.IntegerField(default=0)
	week_dau = models.IntegerField(default=0)
	week_dau_compare = models.IntegerField(default=0)
	month_dau = models.IntegerField(default=0)
	month_dau_compare = models.IntegerField(default=0)
	
	nu_total = models.IntegerField(default=0)
	nu = models.IntegerField(default=0)
	nu_compare = models.IntegerField(default=0)
	yesterday_nu = models.IntegerField(default=0)
	yesterday_nu_compare = models.IntegerField(default=0)
	before_nu = models.IntegerField(default=0)
	before_nu_compare = models.IntegerField(default=0)
	week_nu = models.IntegerField(default=0)
	week_nu_compare = models.IntegerField(default=0)
	month_nu = models.IntegerField(default=0)
	month_nu_compare = models.IntegerField(default=0)

	class Meta:
		abstract = True
		ordering = ['dated']
