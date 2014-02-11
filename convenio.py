class Convenio:
	def  __init__(self,codConvenio, descricao, tipo, pacientes=[]):
		self.codConvenio = codConvenio
		self.descricao = descricao
		self.tipo = tipo
		self.pacientes = pacientes

		def inserirPaciente(self,paciente):
			self.pacientes.append(paciente)


		def verificaPaciente(self,paciente):
			return paciente in self.pacientes
