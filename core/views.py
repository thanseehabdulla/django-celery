from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect


from .form import GenerateRandomUserForm
from .task import create_random_usr_accounts


# Create your views here.
class GenerateRandomUserView(FormView):
    template_name = 'core/generate_random_users.html'
    form_class = GenerateRandomUserForm


    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_usr_accounts.delay(total)
        messages.success(self, request, 'We are generating random users, Wait a moment please')
        return redirect('user_list')