from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
                      url(r'^all/(?P<day>\d{4}-\d{2}-\d{2})$', 'social.views.get_all'),
                      url(r'^trends/(?P<day_start>\d{4}-\d{2}-\d{2})/(?P<day_end>\d{4}-\d{2}-\d{2})$', 'social.views.get_trends'),
                    )

urlpatterns = format_suffix_patterns(urlpatterns)
