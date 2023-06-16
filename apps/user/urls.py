from django.urls import path, include

from apps.user.views import SignUpView, LogInView, HomepageView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('', HomepageView.as_view(), name='homepage'),
    path('', include('django.contrib.auth.urls')),
]