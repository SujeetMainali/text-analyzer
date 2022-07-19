# i have created this file --- sujeet
from cgitb import text
from itertools import count
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    # analyze the text
        return render(request, 'analyze.html', params)

    elif(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to uppercase', 'analyzed_text': analyzed}

        return render(request,'analyze.html',params)

    elif (charcounter == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if index+1<len(djtext) and (not (djtext[index] == " " and djtext[index + 1] == " ")):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
