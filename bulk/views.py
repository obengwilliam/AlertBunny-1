# Create your views here.


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django import  forms 
from django.contrib.auth.forms import User
from dj_simple_sms.models import SMS

'''
beginning sms
'''

class SMSForm(forms.Form):
    senderid = forms.CharField()
    message = forms.TextField()
    receiver=forms.TextField()

def sample_send_sms():
    message_to_send = SMS(to_number='louia', from_number='djNGO', body='fuck you')
    message_to_send.send()
    return HttpResponse('/bulk')
