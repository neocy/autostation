# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm,TextInput,CheckboxSelectMultiple
from .models import Role,State,Project,Department,Node

class RoleForm(forms.ModelForm):
    # 将多对多从多选下拉菜单改为checkbox
    states = forms.ModelMultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        queryset=State.objects.all()
    )
    rolename = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Role
        fields = '__all__'
        # widgets = {
        #    'states' : CheckboxSelectMultiple(attrs={'class':'checkbox'})
        # }
class StateForm(forms.ModelForm):
    statename = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = State
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    # 将多对多从多选下拉菜单改为checkbox
    # roles = forms.ModelMultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     queryset=Role.objects.all()
    # )
    projectname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    opser = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Project
        fields = '__all__'
        # widgets = {
        #    'states' : CheckboxSelectMultiple(attrs={'class':'checkbox'})
        # }
class DepartmentForm(forms.ModelForm):

    deptname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    owner = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Department
        fields = '__all__'
        # widgets = {
        #    'states' : CheckboxSelectMultiple(attrs={'class':'checkbox'})
        # }
class NodeForm(forms.ModelForm):

    nodename = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Node
        fields = '__all__'
