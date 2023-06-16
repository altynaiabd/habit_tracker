from django.urls import path, include

from apps.user.views import SignUpView, LogInView, HomepageView, profile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('', HomepageView.as_view(), name='homepage'),
    path('profile/', profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]