# -*- coding: utf-8 -*-
"""encryption.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tuIOitPcPII4qUET1-SavYekau65Vj8M
"""

import random

def encrypt(key, n, plaintext):
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Return the array of bytes
    return cipher


if __name__ == '__main__':
    print("===========================================================================================================")
    print("===========================================RSA ENCRYPTED===================================================")
    print(" ")

    x = input(" - Enter a message to encrypt: ")
    e = int(input(" - Enter a public key: "))
    n = int(input(" - Enter Modulo Invers: "))
    print(" - Encryption code with public key ", e, " . . . ")
    encrypted_msg = encrypt(e, n, x)
    
    print(" - Your encrypted message is: ", ' '.join(map(lambda x: str(x), encrypted_msg)))
    
    print(" ")
    print("===========================================================================================================")
    print("===========================================================================================================")