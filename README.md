# Creating-and-decoding-QR-code-using-Python
QR code by python with objective to send data by encryption to the receiver and decryption it. 
At first user id and password was created by random string selection using random module.
Then joing or concat both id and password with "&" like below.
```
s = myuser+"&"+mypssw
```

After concatenation that string was encrypted using Fernet module.
```
from cryptography.fernet import Fernet
```
PIP installation:-
```
pip install cryptography
```
The process happens like this:-
```
from cryptography.fernet import Fernet


key = Fernet.generate_key()  # Generate a Fernet key.
cipher_suite = Fernet(key)  # Create a Fernet object with that key.
s="Ritabrata Goswami"
encoded_text = cipher_suite.encrypt(s.encode()) #encrypted.
print(encoded_text)
decrypted_text = cipher_suite.decrypt(encoded_text)  #decrypted.
print(decrypted_text)
```

This was done to encrypt actual data being scanned or theft by malacious user.
At the end when it was decrypted we can extracted the actual info. That is here user id and password. 
