# Created by Abhinandan Mishra

#import httpresponse
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('''<ul><a href="/">Home</a>
                            <a href="capitalizefirst">Capitalize</a>
                            <a href="box">Box Page</a>
                            <a href="acss">Analyze CSS</a></ul>''')

def submit(request):
    nam = request.POST.get("name", 'Abhi')
    bran = request.POST.get("branch", 'IT')
    intr = request.POST.get("intro", "default")
    params = {'name': nam, 'branch': bran, 'intro': intr}

    return render(request, 'details.html', params)

def capfirst(request):
     #return HttpResponse("capitalize first")
     return render(request,'index.html')


def box(request):
    # return HttpResponse("capitalize first")
    return render(request, 'box.html')

def analyzecss(request):
     #return HttpResponse("capitalize first")
     return render(request,'analyzecss.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase=request.POST.get('uppercase', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # for uppercase
    elif uppercase == "on":
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif extraspaceremover =="on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==' ' and djtext[index+1]==' '):
                analyzed = analyzed + char
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcounter == "on":
        # numchr=len(djtext)
        numchr=0
        for char in djtext:
            if char != " ":
                numchr+=1

        params = {'purpose': 'Count of Characters', 'numchr': numchr}
        return render(request, 'analyze.html', params)



    else:
        return HttpResponse('Error')


def third(request):
     #return HttpResponse("capitalize first")
     return render(request,'third.html')