

class Conta():
	def __init__(self, numero, nome, saldo, limite):
		super(). __init__(nome,numero)
		self._numero = numero
		self._titular = nome
		self._saldo = saldo
		self._limite = limite

	def get_saldo(self):
		return self._saldo

	def set_saldo(self, saldo):
		self._saldo = saldo

	def get_titular(self):
		return self._titular

	def set_titular(self, titular):
		self._titular = titular

	def deposita(self, valor):
		self.saldo += valor

	def saca(self, valor):
		if (self.saldo < valor):
			return False
		else:
			self.saldo -= valor
			return True

	def transfere_para(self, destino, valor):
		retirou = self.saca(valor)
		if (retirou == False):
			return False
		else:
			destino.deposita(valor)
			return True

	def extrato(self):
		print("numero:	{}	\nsaldo:	{}".format(self.numero, self.saldo))

