from django.conf.urls import url

from . import views

app_name = "website"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^sell$', views.sell_product, name='sell'),
    url(r'^products$', views.list_products, name='list_products'),
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'products/', views.list_products, name='products'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_product, name='detail'),
    url(r'^account/$', views.account_view, name='account'),
	  url(r'^category$', views.category_product, name='category')

]