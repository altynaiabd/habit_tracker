from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

from apps.user.forms import UserModelCreationForm, UserProfileForm


class HomepageView(TemplateView):
    template_name = 'pages/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная'
        return context


class SignUpView(CreateView):
    form_class = UserModelCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'user/signup.html'

    def post(self, request, *args, **kwargs):
        form = UserModelCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            #выход из системы предыдущего пользователя
            logout(request)

            new_user = authenticate(username = form.cleaned_data['username'],
                                    password = form.cleaned_data['password1'],
                                    )
            #Аутентификация и вход пользователя в систему после регистрации
            login(request, new_user)

            return redirect('homepage')
        else:
            return render(request, self.template_name, {'form': form})


class LogInView(LoginView):
    template_name = 'users/login.html'

    # Перенаправление со страницы входа в систему в случае, если пользователь уже прошел аутентификацию и вошел в систему
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return self.render_to_response(self.get_context_data())


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    context = {'form': form}
    return render(request, 'users/profile.html', context)