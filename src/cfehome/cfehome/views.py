from django.http import HttpResponse


def homePageView(request,*args, **kwargs):
    return HttpResponse("<h1>Hellow world</h1>")