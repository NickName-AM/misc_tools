from django.shortcuts import render, redirect
import string
from django.contrib import messages
import random

# Create your views here.
ALLCHARS = "d=,8hal:W;SvU{3bF0VH\\[.nQ?Y^>/L6R#yM<\"IqPp_E4iA%sN7x'em|f2 c~z}JruGjkOK`&$]9TZwDXCt@5g()-!1*B+o"
ALLCHARS_LEN = len(ALLCHARS)

# Home page - List of ciphers
def cipherlist(request):
    return render(request, 'encryption/cipherlist.html')

# XOR cipher
def xor(string, key):
    cipher_text = ''
    error = ''
    l = len(ALLCHARS)
    if len(string) < 1 or len(key) < 1:
        error = 'Atleast type something'
    if len(string) != len(key):
        error = 'Length of text and key should be same'
    charKey = zip(list(string), list(key))
    for c, k in charKey:
        cipher_char = ALLCHARS[(ALLCHARS.index(c) ^ ALLCHARS.index(k)) % l]
        cipher_text+=cipher_char
    return [cipher_text, error]

# XOR cipher request handler
def xor_handler(request):
    if request.method == 'GET':
        return render(request, 'encryption/xor.html')

    elif request.method == 'POST':
        string = request.POST['text']
        key = request.POST['key']
        cipher_text, error = xor(string, key)
        if error:
            messages.error(request, error)
            return redirect('encryption-xor')
        return render(request, 'encryption/xor.html', {'data': cipher_text})


# By b0t
letters_txt =[
r'hF\#Yxo?]r!~Pc/5BEC2t;%XbA0`+>[y=Q9/3@{^w6Tik( mO1SK_ZjUNG)$L|sV8v4<*WDn.qa*l,}H:-dzJIR7g&uMfpe',
r'uBcLnA-+sy@7l|Zvo$_) 9a4~p8^P>%#hRf5I.JE=[]{?z0NGCVTOM!Dm6e2ik/`Ytb:XH\w;j/FrSx3<(1*Wg&dKq}Q*,U',
r'EJ]|yfXwT98dusqM[:=6>i;@Dp2`$RGAK%(I3mrh7x.t1n<Ho\5*UF)W {VB+#vejPOl_ac0?g&b!LSC~4z*-,ZN/}QY/^k',
r'E1ojW7f\/3iG^,ar%(e@`6H<_SVZR~{& $Y?q/bB2cJ+Ns)QU;[!u*>PT#l=I98t.OyKXdF}xCkgn]wmz*-Lh50:v4DMAp|',
r'G#@pItz/jiEw>CvcJ(rU*mTR^l9\3=+shd-_x 7ZWu65)B~{;?X%eQ[Yfn}LD1bFK<!|PqyS:k]V$&.gM0H2N8`,4*OAa/o',
r'l!/r:6TE_#j2&u8tc>PC|Xb;=Fv/on-xG9}0]LI)*(d<\.51p@ZBe+f?,3 MDmJSOzy4gQ*i[^q%$AVUkRwW`h{H~Ns7KYa',
r'|lM&(^5y?*;Fv6wBfP={4j73Z/T# RLA.Q1CUE@X,<u]>902sb/gHm}heS:`xV$N)zDdrqJ~ac%![-pi+o*Wn\GK8IYk_tO',
r'|m=j^&o.;q)PFhO\JH<STgNv~IMR5`+-p1a*[98bz*Uc(Y:n,0ZfLC}l>_Q%@siGtu6?BArX4d${DeE7 w2#W/3yV/K]xk!',
r'me*a\Jp2 %+#KINTS!)Es`h=/{~]@g<:0G(D56$zBVC&Rd;rYM7b.tqo^w>yukc*LQ[Zxnl8W3X9|}F?A,Uijv14P_/HfO-',
r'+.,sb4/rP<kz)@#:V\oG!8LDA$IcmTWaRj{^?MF&UY(u_wytqN/*7-|9x;fiE*Bl`Khe~QJ[pvn}3S1CZ>%X=dg2O]H065 ',
]
# b0t Encrypt
def bot_encrypt(message, tempkey):
    key=1
    for loop2 in str(tempkey):
        key=ord(loop2)+key
    for digit in str(key):
        key+=int(digit)

    char_num=40
    LETTERS_chooser=letters_txt
    LETTERS_rng=random.randint(0,8)

    LETTERS_choose=(LETTERS_chooser[int(LETTERS_rng)])
    LETTERS=LETTERS_choose

    for chooser in range(LETTERS_rng):
       char_num+=1
    char_letter=(chr(char_num))

    random_encry=random.randint(1,3)

    letter_for_encry = 33 + random_encry

    encrypted =str()
    for chars in str(message):
        if chars in LETTERS:
            num = LETTERS.find(chars)

            num =(num+key)%95

            encrypted +=  LETTERS[num:num+random_encry]

    encrypted= encrypted + chr(letter_for_encry) + char_letter
    return encrypted

