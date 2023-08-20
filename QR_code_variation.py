import pyqrcode
import png
from pyqrcode import QRCode
from PIL import Image
from pyzbar import pyzbar
import random
from cryptography.fernet import Fernet


alphabet = "abcdefghijklmnopqrstuvwxyz0123456789%^*$#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user_length = 10
myuser=""
pw_length = 5
mypssw = ""

for i in range(user_length):
    next_index = random.randrange(len(alphabet))
    myuser = myuser + alphabet[next_index]

for i in range(pw_length):
    next_index = random.randrange(len(alphabet))
    mypssw = mypssw + alphabet[next_index]

print('------------------Random generation------------------')
print(myuser)
print(mypssw)
print('-----------------------------------------------------')

s = myuser+"&"+mypssw
key = Fernet.generate_key()  # Generate a Fernet key
cipher_suite = Fernet(key)  # Create a Fernet object with that key
encoded_text = cipher_suite.encrypt(s.encode())
print('---------Encrypted text-----------')
print(encoded_text)
print('----------------------------------')
url = pyqrcode.create(encoded_text)


# url.svg(r"C:\Users\abc123\Desktop\python\QR_code\file\myqr.svg", scale = 8)
url.png(r'C:\Users\...\test111.png', scale = 12, module_color="#3333ff")



#decoding QR

img = Image.open(r'C:\Users\...\test111.png')
output = pyzbar.decode(img)
print('---------Dcrypted text----------')
print("original:- "+str(output[0].data))
print("Dcrypted text:- "+str(cipher_suite.decrypt(output[0].data)))

res=str(cipher_suite.decrypt(output[0].data), 'utf-8').split('&')
print('--------------------')
print(res)
