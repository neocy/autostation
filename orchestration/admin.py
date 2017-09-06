# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Project,Role,State,Department,Node


admin.site.register(Project)
admin.site.register(Role)
admin.site.register(State)
admin.site.register(Department)
admin.site.register(Node)