from django.contrib import admin
from django import forms
from .models import Building, Suite

admin.site.register(Building)
admin.site.register(Suite)

"""class SuiteForm(forms.ModelForm):
	class Meta:
		model = Suite
		widgets = {
			'type': forms.Select()
		}

class SuiteAdmin(admin.ModelAdmin):
	form = SuiteForm

	def formField(self, db_field, **kwargs):
		if db_field.name == 'annually':
			kwargs['widget'].choices = (
				('YR', 'yearly'), 
				('MO', 'monthly')
			)
		return super(SuiteAdmin, self).formField(db_field, **kwargs)"""
