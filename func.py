import base64

def codificar(m):
	m_bytes = m.encode('ascii')
	base64_bytes = base64.b64encode(m_bytes)
	base64_message = base64_bytes.decode('ascii')

	return base64_message

def decodificar(m):
	message = base64.b64decode(m)
	message = message.decode('ascii')
	message = message.split(" ")
	message.pop()

	return message

def gcd(a, b):
	# Função para encontrar coprimo de 2 números
	if b == 0:
		return a 
	else: 
		return gcd(b, a%b) 

def xgcd(e, phi):
	# Função para encontrar o inverso do E
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