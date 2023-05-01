from typing import Any

MAX = 10000000000037 # MAXIMUM number for Hash (prime num) 
BASE_PRIME = 71 # prime number for Hash
ValidDicts = {

}

def CheckValid(string : str) -> bool:
    if len(string) < 8 or len(string) > 15:
        return 0 #too short or too long
    for i in string:
        if i not in ValidDicts.keys():
            return 0 #typing the wrong key
    return 1#Its Valid Password

def Encryption(pw : str) -> bool: # HASH Algorithm 
    r, k= 0, 1
    for i in pw:
        r = (r + int(i)* k)%MAX
        k = (k*BASE_PRIME)%MAX
    return str(r)

def CheckValidID(idInfo : str) -> bool:
    pass

def CheckValidPW(idInfo : str,pwInfo : str) -> bool:
    pass
