from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(r):
	return render(r,'html/about.html')

def contact(r):
	return render(r,'html/contactus.html')

def login(r):
	return render(r,'html/login.html')

def register(r):
	if r.method == "POST":
		u=r.POST['uname']
		e=r.POST['eml']
		p=r.POST['ps']
		a=r.POST['aag']
		d={'user':u,'email':e,'pass':p,'age':a}
		return render(r,'html/details.html',{'d':d})
	return render(r,'html/register.html')