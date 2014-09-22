from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bookproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'book.views.home', name='home'),
    url(r'^profile/$', 'book.views.profile', name='profile'),
    url(r'^register/$', 'book.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^livres/(?P<genre_id>\w+)/$', 'book.views.livres', name='livres'),
    url(r'^livre/new/$', 'book.views.new_livre', name='new_livre'),
    url(r'^new_genre/$', 'book.views.new_genre', name='new_genre'),
    url(r'^genres/$', 'book.views.genres', name='genres'),
    # url(r'^map/(?P<location_id>\w+)/$', 'book.views.map', name='map'),







)
