# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Project,Role,State,Department
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import RoleForm,StateForm,ProjectForm,DepartmentForm
from django.shortcuts import get_object_or_404

# Create your views here.

class DeptIndexView(generic.ListView):
    template_name = 'orchestration/deptindex.html'
    def get_queryset(self):
        return Department.objects.all()

class DeptDetailView(generic.DetailView):
    model = Department
    template_name = 'orchestration/deptdetail.html'

class StateCreate(CreateView):
    model = State
    fields = ['statename']

class RoleCreate(CreateView):
    form_class = RoleForm
    template_name = 'orchestration/role_form.html'
class StateCreate(CreateView):
    form_class = StateForm
    template_name = 'orchestration/state_form.html'
class ProjectCreate(CreateView):
    form_class = ProjectForm
    template_name = 'orchestration/project_form.html'
class DepartmentCreate(CreateView):
    form_class = DepartmentForm
    template_name = 'orchestration/department_form.html'
class DepartmentUpdate(UpdateView):
    form_class = DepartmentForm
    template_name = 'orchestration/department_form.html'
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return department

