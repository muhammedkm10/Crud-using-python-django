from django.shortcuts import render
def main(request):
    return render(request,'main.html')
def signup(request):
    return render(request,'usersignup.html')
def login(request):
    return render(request,'userlogin.html')
def admin_login(request):
    return render(request,'admin.html')