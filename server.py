# Bradley McCausland - W01053708
# CS578 - Rrushi
# 12/7/2016
# Assignment 4 - Server

import sys
from socket import *
from methods import *
from random import getrandbits
from time import sleep

from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto import Random

DEBUG = False
port = 8001
s = socket()
host = gethostname()

#parse options
try:
	if 'd' in sys.argv[1]:
		DEBUG = True
	if 's' in sys.argv[1]:
		port = input("Enter a port number: ")
except:
	pass

s.bind((host, port))

#randomize private key
a = getrandbits(32)

#defined constants
p = 4094027087
q = 2047013543
g = 1659252438 #alpha

print "Starting server on host", host
s.listen(0)

#server loop
while True:
	c, addr = s.accept()
	
	c.send(str(g))

	beta = square_and_multiply(g, a, p)
	c.send(str(beta))
	sleep(0.1)
	c.send(str(p))

	y1 = int(c.recv(port))

	y2 = square_and_multiply(y1, a, p)

	#recover encrypted AES key
	ciphertext = c.recv(port)
	print ciphertext
	#sometimes fails on this line
	ciphertext = int(ciphertext)

	#Decrypt AES key
	x = (ciphertext * modinv(y2, p)) % p

	#format key to 32 bits
	x = format(x, '#034b')[2:]

	#init cryptosystem
	ctr = Counter.new(128)
	cipher = AES.new(x, AES.MODE_CTR, counter=ctr)
	message = cipher.decrypt(c.recv(port))

	if DEBUG:
		print "Sending g:", str(g)
		print "Sending beta:", str(beta)

	print "Decrypted message: ", message
	c.close()
