from django.shortcuts import render, redirect
import string
from django.contrib import messages
# Create your views here.

def cipherlist(request):
    return render(request, 'encryption/cipherlist.html')


def xor(request):
    if request.method == 'GET':
        return render(request, 'encryption/xor.html')

    elif request.method == 'POST':
        cipherText = ''
        allChars = "d=,8hal:W;SvU{3bF0VH\\[.nQ?Y^>/L6R#yM<\"IqPp_E4iA%sN7x'em|f2 c~z}JruGjkOK`&$]9TZwDXCt@5g()-!1*B+o"
        l = len(allChars)

        string = request.POST['text']
        key = request.POST['key']
        if len(string) < 1 or len(key) < 1:
            messages.error(request, 'Atleast type something')
            return redirect('encryption-xor')

        if len(string) != len(key):
            messages.error(request, 'Length of text and key should be same')
            return redirect('encryption-xor')

        charKey = zip(list(string), list(key))

        for c, k in charKey:
            cipherChar = allChars[(allChars.index(c) ^ allChars.index(k)) % l]
            cipherText+=cipherChar

        return render(request, 'encryption/xor.html', {'data': cipherText})