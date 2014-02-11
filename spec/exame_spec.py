import unittest
from should_dsl import should
from exame import Exame

class exameSpec(unittest.TestCase):
	def it_creates_a_Exame_object(self):
		exame = Exame('001', 'Sangue', '11/02/2014', 'jejum', '001' )
		exame.codExame |should| equal_to('001')
		exame.descricao |should| equal_to('Sangue')
		exame.data |should| equal_to('11/02/2014')	
		exame.observacao |should| equal_to('jejum')
		exame.consulta |should| equal_to('001')

