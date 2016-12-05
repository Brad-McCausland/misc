#helper functions for assignment 4


def gcd(a, b):
	if   a == 0:
		return b
	elif b == 0:
		return a
	else:
		r = a % b
		return gcd(b, r)


###REMOVE###
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
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


