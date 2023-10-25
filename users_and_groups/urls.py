from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('users/', views.users_list, name='users'),
    path('users/create/', views.create_user, name='create_user'),
    path('users/<int:pk>/edit', views.UserEditView.as_view(), name='user_edit'),
    path('groups/', views.groups_list, name='groups'),
    path('groups/create/', views.create_group, name='create_group'),
    path('action_delete/', views.action_delete, name='action_delete'),
    path('groups/<int:pk>/edit', views.GroupEditView.as_view(), name='group_edit')
]
