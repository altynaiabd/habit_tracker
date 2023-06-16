from django.urls import path

from apps.user.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]