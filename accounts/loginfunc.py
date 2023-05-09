from typing import Any
from .models import User, Lecture

MAX = 10000000000037 # MAXIMUM number for Hash (prime num) 
BASE_PRIME = 71 # prime number for Hash
ValidDicts = {
     "!": 0,    "@": 1,    "#": 2,    "$": 3,    "&": 4,
    "*": 5,    "0": 6,    "1": 7,    "2": 8,    "3": 9,    "4": 10,    "5": 11,    "6": 12,    "7": 13,    "8": 14,    "9": 15,    "A": 16,    "B": 17,    "C": 18,    "D": 19,    "E": 20,
    "F": 21,    "G": 22,    "H": 23,    "I": 24,    "J": 25,    "K": 26,    "L": 27,    "M": 28,    "N": 29,    "O": 30,    "P": 31,    "Q": 32,    "R": 33,    "S": 34,    "T": 35,    "U": 36,
    "V": 37,"W": 38,    "X": 39,    "Y": 40,    "Z": 41,    "a": 42,    "b": 43,    "c": 44,    "d": 45,    "e": 46,    "f": 47,    "g": 48,    "h": 49,    "i": 50,    "j": 51,    "k": 52,
    "l": 53,    "m": 54,    "n": 55,    "o": 56,    "p": 57,    "q": 58,    "r": 59,    "s": 60,    "t": 61,    "u": 62,    "v": 63,    "w": 64,    "x": 65,    "y": 66,    "z": 67
}

def CheckValidId(id):
    sameIdObj = User.objects.filter(user_id = id)
    if len(sameIdObj) >= 1:
        return 0
    return 1

def CheckValid(user : User) -> int:
    if len(user.user_pw) < 8 or len(user.user_pw) > 15:
        return 0 #too short or too long
    for i in user.user_pw:
        if i not in ValidDicts.keys():
            return 1 #typing the wrong key
    return 2#Its Valid Password

def Encryption(pw : str) -> bool: # HASH Algorithm 
    r, k= 0, 1
    for i in pw:
        r = (r + ValidDicts[i]* k)%MAX
        k = (k*BASE_PRIME)%MAX
    return str(r)
