
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.ProjectView.as_view(),name='view' ),
    path('create',views.ProjectCreate.as_view(),name='create' ),
    path('project/update/<int:pk>',views.ProjectUpdateView.as_view(), name='project_update'),
    path('task/create', views.TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>', views.TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', views.TaskDeleteView.as_view(), name='task_delete'),
    path('project/delete/<int:pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
]