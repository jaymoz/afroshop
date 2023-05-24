import django_filters
from django_filters import FilterSet
from django_filters import DateFilter
from .models import *

class OrderFilterForm(django_filters.FilterSet):
	orderd_date = django_filters.DateFilter(field_name="ordered_date", lookup_expr='gte')
	start_date = django_filters.DateFilter(field_name="ordered_date", lookup_expr='lte')
	class Meta:
		model = Order
		fields = ['status']
		widgets = {
			'status':django_filters.ModelChoiceFilter(attrs={
				'class':'input-text input-text--primary-style',
				'type':'text',
				'id':'address-fname',
			})
		}