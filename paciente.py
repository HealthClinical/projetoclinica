class Paciente:
	def  __init__(self,codPaciente, nome, rua, numero, bairro, cidade, uf, telefone, cpf, rg, dataNasc, convenio, prontuario, consultas=[]):

		self.codPaciente = codPaciente
		self.nome = nome
		self.rua= rua
		self.numero = numero
		self.bairro = bairro
		self.cidade = cidade
		self.uf = uf
		self.telefone = telefone
		self.cpf = cpf
		self.rg = rg
		self.dataNasc = dataNasc
		self.convenio = convenio
		self.prontuario = prontuario
		self.consultas = consultas


	def inserirConsulta(self,consulta):
		self.consultas.append(consulta)


	def verificarConsulta(self,consulta):
		return consulta in self.consultas
		

	def consultarConsulta(self,data):
		for consulta in self.consultas:
			if consulta.data == data:
				return consulta
		return none		

		








			

		
