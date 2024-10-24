from django.urls import path
from . import views

app_name = 'user_accounts'

urlpatterns = [
    path(r'profile/', views.Profile.as_view(), name='account-welcome'),
    path('signup/', views.Signup.as_view(), name='authemail-signup'),
    path('signup/verify/', views.SignupVerify.as_view(), name='authemail-signup-verify'),
    path('logout/', views.Logout.as_view(), name='authemail-logout'),
    path('password/reset/', views.PasswordReset.as_view(), name='authemail-password-reset'),
    path('password/reset/verify/', views.PasswordResetVerify.as_view(), name='authemail-password-reset-verify'),
    path('password/reset/verified/', views.PasswordResetVerified.as_view(), name='authemail-password-reset-verified'),
    path('password/change/', views.PasswordChange.as_view(), name='authemail-password-change'),
    path('api-token', views.get_api_token, name='get-api-token'),
    path('send-reset-email', views.send_reset_email, name='send-reset-email'),
    path('sign-up', views.sign_up, name='signup')
]
