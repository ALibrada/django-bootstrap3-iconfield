from django.conf.urls import patterns, include, url

from .views import (HomePageView, IconFormView, IconHorizontalFormView,
                    IconCustomFormView)

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^icons$', IconFormView.as_view(), name='form_icons'),
    url(r'^icons-horizontal$', IconHorizontalFormView.as_view(), name='form_icons_horizontal'),
    url(r'^icons-custom$', IconCustomFormView.as_view(), name='form_icons_custom'),
)
