# Bradley McCausland - W01053708
# CS578 - Rrushi
# 12/7/2016
# Assignment 4 - Client

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
s    = socket()
host = gethostname()

try:
	if 'd' in sys.argv[1]:
		DEBUG = True
	if 's' in sys.argv[1]:
		port = input("Enter a port number: ")
		host = input("Enter an IP address: ")
except:
	pass

#randomize private key
k = getrandbits(32)

#randomize AES key
x = getrandbits(32)

#defined constants
p = 4094027087
q = 2047013543

#message to send
message = raw_input('Connection established. Enter message: ')

s.connect((host, port))

#recieve public keys
alpha = int(s.recv(port))
beta  = int(s.recv(port))

y1 = square_and_multiply(alpha, k, p)
s.send(str(y1))

y2 = square_and_multiply(beta, k, p)

#space out send commands. This seems to prevent a bug.
sleep(0.1)

#encrypt AES key
ciphertext = (y2 * x) % p
s.send(str(ciphertext))

#format key to 32 bits
x = format(x, '#034b')[2:]

#init cryptosystem
ctr     = Counter.new(128)
cipher  = AES.new(x, AES.MODE_CTR, counter=ctr)
message = cipher.encrypt(message)

s.send(message)

if DEBUG:
	print "Sending y1: ", str(y1)
	print "Sending encrypted AES key: ", str(ciphertext)
	print "Sending encrypted message: ", message

s.close()
