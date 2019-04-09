from django.shortcuts import render, HttpResponse, HttpResponseRedirect

# first part

def review(request , Page):
    return HttpResponseRedirect("/Application2/review")

def reviewPage(request , Page):
    return HttpResponse('You are reading reviews page %s' %Page)

def comments(request):
    return HttpResponse('First comment')

def comments_number(request, number):
    return HttpResponse('your comment has number %s' %number)

def reviewAction(request, page, action):
    if (action == 'edit'):
        return HttpResponse('You are editing page %s' %page)
    if (action == 'delete'):
        return HttpResponse('You are deleting page %s' %page)
    else:
        return HttpResponse('You are discussing page %s' % page)

# another part

def application3(request):
    return  HttpResponse('Application3')

def redirect(request):
    return  HttpResponseRedirect('/Application3/redirected')

def redirected(request):
    return HttpResponse('You were redirected');

def renderHtml(requdest):
    _html = "<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>";
    return HttpResponse(_html);
def htmlFormTemplate(request):
    return render(request,"form1.html");

def formHandler(request):
    if (request.POST):
        return HttpResponse("Method: Post" );
    else:
        return HttpResponse("Method: Get");

# Create your views here.