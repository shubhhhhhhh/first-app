from django.shortcuts import render

# Create your views here.
def first(request):
    list=[1,4,2,3,8]
    # return render(request,'index.html')  //simply render without any modification in html file for render
    # for modification in the html file for render
    return render(request,'index.html',{'data':list})  