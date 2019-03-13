from django.http import HttpResponse

def sayHi(request):
    return HttpResponse("Hello world! This is my awesome site!")
