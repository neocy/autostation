# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models


# Create your models here.

class Department(models.Model):
    deptname = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    dept_logo = models.FileField()
    def __str__(self):
        return self.deptname
    def get_absolute_url(self):
        return reverse('orchestration:deptindex')
class State(models.Model):
    statename = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.statename
    class Meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('orchestration:stateindex')

class Role(models.Model):
    rolename = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    states = models.ManyToManyField(State)
    def __str__(self):
        return self.rolename
    def get_absolute_url(self):
        return reverse('orchestration:addrole', kwargs={'pk': self.pk})

class Project(models.Model):
    projectname = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    opser = models.CharField(max_length=100)
    roles = models.ManyToManyField(Role)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('orchestration:deptindex')
    def __str__(self):
        return self.projectname
class Node(models.Model):
    nodename = models.CharField(max_length=100)
    projectname = models.ForeignKey(Project,on_delete=models.CASCADE)
    roles = models.ManyToManyField(Role)
    def __str__(self):
        return self.nodename
    def get_absolute_url(self):
        return reverse('orchestration:nodeindex')




