from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
                      url(r'^(?P<day>\d{4}-\d{2}-\d{2})/all$', 'notifications.views.get_all'),
                    )

urlpatterns = format_suffix_patterns(urlpatterns)
