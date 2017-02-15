from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about', views.about, name='about'),
        url(r'^graph', views.graph, name='graph'),
        url(r'^map', views.map, name='map'),
        url(r'^facts',views.facts, name='facts'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',  views.add_page, name='add_page'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^search/', views.search, name='search'),
)