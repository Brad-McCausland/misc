# Bradley McCausland - W01053708
# CS578 - Rrushi
# 12/7/2016
# Assignment 4 - Utility Methods

#Greatest common divisor
def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcd(b%a, a)
        return (g, x - (b//a) * y, y)

#modular inverse
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
	binary = format(t, '#034b')[2:]

	for i in reversed(range(1, len(binary))):
		if binary[i] == "1":
			z = (z*y)%n
		y = (y*y)%n
	return z
