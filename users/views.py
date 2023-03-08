from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic

from .forms import UserUpdateForm, MyCustomSignupForm
from listings.models import Contact


class RegisterView(generic.CreateView):

    def get(self, request, *args, **kwargs):
        context = {'form': MyCustomSignupForm()}
        return render(request, 'account/signup.html', context)

    def post(self, request, *args, **kwargs):
        form = MyCustomSignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            messages.success(request, f'Account has been created successfullly')
            return redirect('account_login')
        return render(request, 'account/signup.html', {'form': form})

class Profile(LoginRequiredMixin, generic.View):
    template_name = 'account/profile.html'

    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
        context = {
            'u_form': u_form,
            'contacts': contacts
        }
        return render(request, self.template_name, context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
        else:
            messages.error(request, f'Your account has not been updated!')
        return redirect('profile')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.warning(
                request, 'There was an error changing your password!')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'account/password_change.html', {'form': form})
