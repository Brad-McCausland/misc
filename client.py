from socket import *
from Crypto.Cipher import AES
from Crypto import Random

s = socket()
host = gethostname()
port = 8001

s.connect((host, port))
message = raw_input('Connection established. Enter message: ')

key = b'1234567890123456'
iv = b'0987654321098765'
cipher = AES.new(key, AES.MODE_CFB, iv)
#message = iv + cipher.encrypt(message)
message = cipher.encrypt(message)

print "Encrypted message: ", message

s.send(message)
s.close()

print "Message sent to localhost port 8001"
