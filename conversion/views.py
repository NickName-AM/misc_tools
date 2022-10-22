from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'conversion/home.html')

## Number to roman
def convert_to_roman(num):
    str_num = str(num)
    num_str = ''
    length = len(str_num)
    i = 0
    while i < length:
        base = 10 ** (length-i-1)
        num_str += rule_conversion(int(str_num[i]), base)
        i += 1
    return num_str

def rule_conversion(num, base):
    first = ''
    r_a = {
        1000: 'M',
		500: 'D',
		100: 'C',
		50: 'L',
		10: 'X',
		5: 'V',
		1: 'I'
    }
    rules = {
    	1:[1],
    	2:[1,1],
    	3:[1,1,1],
    	4:[1,5],
    	5:[5],
    	6:[5,1],
    	7:[5,1,1],
    	8:[5,1,1,1],
    	9:[1,10]
   	}

    if num == 0:
        return ''
    
    for i in rules[num]:
        first += r_a[i*base]
    return first

def num_to_roman(request):
    if request.method == 'GET':
        return render(request, 'conversion/numtoroman.html')
    elif request.method == 'POST':
        try:
            num = int(request.POST['num'])
        except TypeError:
            messages.error(request, 'Should be an integer.')
            return redirect('num-to-roman')

        if not 0 < num < 4000:
            messages.error(request, 'Integer should be in the range of 1 to 3999.')
            return redirect('num-to-roman')
        
        roman = convert_to_roman(num)
        return render(request, 'conversion/numtoroman.html', {'data': roman})

# End number to roman