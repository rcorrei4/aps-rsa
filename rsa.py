from func import *

# Números primos
p = 191
q = 233

# Produto dos primos
n = p*q

# Função ϕ
phi = (p-1)*(q-1)

# Encontrar um número para o E (deve ser 1 < E < N que é coprimo de N)
for e in range(2, phi):
	if gcd(e, phi) == 1:
		break

# Inverso de E
d = xgcd(e, phi)

def encriptar(m):
	return pow(m, e) % n

def decriptar(c):
	# c^d mod n = m
	return pow(c, d) % n
	
# Mensagem para ser codificada 
m = input('Digite a mensagem a ser criptografada: ')
# Transforma cada letra para o seu número da tabela ASCII
m = [ord(x) for x in m]

chave_publica = codificar(str(n)+" "+str(e))

print('Chave pública: ', chave_publica)

# Criptografa cada letra da mensagem
mensagem_in = ""
for i in m:
	mensagem_in += str(encriptar(i))+" "

# Transforma todos as letras critografadas em uma única string codificada em base64
mensagem_codificada = codificar(mensagem_in)
print('Mensagem codificada', mensagem_codificada)


chave_privada = codificar(str(n)+" "+str(d))
print('Chave privada: ', chave_privada)

message = decodificar(mensagem_codificada)
message_out = ""

for i in message:
	message_out += chr(decriptar(int(i)))
print('Mensagem decodificada', message_out)
