# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext as _

#------------------------------------------------------------------------------ 
def default_renderer(request, template, content):
    "Wrapper for render_to_response" 
    return render_to_response(template, content, context_instance=RequestContext(request))