# /usr/bin/env python3
# Written by Cyn. Copyrighted 2025.

import sys
import argparse
import time
import os
import art #type:ignore

# Prompt for Title
class Prompt:
    title = art.text2art("Cypher",font="tarty1")
    author = art.text2art("Written by Cyn. Copyright 2025",font="fancy69")
logo = Prompt

# Caesar decoder
def Caesar():
    letters = f'{args.ciphertext}'
    plaintext = []
    offset = 96
    for char in letters:
        ctext = ord(char.lower()) - offset
        dcrypt = (ctext -3)%26 + offset
        plain = chr(dcrypt)
        plain = plain.replace("`"," ")
        plaintext.append(plain.upper())
    print(f"Decoded: {''.join(plaintext)}")

# ROT13 decoder
def Rot13():
    letters = f'{args.ciphertext}'
    plaintext = []
    offset = 13
    for char in letters:
        ctext = ord(char.lower())
        dcrypt = ctext + offset
        plain = chr(dcrypt)
        plain = plain.replace("<", " ")
        if dcrypt > 122:
         plain = chr(dcrypt - offset*2)
        plaintext.append(plain.upper())
    print(f"Decoded: {''.join(plaintext)}")

# Atbash decoder
def Atbash():
    letters = f'{args.ciphertext}'
    plaintext = []
    offset = 219
    for char in letters:
        ctext = ord(char.lower())
        dcrypt = offset - ctext
        plain = chr(offset - ctext)
        plain = plain.replace("¬", " ")
        plaintext.append(plain.upper())
    print(f"Decoded: {''.join(plaintext)}")

# Arguments to get parsed.
parser = argparse.ArgumentParser()
parser.add_argument('-ct','--ciphertext', metavar='CIPHERTEXT', nargs='?', required=True, help="The ciphertext to decode")
parser.add_argument('-m','--method', metavar='METHOD', nargs=1, required=False, help="Cipher to use to decode")
args = parser.parse_args()

print(logo.title)
print(logo.author)
print("Decoding string...\n")
time.sleep(1.2)
if args.method:
    if sys.argv[4] == "atbash":
        Atbash()
    if sys.argv[4] == "caesar":
        Caesar()
    if sys.argv[4] == "rot13":
        Rot13()
print("String decoded Successfully.")
