from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1" : "Sid is Awesome",
        "variable2" : "Dip is not Awesome"
    }
    return render(request, "index.html", context)
    # return HttpResponse("This is home page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def services(request):
    return HttpResponse("This is services page")