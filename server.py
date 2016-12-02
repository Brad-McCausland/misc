from socket import *
from Crypto.Cipher import AES
from Crypto import Random
from methods import square_and_multiply
from random import getrandbits

s = socket()
host = gethostname()
port = 8001
s.bind((host, port))

key = getrandbits(256)
print key
print key + 10
print "Starting server on host", host
s.listen(0)

while True:
	c, addr = s.accept()
	print "Message from ", addr, ":",
	#key = b'1234567890123456'
	cipher = AES.new(key, AES.MODE_CFB, iv)
	#message = iv + cipher.encrypt(message)
	message = cipher.decrypt(c.recv(8001))

	print message
	c.close()
