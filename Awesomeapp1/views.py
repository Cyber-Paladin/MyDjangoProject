from django.shortcuts import HttpResponse, HttpResponseRedirect

# Create your views here.
# Request 1
def product(request):
    return HttpResponse('application2/product')

# Request 2
def poroduct2019(request):
    return HttpResponse('poroduct2019')

# Request 3
def productFour(request, year):
    return HttpResponse(
        {
            'It’s year basic folder %s' % year
        }

    )

# Request 4
def productFourYM(request, year, month):
    return HttpResponse(
        {
            'It’s months basic folder %s' % year,
            '.%s' % month
        }

    )

# Request 5
def productFourYMD(request, year, month ,day):
    return HttpResponse(
        {
            '.%s' % month,
            'It’s days basic folder %s' % year,
            '.%s' % day,


        }

    )

# Request 6
def productText(request, word):
    return HttpResponse(
        {
            'Your argument is %s' %word

         }
    )

# Request 7
def folder(request):
    return HttpResponseRedirect("/Application2/folder/Product1")

# Request 8
def ReFolder(request , num = "1"):
    if num == "1":
        return HttpResponse('First product page')

# Request 9
def folderProductN(request , numberPage):
    return HttpResponse('Product page with number %s' %numberPage)