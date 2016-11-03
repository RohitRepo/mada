from django.conf.urls import patterns, url, include

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns('',
                      url(r'^all/(?P<day>\d{4}-\d{2}-\d{2})$', 'transactions.views.get_all'),
                      url(r'^trends/(?P<day_start>\d{4}-\d{2}-\d{2})/(?P<day_end>\d{4}-\d{2}-\d{2})$', 'transactions.views.get_trends'),
                      url(r'^(?P<day>\d{4}-\d{2}-\d{2})/started$', 'transactions.views.started'),
                      url(r'^(?P<day>\d{4}-\d{2}-\d{2})/completed$', 'transactions.views.completed'),
                      url(r'^(?P<day>\d{4}-\d{2}-\d{2})/completed-drop$', 'transactions.views.completed_drop'),
                    )

urlpatterns = format_suffix_patterns(urlpatterns)
