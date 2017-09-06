from django.conf.urls import url
from . import views

app_name = 'orchestration'

urlpatterns = [
    #/music/
    url(r'^$', views.DeptIndexView.as_view(),name='deptindex'),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DeptDetailView.as_view(),name='deptdetail'),
    url(r'^addstate/$', views.StateCreate.as_view(),name='addrState'),
    url(r'^add/state/$', views.StateCreate.as_view(),name='addstate'),
    url(r'^add/role/$', views.RoleCreate.as_view(), name='addrole'),
    url(r'^add/project/$', views.ProjectCreate.as_view(), name='addproject'),
    url(r'^add/department/$', views.DepartmentCreate.as_view(), name='adddepartment'),
    url(r'^update/department/(?P<pk>\d+)/$', views.DepartmentUpdate.as_view(), name='updatedepartment'),
]