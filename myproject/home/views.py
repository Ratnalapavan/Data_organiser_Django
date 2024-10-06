from django.shortcuts import render, redirect
from django.http import HttpResponse

def index1(request):
    return HttpResponse("Hello, world. This is my first Django app!")

def index(request):
    return render(request,"home/form.html")

def submit_view(request):
    if request.method == "POST":
        ids = request.POST.get("your_id")
        return redirect("success_view",ids)
    return HttpResponse("Method is not post")

def success_view(request,hi):
    res = f"Thanks for using. Your ID is {hi}"
    return HttpResponse(res)

def detail(request,id):
    # return HttpResponse("Text Updated to Custome.........")
    c = {"counter":id}
    return render(request, 'home/detail.html',c)
