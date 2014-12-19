# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

from .forms import ContactForm, CustomIconForm


class HomePageView(TemplateView):
    template_name = 'demo/home.html'

    def get_context_data(self, **kwargs):
            context = super(HomePageView, self).get_context_data(**kwargs)
            messages.info(self.request, 'This is a demo of a message.')
            return context


class IconFormView(FormView):
    template_name = 'demo/icon.html'
    form_class = ContactForm


class IconHorizontalFormView(FormView):
    template_name = 'demo/icon-horizontal.html'
    form_class = ContactForm


class IconCustomFormView(FormView):
    template_name = 'demo/custom-icons.html'
    form_class = CustomIconForm
