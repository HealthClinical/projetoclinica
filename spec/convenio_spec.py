import unittest
from should_dsl import should
from convenio import Convenio

class convenioSpec(unittest.TestCase):
	def it_creates_a_Convenio_object(self):
		convenio = Convenio('001', 'Empresa', 'Unimed')
		convenio.codConvenio |should| equal_to('001')
		convenio.descricao |should| equal_to('Empresa')
		convenio.tipo |should| equal_to('Unimed')


