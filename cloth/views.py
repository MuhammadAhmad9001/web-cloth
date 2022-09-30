from django.shortcuts import render
def home(request):
    print("welcome to home")
    return render(request,"index.html") 



# Create your views here.
