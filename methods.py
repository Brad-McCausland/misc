#helper functions for assignment 4
import sys, hashlib, string, getpass, binascii, struct, cPickle

def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b%a, a)
        return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = gcd(a, m)
    if g != 1:
        print "ruh roh (modinv broke)"
    else:
        return x % m

#From slides
#Compute S = m^t mod n
def square_and_multiply(m, t, n):
	z = 1
	y = m
	binary = bin(t)[2:] #or something

	while len(binary) != 32:
		binary = '0' + binary

	for i in reversed(range(1, len(binary))):
		if binary[i] == "1":
			z = (z*y)%n
		y = (y*y)%n
	return z

#From assignment 2
def passwordToAesKey(password):
    sha256 = hashlib.sha256()
    sha256.update(password)
    
    aesKey = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    el = 0
    for c in list(sha256.digest()):
        if el < 16:
           aesKey[el] = ord(c)
           el = el+1
        
    key = (aesKey[0]<<120) | (aesKey[1]<<112) | (aesKey[2]<<104) | (aesKey[3]<<96) | (aesKey[4]<<88) | (aesKey[5]<<80) | (aesKey[6]<<72) | (aesKey[7]<<64) | (aesKey[8]<<56) | (aesKey[9]<<48)  | (aesKey[10]<<40) | (aesKey[11]<<32) | (aesKey[12]<<24) | (aesKey[13]<<16) | (aesKey[14]<<8) | (aesKey[15]<<0) 
    return str(key)
