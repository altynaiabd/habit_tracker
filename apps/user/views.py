from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from apps.user.forms import UserModelCreationForm


class SignUpView(CreateView):
    form_class = UserModelCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'user/signup.html'

    def post(self, request, *args, **kwargs):
        form = UserModelCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        else:
            return render(request, self.template_name, {'form': form})