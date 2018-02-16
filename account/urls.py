from django.conf.urls import url
from django.contrib.auth.views import (
                                        LoginView,
                                        LogoutView,
                                        PasswordChangeView,
                                        PasswordChangeDoneView,
                                        PasswordResetView,
                                        PasswordResetDoneView,
                                        PasswordResetConfirmView,
                                        PasswordResetCompleteView,
                                        )

from . import views




urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^register/$', views.UserRegistrationView.as_view(), name='register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', views.user_activation_view, name="user_activation"),

    #change password urls
    url(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change-done/$', PasswordChangeDoneView.as_view(), name="password_change_done"),
    
    # restore password urls
    url(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

# r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',