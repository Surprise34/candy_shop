#coding=utf8
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver


class Country(models.Model):
	name = models.CharField(verbose_name='Страна', max_length=65, unique=True)	
	class Meta:
		ordering = ('name', )
		verbose_name = 'Страна'
		verbose_name_plural = 'Страны'		
	def __str__(self):
		return self.name
			

class Manufacturer(models.Model):
    name = models.CharField(verbose_name='Изготовитель', max_length=100)
    contact_address = models.CharField(verbose_name='Контактный адрес', max_length=250)
    manufacturers_address = models.CharField(
        verbose_name='Адрес производства',
    	max_length = 250
    )
    country = models.ForeignKey(
    	verbose_name='Страна', 
    	to=Country, 
    	null=True, 
    	on_delete=models.CASCADE) 
    def __str__(self):
    	return self.name
    class Meta:
        ordering = ('country', )
        verbose_name = 'Изготовитель'
        verbose_name_plural = 'Изготовители'       
    
    	
    	
    	

class TypeOfSweet(models.Model):
	name = models.CharField(verbose_name='Тип сладости', max_length=50, unique=True)	
	class Meta:
		ordering = ('name', )
		verbose_name = 'Тип сладости'
		verbose_name_plural = 'Типы сладостей'		
	def __str__(self):
		return self.name    
		
		
		
			
    	
class Sweet(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)
    price_for_one = models.FloatField(verbose_name='Цена за одну штуку', null=True)
    price_weight = models.FloatField(verbose_name='Цена за 100 грамм', blank=True, null=True)
    structure = models.CharField(verbose_name='Состав', max_length=201)
    description = models.CharField(verbose_name='Описание', max_length=200)
    manufacturer = models.ForeignKey(
    	verbose_name='Изготовитель', 
    	to=Manufacturer,
    	null=True, 
    	on_delete=models.CASCADE
    )
    typeOfSweet = models.ForeignKey(
    	verbose_name='Тип сладости',
    	to=TypeOfSweet, 
    	on_delete=models.CASCADE,
    	null=True
    )
      
    class Meta:
        ordering = ('title', 'manufacturer', )
        verbose_name = 'Сладость'
        verbose_name_plural = 'Сладости' 
        permissions = (
        	('buy_sweet' , 'Купить сладость'),
        )       
    def __str__(self):
    	return self.title
    	
    	
class Profile(models.Model):
	user = models.OneToOneField(
		User, 
		unique=True,
		on_delete=models.CASCADE
	)
	bio = models.TextField(max_length=500, blank=True, null=True)
	vk_page = models.CharField(verbose_name='Страница Вконтакте',max_length=30,blank=True, null=True)
	balance = models.FloatField(verbose_name='Баланс', default=100.0)
	timezone = models.CharField(verbose_name='Часовой пояс',max_length=50, default='Europe/Moscow')
	
	def __str__(self):
		return self.user.username
	
		

@receiver(post_save, sender=User)	
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
      

@receiver(post_save, sender=User)	
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
@receiver(post_save, sender=User, dispatch_uid='myproject.myapp.models.user_post_save_handler')
def user_post_save(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Пользователи'))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




