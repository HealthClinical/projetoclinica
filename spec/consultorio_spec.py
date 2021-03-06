import unittest	
from should_dsl import should
from consultorio import Consultorio
from prontuario import Prontuario
from medico import Medico
from paciente import Paciente
from convenio import Convenio
from consulta import Consulta
from exame import Exame

class consultorioSpec(unittest.TestCase):
	def it_creates_a_Consultorio_object(self):
		consultorio = Consultorio('001','103','Pediatria')
		consultorio.codConsultorio |should| equal_to('001')
		consultorio.numero |should| equal_to('103')
		consultorio.descricao |should| equal_to('Pediatria')



	def it_inserir_consultas(self): #teste
	
		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		consultorio.inserirConsulta(consultorio)#testando o metodo
		(consultorio in consultorio.consultas) |should| equal_to(True) #verifica se consulta esta na lista de consulta


		
	def it_verificar_consultas(self):

		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')	
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		consultorio = Consultorio('001','103','Pediatria')
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)
			
		consultorio.inserirConsulta(consulta)#testando o metodo
		consultorio.verificarConsulta(consulta) |should| equal_to(True) 





		
