from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from shop.models import Sweet, Manufacturer
from django.template import Context, loader
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User, Group
from shop.forms import UserForm, ProfileForm, SweetBuyForm, ContactForm 
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError


def sweet_list(request):
	sweets_list = Sweet.objects.select_related('typeOfSweet')
	paginator = Paginator(sweets_list, 15)	
	page = request.GET.get('page')
	try:
		sweets = paginator.page(page)
	except PageNotAnInteger:
		sweets = paginator.page(1)
	except EmptyPage:
		sweets = paginator.page(paginator.num_pages)
	
	return render(request, 'sweet/sweet_list.html', {'sweets' : sweets})
		
	
def sweet_detail(request, sweet_id):
	try:
		sweet = Sweet.objects.select_related('manufacturer', 'typeOfSweet').get(id=sweet_id)
	except Sweet.DoesNotExist:
		raise Http404
	return render (
		request, 'sweet/sweet_detail.html',
		{'sweet' : sweet}
	)

def sweet_buy(request, sweet_id):
	try:
		sweet = Sweet.objects.select_related('typeOfSweet').get(id=sweet_id)
	except Sweet.DoesNotExist:
		raise Http404	
	if request.method == 'POST':
		form = SweetBuyForm(request.POST)
		if form.is_valid():
			price1 = form.cleaned_data['price1']
			if form.cleaned_data['price2']==None:
				price2 = 0
			else:
				price2 = form.cleaned_data['price2']
			try:			
				price = price1*sweet.price_for_one + (price2/100)*sweet.price_weight
			except TypeError:
				price = price1*sweet.price_for_one
			if request.user.profile.balance >= price:
				request.user.profile.balance -= price
				request.user.profile.save()
				return render(
				request, 'sweet/sweet_thanks.html',			
				)
			else :
				return render(
					request, 'sweet/sweet_nomoney.html'
				)
					
	else:
		form = SweetBuyForm()
	return render (
		request, 'sweet/sweet_buy.html', {
			'form' : form,
			'sweet' : sweet
		}
	)



@login_required
@transaction.atomic	
def profile_detail(request, user_id):
	try:
		user = User.objects.select_related('profile').get(id=user_id)
	except User.DoesNotExist:
		raise Http404
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, ('Your profile was successfully updated!'))
		else:
			messages.error(request, ('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render (
		request, 'profile/profile_detail.html', {
			'user' : user,
			'user_form': user_form,
	       	'profile_form': profile_form
		}	
	)



def index(request):
	return render(request, 'index.html')
	
	
	
def manufacturer_list(request):
	manufacturer_list = Manufacturer.objects.select_related('country')
	paginator = Paginator(manufacturer_list, 15)	
	page = request.GET.get('page')
	try:
		mans = paginator.page(page)
	except PageNotAnInteger:
		mans = paginator.page(1)
	except EmptyPage:
		mans = paginator.page(paginator.num_pages)	
	return render(request, 'manufacturer/manufacturer_list.html', {'manufacturers' : mans})
		
	
def manufacturer_detail(request, manufacturer_id):
	try:
		manufacturer = Manufacturer.objects.select_related('country').get(id=manufacturer_id)
	except Manufacturer.DoesNotExist:
		raise Http404
	return render (
		request, 'manufacturer/manufacturer_detail.html',
		{'manufacturer' : manufacturer}
	)

def contactView(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			sender = form.cleaned_data['sender']
			message = form.cleaned_data['message']
			copy = form.cleaned_data['copy']
			recipients = ['mzkmobile@yandex.ru']			
			if copy:
				recipients.append(sender)
			try:
				send_mail(subject, message, 'ProjectWorkMail@yandex.ru', recipients)
			except BadHeaderError: 
				return HttpResponse('Invalid header found')
			return render(request, 'contact/contact_thanks.html')
	else:
		form = ContactForm()
	return render(request, 'contact/contact.html', {'form': form})	
	
	


	

		
		
	
	
		

