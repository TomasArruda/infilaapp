from django.conf.urls import patterns, url

urlpatterns = patterns('infila.views',
    url(r'^patients/$', 'patient_list'),
    url(r'^patients/(?P<pk>[0-9]+)/$', 'patient_detail'),
)