# b0t Decrypt
def bot_decrypt(message, tempkey):
    key=1
    for loop2 in str(tempkey):
        key=ord(loop2)+key

    for digit in str(key):
        key+=int(digit)

    decrypted =str()

    n=0
    m=1
    user_list=[]
    words=[]
    random_var=0
    main_var=0

    char=message[-1]
    LETTERS_choosing=ord(char)-40
    message=message.strip(message[len(message)- 1])

    #for random_var
    char_random_encry = message[-1]
    random_var = ord(char_random_encry) - 33
    message=message.strip(message[len(message)- 1])

    print(message)
    LETTERS_chooser=letters_txt
    LETTERS_choose=(LETTERS_chooser[int(LETTERS_choosing)])
    LETTERS=LETTERS_choose

    i=random_var-1
    main_var = random_var-1
    for chars in str(message):
        if main_var == i:
            if chars in LETTERS:
                num = LETTERS.find(chars)

                num =(num-key)%95

                decrypted +=  LETTERS[num]

                i=0
        else:
            i=i+1        
    return decrypted

# b0t encryption/decryption handler
def botcrypt_handler(request):
    if request.method == 'GET':
        return render(request, 'encryption/botcrypt.html')
    elif request.method == 'POST':
        crypt_option = request.POST['cryptoption']
        text = request.POST['text']
        key = request.POST['key']
        # if nothing is given
        if len(text) < 1 or len(key) < 1:
            return redirect('encryption-botcrypt')
        
        if crypt_option == 'encrypt':
            data = bot_encrypt(text, key)
        else:
            data = bot_decrypt(text, key)
        return render(request, 'encryption/botcrypt.html', {'data': data})

# Caesar Cipher
def caesarcipher_encrypt(string, key):
    cipher_text=''
    for i in string:
        charac = ALLCHARS[(ALLCHARS.index(i) + key) % ALLCHARS_LEN]
        cipher_text += charac
    return cipher_text

def caesarcipher_decrypt(string, key):
    cipher_text=''
    for i in string:
        charac = ALLCHARS[(ALLCHARS.index(i) - key) % ALLCHARS_LEN]
        cipher_text += charac
    return cipher_text

def caesarcipher_handler(request):
    if request.method == 'GET':
        return render(request, 'encryption/caesarcipher.html')
    elif request.method == 'POST':
        crypt_option = request.POST['cryptoption']
        text = request.POST['text']
        key = request.POST['key']
        # if nothing is given
        if len(text) < 1 or len(key) < 1:
            return redirect('encryption-caesarcipher')
        try:
            key = int(key)
        except:
            messages.error('Enter an integer(for key).')
            return redirect('encryption-caesarcipher')
        
        if crypt_option == 'encrypt':
            data = caesarcipher_encrypt(text, key)
        else:
            data = caesarcipher_decrypt(text, key)
        return render(request, 'encryption/caesarcipher.html', {'data': data})