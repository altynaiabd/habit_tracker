from django.urls import path, include

from apps.user.views import SignUpView, LogInView, HomepageView, profile

app_name = 'user'

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomepageView.as_view(), name='homepage'),
    path('profile/', profile, name='profile'),
]