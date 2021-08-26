from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Member
from .forms import JoinForm

from django.core.mail import send_mail

from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def index(request):
    
    if 'join_status' not in request.session:
        request.session['join_status'] = None

    if request.method == "POST":
        form = JoinForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            major = form.cleaned_data['major']
            exp_grad_year = form.cleaned_data['exp_grad_year']
            notifications = form.cleaned_data['notifications']

            new_member = Member(
                email=email, 
                name=name, 
                major=major, 
                exp_grad_year=exp_grad_year, 
                notifications=notifications
            )
            
            new_member.save()
            request.session['join_status'] = 'joined'

            current_site = get_current_site(request)

            send_mail(
                subject='Verify your identity: Thank you for joining MakeOpenSource!',
                message=render_to_string('join/acc_active_email.html', {
                    'member': new_member,
                    'email': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(new_member.pk)),
                    'token':account_activation_token.make_token(new_member),
                }),
                from_email='no-reply@makeopensource.org',
                recipient_list=[email],
                fail_silently=False,
            )
            
            return HttpResponseRedirect('/join/')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid'
    else:
        form = JoinForm()
    
    return render(request, 'join/index.html',
        {'form': form, 'join_status': request.session['join_status']})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64)).decode()
        member: Member = Member.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Member.DoesNotExist):
        member = None
    if member is not None and account_activation_token.check_token(member, token) and account_activation_token.is_valid():
        member.verified = True
        member.save()
        return HttpResponse('Thanks for verifying your email! You are now officially a club member ')
    else:
        return HttpResponse('Activation link is invalid!')
