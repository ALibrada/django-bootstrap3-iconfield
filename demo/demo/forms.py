# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bootstrap3.tests import TestForm


class ContactForm(TestForm):
    pass


class CustomIconForm(TestForm):
    def __init__(self, *args, **kwargs):
        super(CustomIconForm, self).__init__(*args, **kwargs)
        self.fields['subject']. \
            widget.attrs.update({'custom-icon': 'glyphicon glyphicon-heart'})

        self.fields['select1']. \
            widget.attrs.update({'custom-icon': 'glyphicon glyphicon-heart'})
