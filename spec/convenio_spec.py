import unittest
from should_dsl import should
from convenio import Convenio
from paciente import Paciente
from prontuario import Prontuario


class convenioSpec(unittest.TestCase):
	def it_creates_a_Convenio_object(self):
	
		
		convenio = Convenio('001', 'Empresa', 'Unimed')
		convenio.codConvenio |should| equal_to('001')
		convenio.descricao |should| equal_to('Empresa')
		convenio.tipo |should| equal_to('Unimed')
		convenio.pacientes |should| equal_to([])

	def it_inserir_pacientes(self): #teste
	
		prontuario = Prontuario('001', 'historico', '001')		
		convenio = Convenio('001', 'Empresa', 'Unimed')
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)

		convenio.inserirPaciente(paciente)#testando o metodo
		(paciente in convenio.pacientes) |should| equal_to(True) #verifica se paciente esta na lista de convenio


	def it_verificar_pacientes(self):

		prontuario = Prontuario('001', 'historico', '001')		
		convenio = Convenio('001', 'Empresa', 'Unimed')
		paciente = Paciente('001', 'Manoel', 'Rua A', '12', 'Centro', 'Campos', 'RJ', '98213484', '03945698778', '056568311', '12/03/83', convenio, prontuario)

		convenio.inserirPaciente(paciente)#testando o metodo
		convenio.verificarPaciente(paciente) |should| equal_to(True) #verifica se paciente esta na lista de convenio

		


		
	












		
