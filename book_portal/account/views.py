from django.shortcuts import render,redirect,reverse
from django.contrib.auth.views import LoginView
from django.views import View
from .forms import signUpForm,UpdateProfileForm,UpdateUserForm
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden,HttpResponseRedirect


class LoginView(LoginView):
    template_name='account/login.html'

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import signUpForm  # Import your custom form

class SignUpView(View):
    def get(self, request):
        form = signUpForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request):
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('get_books')  # Redirect to the desired URL upon successful signup
        return render(request, 'account/signup.html', { 'form': form })
    
class SameUserRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        print('printin',user_id) 
        if not request.user.id != user_id:
            return HttpResponseForbidden("You do not have permission to edit this user.")
        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(SameUserRequiredMixin,View):
    def get(self,request):
        form=UpdateUserForm()
        profileUpdateForm = UpdateProfileForm()
        return render(request,'account/profileUpdate.html',{'form': form,'profileform':profileUpdateForm})
    
    def post(self,request):
        user=request.user
        form = UpdateUserForm(request.POST,instance=user)
        profileUpdateForm = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid() and profileUpdateForm.is_valid():
            print(profileUpdateForm.cleaned_data['favorite_genres'])
            form.save()
            profileUpdateForm.save()
        return redirect(reverse('profile',args=[user.pk]))

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid:
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'account/password_change_done.html')

def profileView(request,pk):
    user=User.objects.get(id=pk)
    return render(request,'account/profile.html',{'user':user})

'''
if request.method == 'POST':
        if not user == request.user:
            return HttpResponseForbidden('You dont have access')
        form = UpdateUserForm(request.POST,instance=user)
        profileUpdateForm = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if form.is_valid() and profileUpdateForm.is_valid():
            print(profileUpdateForm.cleaned_data['favorite_genres'])
            form.save()
            profileUpdateForm.save()
        return redirect(reverse('profile',args=[user.pk]))
    else:
        form=UpdateUserForm()
        profileUpdateForm = UpdateProfileForm()
        ,'form': form,'profileform':profileUpdateForm
'''
def blockUser(request,userId):
    user = User.objects.get(id=userId)
    if request.user.is_superuser:
        user.is_active = not user.is_active
        user.save()
        return HttpResponseRedirect(reverse('profile', args=[userId]))

    else:
        return HttpResponseForbidden("Access Denied: You are not a superuser.")
