from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Humne 'login/' ko badal kar 'accounts/login/' kar diya
    path('accounts/login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    path('', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('update/<int:pk>/', views.task_update, name='task-update'),
    path('delete/<int:pk>/', views.task_delete, name='task-delete'),
]