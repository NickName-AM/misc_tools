from django.shortcuts import render
import random
import string



# Create your views here.

def determineCharset(c):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation
    allChars = upper + lower + digits + symbols
    if c == 'upper':
        return upper
    elif c == 'lower':
        return lower
    elif c == 'digit':
        return digits
    elif c == 'symbol':
        return symbols
    return allChars

def checkError(p):
    try:
        a = int(p)
        if a < 0 or a > 500:
            return "Number between 0 and 500"
    except:
        return "Type a number"
    return


def home(request):
    if request.method == 'POST':
        cSet = request.POST['charset']
        charSet = determineCharset(cSet)

        pLength = request.POST['plength']
        error = checkError(pLength)
        if(error):
            err = {'error': error}
            return render(request, 'pgenerator/home.html', err)
        randomPassword = ''.join(random.choices(charSet, k=int(pLength)))
        return render(request,'pgenerator/home.html', {'randompassword': randomPassword})

    return render(request, 'pgenerator/home.html')
    