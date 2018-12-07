# -*- coding: utf-8 -*-
from django.shortcuts import render


def about(request):
    context_dict = {'autor': 'Leonardo Möers'}
    return render(request, 'rango/about.html', context=context_dict)
