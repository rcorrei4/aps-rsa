def gcd(a, b):
	if b == 0:
		return a 
	else: 
		return gcd(b, a%b) 

def xgcd(x, y):
	if y == 0:   
		return x, 1, 0
			 
	d, a, b = xgcd(y, x % y)  
	 
	return d, b, a - (x // y) * b

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

_, d, _ = xgcd(e, phi)
if d < 0:
	d= d + phi

def encriptar(m):
	return pow(m, e) % n

def decriptar(c):
	# c^d mod n = m
	return pow(c, d) % n
	
# Mensagem para ser codificada
m = 321321

print('Chave pública: ', n, e)
message_in = encriptar(m)
print('Mensagem codificada', message_in)

print('Chave privada: ', n, d)
message_out = decriptar(message_in)
print('Mensagem decodificada', message_out)