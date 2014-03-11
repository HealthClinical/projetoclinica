import unittest
from should_dsl import should
from medico import Medico
from consulta import Consulta
from consultorio import Consultorio
from convenio import Convenio
from paciente import Paciente
from prontuario import Prontuario
from exame import Exame

class medicoSpec(unittest.TestCase):
	def it_creates_a_Medico_object(self):
		
		
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980',[])
		medico.codMedico |should| equal_to('001')
		medico.nome |should| equal_to('Hugo')
		medico.rua |should| equal_to('Rua B')
		medico.numero |should| equal_to('10')
		medico.bairro |should| equal_to('Centro')
		medico.cidade |should| equal_to('SJB')
		medico.uf |should| equal_to('RJ')
		medico.telefone |should| equal_to('98562312')
		medico.cpf |should| equal_to('00100200379')
		medico.rg |should| equal_to('08956782')
		medico.crm |should| equal_to('1245')
		medico.especialidade |should| equal_to('pediatra')
		medico.dataNasc |should| equal_to('11/05/1980')
		medico.consultas |should| equal_to([])


	def it_inserir_consultas(self): #teste
	
		consultorio = Consultorio('001','103','Pediatria')
		prontuario = Prontuario('001', 'historico', '001')	
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		convenio = Convenio('001', 'Empresa', 'Unimed')		
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)		
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		medico.inserirConsulta(medico)#testando o metodo
		(medico in medico.consultas) |should| equal_to(True) #verifica se consulta esta na lista de consulta


		
	def it_verificar_consultas(self):

		convenio = Convenio('001', 'Empresa', 'Unimed')
		prontuario = Prontuario('001', 'historico', '001')	
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)
		medico = Medico('001', 'Hugo', 'Rua B', '10', 'Centro', 'SJB', 'RJ', '98562312','00100200379', '08956782', '1245', 'pediatra', '11/05/1980')
		consultorio = Consultorio('001','103','Pediatria')
		consulta = Consulta('001',paciente, medico, consultorio, prontuario,'18/02/2014', '13:00', 'Bom')
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', consulta)
			
		medico.inserirConsulta(consulta)#testando o metodo
		medico.verificarConsulta(consulta) |should| equal_to(True) #verifica se paciente esta na lista de consulta


