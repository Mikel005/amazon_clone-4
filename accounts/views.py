
# from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from .forms import SignupForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.template.loader import render_to_string
from django.contrib.auth.models import User
# from django.core.mail import EmailMessage
# from .tokens import account_activation_token

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']
        # user = User.objects.create_user(username=username, email=email)
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})







# def signup_view(request):
#     # if request.method == "POST":
#     #     username = request.POST['username']
#     #     email = request.POST['email']
#     #     password = request.POST['password']
#     #     user = User.objects.create_user(username=username, email=email, password=password)
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         user = CustomUser.objects.create_user( form=form)
#         #user = User.objects.create_user(username=username, email=email, password=password)
#         if form.is_valid():
#             #user = form.save()
            
            
#             email = request.POST['email']
#             login(request, user)
#             return redirect('/')
    #     user.is_active = False  # Deactivate until email confirmed
    #     user = form.save()
    #     user.save()
    #     # Send verification email
    #     current_site = get_current_site(request)
    #     mail_subject = 'Activate your account'
    #     message = render_to_string('acc_active_email.html', {
    #         'user': user,
    #         'domain': current_site.domain,
    #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
    #         'token': account_activation_token.make_token(user),
    #     })
    #     email_message = EmailMessage(mail_subject, message, to=[email])
    #     email_message.send()
    #     return render(request, 'check_email.html')
    # else:
    #     form = SignupForm()
    # return render(request, 'accounts/signup.html', {'form': form})



# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         login(request, user)
#         return redirect('home')
#     else:
#         return render(request, 'activation_invalid.html')



def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')