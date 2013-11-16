# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('desktop.views',
    (r'^$', 'view_index'),                   
    (r'^c/desktop/$', 'view_desktop'),
    (r'^system_folder/$', 'system_folder'),
    (r'^information/$', 'information'),
    (r'^tutorial/$', 'tutorial'),
    (r'^cmd/$', 'command_line'),
    (r'^webexplorer/$', 'webexplorer'),
    (r'^app/(?P<app_name>\w+)/$', 'run_app'),
    
    # AJAX
    (r'^ajax_query/(?P<query_id>\w+)/$', 'ajax_query'),
)
