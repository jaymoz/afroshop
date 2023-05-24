import factory
from .models import *

from factory import faker
FAKE = faker.Faker('en_US')

class ItemFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Item

	name = factory.Faker("sentence", nb_words=3)
	price = 480
	discount_price = 0
	description = factory.Faker("sentence", nb_words=70)
	slug = factory.Faker("slug")

