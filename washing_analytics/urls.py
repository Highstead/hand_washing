from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from washing_analytics.api_views.api import WashHandsData, WashHandsDetails

urlpatterns = patterns('',
    url(r'^', include('washing_analytics.urls', namespace='analytics'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

