class Prontuario:
	def __init__(self,codProntuario, historico, paciente, consultas=[]):
		self.codProntuario = codProntuario
		self.historico = historico 
		self.paciente = paciente
		self.consultas = consultas


	def inserirConsulta(self,consulta):
		self.consultas.append(consulta)


	def verificarConsulta(self,consulta):
		return consulta in self.consultas
