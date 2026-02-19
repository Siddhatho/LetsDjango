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
    return render(request,'about.html')
    #return HttpResponse("This is about page")

def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')