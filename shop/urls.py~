from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^sweet/list/$', views.sweet_list, name='sweet_list'),
	url(r'^sweet/detail/(?P<sweet_id>\d+)$', views.sweet_detail, name='sweet_detail'),
	url(r'^user/detail/(?P<user_id>\d+)$', views.profile_detail, name='profile_detail'),
	url(r'^sweet/buy/(?P<sweet_id>\d+)$', views.sweet_buy, name='sweet_buy'),
	url(r'^$', views.index, name='main_page'),
	url(r'^manufacturer/list/$', views.manufacturer_list, name='manufacturer_list'),
	url(r'^manufacturer/detail/(?P<manufacturer_id>\d+)$', views.manufacturer_detail, name='manufacturer_detail'),
	url(r'^contact/$', views.contactView, name='contact'),
]
