from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'hello.html')
def hai(request):
    return render(request, 'hai.html')
+++++++++++++