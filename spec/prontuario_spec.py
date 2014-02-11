import unittest
from should_dsl import should
from prontuario import Prontuario
from paciente import Paciente

class prontuarioSpec(unittest.TestCase):
	def it_creates_a_Prontuario_object(self):
		prontuario = Prontuario('001', 'historico', '001')
		prontuario.codProntuario |should| equal_to('001')
		prontuario.historico |should| equal_to('historico')
		prontuario.paciente |should| equal_to('001')


