from socket import *
from Crypto.Cipher import AES
from Crypto import Random
from methods import square_and_multiply
from random import getrandbits

s = socket()
host = gethostname()
port = 8001

#private key
k = getrandbits(32)

#AES key
x = 1234567890

#defined constants
p = 4094027087
q = 2047013543

#message to send
message = raw_input('Connection established. Enter message: ')

s.connect((host, port))

alpha = int(s.recv(8001))
print "alpha recieved: ",alpha
beta  = int(s.recv(8001))
print "beta recieved: ",beta

y1 = square_and_multiply(alpha, k, p)

s.send(str(y1))
print "sent y1"

y2 = square_and_multiply(beta, k, p)

print "Y2: ",y2

ciphertext = (y2 * x) % p
print "Ciphertext: ",str(ciphertext)
s.send(str(ciphertext))
s.close()

print "Message sent to localhost port 8001"

#cipher = AES.new(key, AES.MODE_CFB, iv)
#message = cipher.encrypt(message)
