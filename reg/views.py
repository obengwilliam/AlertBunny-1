# Create your views here.


from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt


from django import  forms 
from django.contrib.auth.forms import User

from django.contrib.auth.forms import UserCreationForm





'''
trying  another way to do registration of users

'''

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    fullname = forms.CharField(label = "Full	 name")

    class Meta:
        model = User
        fields = ("username", "fullname", "email",)







def save(self, commit=True):
        form = RegisterForm()
        user = super(RegisterForm, self).save(commit=False)
        first_name, last_name = self.cleaned_data["fullname"].split()
        user.first_name = first_name
        user.last_name = last_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user



@csrf_exempt
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
      
       if form.is_valid():
            print 3
            new_user = form.save();
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/books' + uname)
    else:
        pass

    return render_to_response("reg/base_register.html", {'form' : form})




'''
#Handling registration  obeng william 
class Registration(form.Form):
      username=forms.CharField()
      email=forms.EmailField(widget=forms.TextInput())
      password=forms.CharField(widget=forms.PasswordInput())

@csrf_exempt
def register(request):
    form = registration()
    if request.method == 'POST':
       if form.is_valid:
           new_user = form.save(d)
           return HttpResponseRedirect("/books/")
    else:
        pass

    return render_to_response("reg/base_register.html", {'form' : form})
    


class registration(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

@csrf_exempt
def register(request):
    form = registration()
    if request.method == 'POST':
       data = request.POST.copy()
       if form.is_valid:
           new_user = form.save(data)
           return HttpResponseRedirect("/books/")
    else:
        pass

    return render_to_response("reg/base_register.html", {'form' : form})



'''










#Added placeholder attribute to username and password field 
# @Nana B.

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '    username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '    password'}))


# Login view - @Nana B.
#tested code and it works logs in perfectly
@csrf_exempt
def do_login(request):
	empty_cred = '' #empty login credential variable
	disabled_accMsg = ''
	invalidMsg = ''
	sess_data = ''
        already_logged_in=''#william made changes to your code here...had errors to added this to work
	if request.user.username != '':
		already_logged_in = 'You are already logged in.'

	if request.method == 'POST':
   	        uname = request.POST['username']	
		pword = request.POST['password']
		if uname == '' or pword == '':
			empty_cred = 'Username or password field cannot be empty!'
		else:
			user = authenticate(username=uname, password=pword)
			if user is not None:
				if user.is_active:
					login(request, user)
					#request.session["uname_sess"] = uname
					return HttpResponseRedirect('/bulk/sendsms/' + uname)
			
				##redirect
				else:
					disabled_accMsg = "Sorry, your account has been disabled. Contact the administrator."
				
				##return a disabled account msg
			else:
				invalidMsg = "Username or Password is invalid!"
			
			#return an invalid login message
	
		#YOUR CODE HERE
	else:
		form = LoginForm()
	return render_to_response('reg/base_login.html', {
        'form': form,
        'logged_in': request.user.is_authenticated(),
	'disabled_accMsg': disabled_accMsg,
	'invalidMsg': invalidMsg,
	'empty_cred':empty_cred,
	'already_logged_in': already_logged_in,
	'user': request.user
    })


# Logout view - Nana B.

@csrf_exempt
def do_logout(request):
	if request.user.username != '':
		logout(request)
		request.user.username = ''
		return HttpResponseRedirect('/reg/login')
		
	else:
		return HttpResponseRedirect('/reg/login')
	return render_to_response('reg/base_logout.html',{'user': request.user})
