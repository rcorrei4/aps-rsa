def gcd(a, b):
	if b == 0:
		return a 
	else: 
		return gcd(b, a%b) 

def xgcd(e, phi):
	n1 = phi
	n2 = phi
	n3 = e
	n4 = 1
	while True:
		n3_new = (n1//n3)*n3
		n4_new = (n1//n3)*n4

		if n1-n3_new < 0:
			n1, n3 = n3, (n1-n3_new)%phi
		else:
			n1, n3 = n3, n1-n3_new
		if n2-n4_new < 0:
			n2, n4 = n4, (n2-n4_new)%phi
		else:
			n2, n4  = n4, n2-n4_new
		if n3 == 1:
			break
	return n4

# Números primos
p = 191
q = 233

# Produto dos primos
n = p*q

# Função ϕ
phi = (p-1)*(q-1)

for e in range(2, phi):
	if gcd(e, phi) == 1:
		break

d= xgcd(e, phi)

def encriptar(m):
	return pow(m, e) % n

def decriptar(c):
	# c^d mod n = m
	return pow(c, d) % n
	
# Mensagem para ser codificada 
# (Não pode ser maior que N mas isso não vai acontecer porque ao transformar cada letra na table ASCII não vai passar de 200)
m = 123

print('Chave pública: ', n, e)
message_in = encriptar(m)
print('Mensagem codificada', message_in)

print('Chave privada: ', n, d)
message_out = decriptar(message_in)
print('Mensagem decodificada', message_out)