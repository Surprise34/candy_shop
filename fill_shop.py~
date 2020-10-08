import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subd_project.settings')

import django
django.setup()

from shop.models import Sweet, Manufacturer, Country, TypeOfSweet
from django.contrib.auth.models import Group

import random

def fill():
	russia_country = add_country('Россия')
	belarus_country = add_country('Белоруссия')
	turkey_country = add_country('Турция')
	vaflya_type = add_typeOfSweet('Вафля')
	candy_type = add_typeOfSweet('Конфета')
	chocolate_type = add_typeOfSweet('Шоколадка')
	for cou in Country.objects.all():
		if str(cou)=='Россия':
			town = 'Москва'
		elif str(cou)=='Белоруссия':
			town = 'Минск'
		else:
			town = 'Анкара'
		for typ in TypeOfSweet.objects.all():
			for i in range(10):		
				Zavod = add_man(
					name='Завод'+str(i)+str(cou),
					contact_address=town+', ул. Пушкина, д.'+str(i),
					manufacturers_address=town,
					country=cou
				)
				if str(typ)=='Шоколадка':
					add_sweet(
					title= str(typ)+str(i),
					price_for_one=str(random.randint(10,99)/10),
					price_weight=None,
					structure='Шоколад',
					description='Вкусная'+str(typ),
					manufacturer=Zavod,
					typeOfSweet=typ
					)
				else:
					add_sweet(
						title= str(typ)+str(i),
						price_for_one=str(random.randint(10,99)/10),
						price_weight='25.0',
						structure='Шоколад',
						description='Вкусная'+str(typ),
						manufacturer=Zavod,
						typeOfSweet=typ
					)
	

def add_sweet(title, price_for_one, price_weight, structure, description, manufacturer, typeOfSweet):
	c = Sweet.objects.get_or_create(
		title=title, 
		typeOfSweet=typeOfSweet, 
		manufacturer=manufacturer
	)[0]
	c.price_for_one=float(price_for_one)
	if price_weight==None:
		c.price_weight=None
	else:
		c.price_weight=float(price_weight)
	c.structure=structure
	c.description=description
	c.save()
	return c

def add_man(name, contact_address, manufacturers_address, country):
	m = Manufacturer.objects.get_or_create(
		name=name,
		manufacturers_address=manufacturers_address,
		country=country
	)[0]
	m.contact_address=contact_address
	m.save()
	return m

def add_typeOfSweet(name):
	ty = TypeOfSweet.objects.get_or_create(name=name)[0]
	ty.save()
	return ty
	
def add_country(name):
	c=Country.objects.get_or_create(name=name)[0]
	c.save()
	return c 


	
if __name__ == '__main__':
	print('starting shop fill script')
	new_group, created = Group.objects.get_or_create(name='Пользователи')
	fill()	
	
	
	
	

