import unittest
from should_dsl import should
from consulta import Consulta
from convenio import Convenio
from prontuario import Prontuario
from medico import Medico
from consultorio import Consultorio
from paciente import Paciente
from exame import Exame

class consultaSpec(unittest.TestCase):
	def it_creates_a_Consulta_object(self):
		
		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)
		consultorio = Consultorio('001','103','Pediatria')
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom',[])
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)
		consulta.codConsulta |should| equal_to('001')
		consulta.codPaciente |should| equal_to(paciente)
		consulta.codMedico |should| equal_to(medico)
		consulta.codConsultorio |should| equal_to(consultorio)
		consulta.codProntuario |should| equal_to(prontuario)
		consulta.data |should| equal_to('18/02/2014')
		consulta.hora |should| equal_to('13:00')
		consulta.observacao |should| equal_to('Bom')
		consulta.exames |should| equal_to([])


	def it_inserir_exames(self): #teste
	
		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)	

		consulta.inserirExame(exame)#testando o metodo
		(exame in consulta.exames) |should| equal_to(True) #verifica se exame esta na lista de consulta



	def it_verificar_exames(self):

		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')	
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		consultorio = Consultorio('001','103','Pediatria')
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)
			
		consulta.inserirExame(exame)#testando o metodo
		consulta.verificarExame(exame) |should| equal_to(True) #verifica se paciente esta na lista de consulta


	def it_consultar_exame(self):
		
		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta )
		exame1 = Exame('002', 'Urina', '20/10/2014', 'beber muita agua', consulta )

		consulta.inserirExame(exame)
		consulta.inserirExame(exame1)	
		consulta.consultarExame('20/10/2014') |should| equal_to(exame1)











		

	
