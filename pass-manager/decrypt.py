import base64
import os
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

with open('passBox.txt','rb') as f:
    header = f.readline()
    if not b'Encrypted' in header:
        print('Already decrypted')
        exit()

print('Enter the master password')
answer = input()
password = answer.encode()

#Derives key from password using salt
salt = b'\xea\x7f\xb3gN\xe3\x98*\x05\x95\xf7\xd8\xac\t\x81\xb8'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

#Decrypting the file
f = open('passBox.txt','rb')
next(f)
data = f.read()
f.close()

fernet = Fernet(key)
try:
    message = fernet.decrypt(data)
    f2 = open('passBox.txt','wb')
    f2.write(message)
    f2.close()
except cryptography.exceptions.InvalidSignature:
    quit()
except cryptography.fernet.InvalidToken:
    print('Wrong password')
    quit()

'''
except InvalidToken:
    print('Wrong passowrd')
except NameError:
    print('Wrong password')

except cryptography.exceptions.InvalidSignature:
    print('Wrong password')
except cryptography.fernet.InvalidToken:
    print('Wrong password')
'''