class Medico:
	def  __init__(self,codMedico, nome, rua, numero, bairro, cidade, uf, telefone, cpf, rg, crm, especialidade, dataNasc, consultas=[]):

		self.codMedico = codMedico
		self.nome = nome
		self.rua = rua
		self.numero = numero
		self.bairro = bairro
		self.cidade = cidade
		self.uf = uf
		self.telefone = telefone
		self.cpf = cpf
		self.rg = rg
		self.crm = crm
		self.especialidade = especialidade
		self.dataNasc = dataNasc
		self.consultas = consultas

	def inserirConsulta(self,consulta):
		self.consultas.append(consulta)

	
	def verificarConsulta(self,consulta):
		return consulta in self.consultas


	def consultaPorMedico(self, codMedico):
		for consulta in self.consultas:
			if consulta.codMedico == codMedico:
				return consulta
