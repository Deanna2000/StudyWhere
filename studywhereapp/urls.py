from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "studywhereapp"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^add$', views.add_venue, name='add'),
    url(r'^venues$', views.list_venues, name='list_venues'),
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search, name='search'),
    url(r'venues/', views.list_venues, name='venues'),
    url(r'^get_venues$', views.get_all_venues, name='all_venues'),
    url(r'^detail/(?P<pk>\d+)/$', views.detail_venue, name='detail'),
    url(r'^account/$', views.account_view, name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

