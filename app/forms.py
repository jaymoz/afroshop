from django import forms
from .models import *
from django.forms import ModelForm
from django.core.validators import RegexValidator

class UserContactForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea(attrs={'rows':6}),required=True)


class CheckoutForm(forms.Form):
	street_address = forms.CharField(required=False)
	apartment_address = forms.CharField(required=False)
	city = forms.CharField(required=False)
	phone = forms.IntegerField(required=False,validators=[RegexValidator(regex=r'^(\+?7|8)\d{10}$', message='Phone number must be entered in the format: (+7|8) 960 xxx-xx-xx ' )])
	use_default_delivery = forms.BooleanField(required=False)
	set_default_delivery = forms.BooleanField(required=False)


class DeliveryOptionForm(forms.Form):
	DELIVERY_CHOICES = (
    ('self pickup', 'Self Pickup'),
    ('delivery', 'Delivery')
	)
	delivery_method = forms.ChoiceField(
        widget=forms.RadioSelect, choices=DELIVERY_CHOICES)
class SetDefaultAddressForm(forms.Form):
	option = forms.ChoiceField(widget=forms.RadioSelect)

class RefundForm(forms.Form):
	ref_code = forms.CharField(required=True)
	reason = forms.CharField(required=True)

	code = forms.CharField(widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Coupon code',
		'aria-label': 'Recipient\'s username',
		'aria-describedby': 'basic-addon2',
		'required':False
	}))

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
		
class AddAddressForm(ModelForm):
	class Meta:
		model = Address
		fields = ['street_address','apartment_address','city','phone']
		widgets = {
			'street_address':forms.TextInput(attrs={
				'class':'input-text input-text--primary-style',
				'type':'text',
				'id':'address-fname',
				'required':True,
				'placeholder':'street_address'
			}),
			'apartment_address':forms.TextInput(attrs={
			'class':'input-text input-text--primary-style',
			'id':'address-lname',
			'type':'text',
			'required':True,
			'placeholder':'apartment number'
			}),
			'city':forms.TextInput(attrs={
			'class':'input-text input-text--primary-style',
			'id':'address-street',
			'type':'text',
			'required':True,
			'placeholder':'city'
			}),
			'phone':forms.TextInput(attrs={
			'class':'input-text input-text--primary-style',
			'id':'address-phone',
			'type':'tel',
			'required':True,
			'placeholder':'8 960 xxx-xx-xx'
			})
		}

