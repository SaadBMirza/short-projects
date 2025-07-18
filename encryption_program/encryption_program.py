import random
import string

chars = " " + string.punctutation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letters)
    cipher_texts += key[index]

print(f"original message : {plain_texts}")
print(f"encrypted message: {cipher_text}")

#Decrypt
cipher_text = input("Enter a message to derypt: ")
plain_text = ""

for letter in cipher_text:
    index = chars.index(letters)
    plain_texts += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_texts}")

