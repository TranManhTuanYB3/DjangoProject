from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('account/', views.account_view, name="account"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.registration_view, name="register"),
    path('must_authenticate/', views.must_authenticate_view, name="must_authenticate"),
    path('profile/', views.account_view, name="profile"),
    path('address/', views.address, name="address"),
    path('updateaddress/<int:pk>', views.updateaddress, name="updateaddress"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]