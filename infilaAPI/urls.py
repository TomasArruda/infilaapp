from infila import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'appointments', views.AppointViewSet)
router.register(r'clinics', views.ClinicViewSet)
router.register(r'medics', views.MedicViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'admins', views.AdminViewSet)
router.register(r'tokens', views.TokenViewSet)
router.register(r'ptokens', views.PTokenViewSet)
router.register(r'pnotifications', views.PNotificationViewSet)
router.register(r'anotifications', views.ANotificationViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^adminLogin/$', 'infila.views.adminLogin'),
    url(r'^adminLogout/$', 'infila.views.adminLogout'),
    url(r'^patientLogin/$', 'infila.views.patientLogin'),
    url(r'^patientLogout/$', 'infila.views.patientLogout'),
    url(r'^restricted/$', 'infila.views.restricted'),
    url(r'^check/$', 'infila.views.check'),
    url(r'^pcheck/$', 'infila.views.pcheck'),
)