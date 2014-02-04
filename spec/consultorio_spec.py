import unittest	
from should_dsl import should
from consultorio import Consultorio

class consultorioSpec(unittest.TestCase):
	def it_creates_a_Consultorio_object(self):
		consultorio = Consultorio('001','103','Pediatria')
		consultorio.codConsultorio |should| equal_to('001')
		consultorio.numero |should| equal_to('103')
		consultorio.descricao |should| equal_to('Pediatria')
		
