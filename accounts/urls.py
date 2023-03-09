from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('my_account/', views.my_account, name="my_account"),
    path('order_details/<str:order_id>', views.order_details, name="order_details"),
    path('order_info/', views.order_info, name="order_info"),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
     # change password urls
    path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('password_change_done')), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
