import unittest
from should_dsl import should
from paciente import Paciente
from convenio import Convenio
from prontuario import Prontuario
from consultorio import Consultorio
from medico import Medico
from consulta import Consulta
from exame import Exame

class pacienteSpec(unittest.TestCase):
	def it_creates_a_Paciente_object(self):
		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario,[])
		paciente.codPaciente |should| equal_to('001')
		paciente.nome |should| equal_to('Manoel')
		paciente.rua |should| equal_to('Rua A')
		paciente.numero |should| equal_to('12')
		paciente.bairro |should| equal_to('Centro')
		paciente.cidade |should| equal_to('Campos')
		paciente.uf |should| equal_to('RJ')
		paciente.telefone |should| equal_to('98213484')
		paciente.cpf |should| equal_to('03945698778')
		paciente.rg |should| equal_to('056568311')
		paciente.dataNasc |should| equal_to('12/03/83')
		paciente.convenio |should| equal_to(convenio)
		paciente.prontuario |should| equal_to(prontuario)
		paciente.consultas |should| equal_to([])

		
	def it_inserir_consultas(self): #teste
	
		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		paciente.inserirConsulta(paciente)#testando o metodo
		(paciente in paciente.consultas) |should| equal_to(True) #verifica se consulta esta na lista de consulta


		
	def it_verificar_consultas(self):

		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')	
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		consultorio = Consultorio('001','103','Pediatria')
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)
			
		paciente.inserirConsulta(consulta)#testando o metodo
		paciente.verificarConsulta(consulta) |should| equal_to(True) #verifica se paciente esta na lista de consulta


	def it_consultar_consultas(self):

		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		consulta1 = Consulta('002',paciente, medico, consultorio, prontuario,'20/02/2014', '15:00', 'Ruim')

		paciente.inserirConsulta(consulta)
		paciente.inserirConsulta(consulta1)
		paciente.consultarConsulta('20/02/2014') |should| equal_to(consulta1)






		
		
