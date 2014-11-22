from django.conf.urls import patterns, include, url
from washing_analytics.api_views.api import WashHandsData, WashHandsDetails

urlpatterns = patterns('',
    url(r'^$', 'washing_analytics.views.index', name='home'),
    url(r'^wash/$', WashHandsData.as_view()),
    url(r'^leaderboard/(?P<pk>\d+)$', WashHandsDetails.as_view())
)
