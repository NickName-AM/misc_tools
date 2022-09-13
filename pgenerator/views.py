from django.shortcuts import render
import random
import string

# Some global variables
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation
allChars = upper + lower + digits + symbols

# Create your views here.

def checkError(p):
    try:
        a = int(p)
    except:
        return "Type a number"
    if a < 0 or a > 100:
        return "Number between 0 and 100"
    return


def home(request):
    if request.method == 'POST':
        plength = request.POST['plength']
        error = checkError(plength)
        if(error):
            err = {'error': error}
            return render(request, 'pgenerator/home.html', err)
        randomPassword = ''.join(random.choices(allChars, k=int(plength)))
        return render(request, 'pgenerator/home.html', {'randompassword': randomPassword})

    return render(request, 'pgenerator/home.html')
    