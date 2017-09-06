from django.conf.urls import url
from . import views

app_name = 'orchestration'

urlpatterns = [

    #homepage index
    url(r'^$', views.DeptIndexView.as_view(),name='index'),
    url(r'^table/$', views.tempview.as_view(),name='temp'),

    #department urls
    url(r'^$', views.DeptIndexView.as_view(),name='deptindex'),
    url(r'^detail/department/(?P<pk>[0-9]+)/$', views.DeptDetailView.as_view(),name='deptdetail'),
    url(r'^add/department/$', views.DepartmentCreate.as_view(), name='adddepartment'),
    url(r'^update/department/(?P<pk>\d+)/$', views.DepartmentUpdate.as_view(), name='updatedepartment'),
    url(r'^delete/department/(?P<pk>\d+)/$', views.DepartmentDelete.as_view(), name='deletedepartment'),

    #state urls
    url(r'^index/state/$', views.StateIndexView.as_view(), name='stateindex'),
    url(r'^detail/state/(?P<pk>[0-9]+)/$', views.StateDetailView.as_view(), name='statedetail'),
    url(r'^add/state/$', views.StateCreate.as_view(), name='addstate'),
    url(r'^update/state/(?P<pk>\d+)/$', views.StateUpdate.as_view(), name='updatestate'),
    url(r'^delete/state/(?P<pk>\d+)/$', views.StateDelete.as_view(), name='deletestate'),

    # node urls
    url(r'^index/node/$', views.NodeIndexView.as_view(), name='nodeindex'),
    #url(r'^detail/node/(?P<pk>[0-9]+)/$', views.StateDetailView.as_view(), name='statedetail'),
    url(r'^add/node/$', views.NodeCreate.as_view(), name='addnode'),
    url(r'^update/node/(?P<pk>\d+)/$', views.NodeUpdate.as_view(), name='updatenode'),
    url(r'^delete/node/(?P<pk>\d+)/$', views.NodeDelete.as_view(), name='deletenode'),
    url(r'^delete/nodefromproject/(?P<pk>\d+)/$', views.NodeDeleteProject.as_view(), name='deletenodefromproject'),

    # project urls
    url(r'^index/project/$', views.ProjectIndexView.as_view(), name='projectindex'),
    url(r'^detail/project/(?P<pk>[0-9]+)/$', views.ProjectDetailView.as_view(), name='projectdetail'),
    url(r'^add/project/$', views.ProjectCreate.as_view(), name='addproject'),
    url(r'^update/project/(?P<pk>\d+)/$', views.ProjectUpdate.as_view(), name='updateproject'),
    url(r'^delete/project/(?P<pk>\d+)/$', views.ProjectDelete.as_view(), name='deleteproject'),

   # role urls

    url(r'^index/role/$', views.RoleIndexView.as_view(), name='roleindex'),
    url(r'^detail/role/(?P<pk>[0-9]+)/$', views.RoleDetailView.as_view(), name='roledetail'),
    url(r'^add/role/$', views.RoleCreate.as_view(), name='addrole'),
    url(r'^update/role/(?P<pk>\d+)/$', views.RoleUpdate.as_view(), name='updaterole'),
    url(r'^delete/role/(?P<pk>\d+)/$', views.RoleDelete.as_view(), name='deleterole'),



]