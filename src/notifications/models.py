from django.db import models
from accounts.models import Account
from django.shortcuts import reverse

class Notification(models.Model):
	account    = models.ForeignKey(Account, on_delete=models.CASCADE)
	title 	   = models.CharField(max_length=200, default='', blank=True)
	content    = models.TextField(default='', blank=True)
	link	   = models.TextField(default='')
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_seen	   = models.BooleanField(default=False, blank=True)

	def __str__(self):
		return self.account.name + ' - ' + 'seen = ' + str(self.is_seen)

	class Meta:
		ordering = ['-created_at']