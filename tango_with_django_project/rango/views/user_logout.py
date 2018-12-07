# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))