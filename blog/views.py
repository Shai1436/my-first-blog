# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
def post_list(request):
    return render(request, 'blog/post_list.html', {})
