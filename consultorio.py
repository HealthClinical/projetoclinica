class Consultorio:

	def __init__(self,codConsultorio,numero,descricao, consultas=[]):

		self.codConsultorio = codConsultorio
		self.numero = numero
		self.descricao = descricao
		self.consultas = consultas


	def inserirConsulta(self,consulta):
		self.consultas.append(consulta)

	
	def verificarConsulta(self,consulta):
		return consulta in self.consultas


		
