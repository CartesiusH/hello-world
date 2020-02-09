import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

with open('joyero.txt','rb') as f:
    header = f.readline()
    if b'Encrypted' in header:
        print('Already encrypted')
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


#Encrypting the file
f = open('joyero.txt','rb')
data = f.read()
f.close()

fernet = Fernet(key) #Turn key into a fernet object for symmetric (ie. fernet) encryption
token = fernet.encrypt(data)

f2 = open('joyero.txt','wb')
f2.write(b'Encrypted'+ b'\n')
f2.write(token)
f.close()




'''
#Big Scheme
openCrypt
generate password and write in it
closeCrypt

need same key
ie. need same password. so ask 4 password
way to make sure same password is used each time?

understand to make something

#For a simple string
f = Fernet(key)
token = f.encrypt(b"Secret message!")
print(token)

message = f.decrypt(token)
print(message)
'''
