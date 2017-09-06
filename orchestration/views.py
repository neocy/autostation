# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Project,Role,State,Department,Node
from django.views.generic import CreateView,UpdateView,DeleteView
from .forms import RoleForm,StateForm,ProjectForm,DepartmentForm,NodeForm
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy

#temp view

class tempview(generic.ListView):
    template_name = 'orchestration/tables.html'
    def get_queryset(self):
        return Department.objects.all()
# Department view

class DeptIndexView(generic.ListView):
    template_name = 'orchestration/deptindex.html'
    def get_queryset(self):
        return Department.objects.all()

class DeptDetailView(generic.DetailView):
    model = Department
    template_name = 'orchestration/deptdetail.html'

class DepartmentCreate(CreateView):
    form_class = DepartmentForm
    template_name = 'orchestration/department_form.html'

class DepartmentUpdate(UpdateView):
    form_class = DepartmentForm
    template_name = 'orchestration/department_form.html'
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return department

class DepartmentDelete(DeleteView):
    mode = Department
    success_url = reverse_lazy('orchestration:deptindex')
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return department

#state view
class StateIndexView(generic.ListView):
    template_name = 'orchestration/stateindex.html'
    def get_queryset(self):
        return State.objects.all()

class StateDetailView(generic.DetailView):
    model = Department
    template_name = 'orchestration/deptdetail.html'

class StateCreate(CreateView):
    form_class = StateForm
    template_name = 'orchestration/state_form.html'

class StateUpdate(UpdateView):
    form_class = DepartmentForm
    template_name = 'orchestration/department_form.html'
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return department

class StateDelete(DeleteView):
    mode = Department
    success_url = reverse_lazy('orchestration:deptindex')
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Department, pk=self.kwargs['pk'])
        return department


# Node view

class NodeIndexView(generic.ListView):
    template_name = 'orchestration/nodeindex.html'
    def get_queryset(self):
        return Node.objects.all()

class NodeDetailView(generic.DetailView):
    model = Node
    template_name = 'orchestration/nodedetail.html'

class NodeCreate(CreateView):
    form_class = NodeForm
    template_name = 'orchestration/node_form.html'

class NodeUpdate(UpdateView):
    form_class = NodeForm
    template_name = 'orchestration/node_form.html'
    def get_object(self, *args, **kwargs):
        node = get_object_or_404(Node, pk=self.kwargs['pk'])
        return node

class NodeDelete(DeleteView):
    mode = Node
    success_url = reverse_lazy('orchestration:nodeindex')
    def get_object(self, *args, **kwargs):
        node = get_object_or_404(Node, pk=self.kwargs['pk'])
        return node

class NodeDeleteProject(DeleteView):
    mode = Node
    success_url = reverse_lazy('orchestration:projectindex')

    def get_object(self, *args, **kwargs):
        node = get_object_or_404(Node, pk=self.kwargs['pk'])
        return node

# Department view

class ProjectIndexView(generic.ListView):
    template_name = 'orchestration/projectindex.html'
    def get_queryset(self):
        return Project.objects.all()

class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context["states"] = Role.states
        return context
    template_name = 'orchestration/projectdetail.html'

class ProjectCreate(CreateView):
    form_class = ProjectForm
    template_name = 'orchestration/project_form.html'

class ProjectUpdate(UpdateView):
    form_class = ProjectForm
    template_name = 'orchestration/project_form.html'
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Project, pk=self.kwargs['pk'])
        return department

class ProjectDelete(DeleteView):
    mode = Project
    success_url = reverse_lazy('orchestration:deptindex')
    def get_object(self, *args, **kwargs):
        department = get_object_or_404(Project, pk=self.kwargs['pk'])
        return department


#role view


class RoleIndexView(generic.ListView):
    template_name = 'orchestration/roleindex.html'
    def get_queryset(self):
        return Role.objects.all()

class RoleDetailView(generic.DetailView):
    model = Role
    template_name = 'orchestration/roledetail.html'

class RoleCreate(CreateView):
    form_class = RoleForm
    template_name = 'orchestration/role_form.html'

class RoleUpdate(UpdateView):
    form_class = RoleForm
    template_name = 'orchestration/role_form.html'
    def get_object(self, *args, **kwargs):
        role = get_object_or_404(Role, pk=self.kwargs['pk'])
        return role

class RoleDelete(DeleteView):
    mode = Role
    success_url = reverse_lazy('orchestration:roleindex')
    def get_object(self, *args, **kwargs):
        role = get_object_or_404(Role, pk=self.kwargs['pk'])
        return role





