from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin



from .models import Profile
from .forms import LoginForm, UserRegisterForm
# Create your views here.

# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd["username"],
#                                 password=cd["password"])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect(reverse_lazy("home"))
#                 else:
#                     return HttpResponse("Your account is disabled from login. Please contact the support team for help!")
#             else:
#                 return HttpResponse("Invalid Login")
#     else:
#         form = LoginForm()

#     return render(request, "account/login.html", {"form": form,})


# def user_logout(request):
#     logout(request)
#     return redirect(reverse_lazy("login"))


class UserRegistrationView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    success_message = "Your account was created successfully. Please check your email." 

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(reverse_lazy("home"))

        return super(UserRegistrationView, self).dispatch(*args, **kwargs)


# def user_registration_done_view(request):
#     template_name = "registration/registeration_done.html"
#     context = {}
#     return render(request, template_name, context)

def user_activation_view(request, code=None, *args, **kwargs):
    if code:
        qs = Profile.objects.filter(activation_key=code)
        if qs.exists() and qs.count() == 1:
            profile = qs.first()
            if not profile.activated:
                user_ = profile.user 
                user_.is_active = True
                user_.save()
                profile.activated = True
                profile.activation_key = None
                profile.save()

                messages.success(request, "Your account is Successfully activated")
                return redirect(reverse_lazy("login"))
    messages.success(request, "Oops the activation code is incorrect!")
    return redirect(reverse_lazy("login"))