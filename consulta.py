class Consulta:
	def  __init__(self,codConsulta, codPaciente, codMedico, codConsultorio, codProntuario, data, hora, observacao, exames=[]):

		self.codConsulta = codConsulta
		self.codPaciente = codPaciente
		self.codMedico = codMedico
		self.codConsultorio = codConsultorio
		self.codProntuario = codProntuario
		self.data = data
		self.hora = hora
		self.observacao = observacao
		self.exames = exames


		
	def inserirExame(self,exame):
		self.exames.append(exame)

	
	def verificarExame(self,exame):
		return exame in self.exames


	def consultarExame(self,data):
		for exame in self.exames:
			if exame.data == data:
				return exame
		return none	


#done	


	


	


