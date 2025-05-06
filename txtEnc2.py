import random as rd
import string as str
def genRandom(n):
    t = str.ascii_letters + ' ' + str.punctuation + ' ' + str.digits

    return ''.join([rd.choice(t) for x in range(n)])

def encryptMsg(text: str, key: str):
    encryptedTxt = ''
    n = len(key)
    encryptedTxt += ''.join(genRandom(n)+key[x] for x in range(n))
    encryptedTxt += ''.join(genRandom(n) + text[x] for x in range(len(text)))

    return encryptedTxt

def decryptMsg(encryptedTxt: str, key: str):
    isLegit = False
    decryptedTxt = ''
    actKey = ''
    n = len(key)
    actKey += ''.join( encryptedTxt[: n*(n+1) ] [ ( (n+1)*x ) - 1 ] for x in range (1, n+1) )
    isLegit = 1 if actKey == key else 0
    if not isLegit: decryptedTxt = "Your key is wrong!"
    elif isLegit:
        decryptedTxt += ''.join( encryptedTxt [ n*(n+1) : ] [ (( n+1)*x)  -1 ] for x in range ( 1, ( len(encryptedTxt [ n*(n+1) : ]) // (n+1) ) + 1) )
     