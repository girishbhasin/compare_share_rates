import codey
import unittest
import os

class GirishTest(unittest.TestCase):
	def testAsDemoForGirish(self):
		
		self.assertTrue(True)

	def testIfFileExists(self):
		self.assertTrue(os.path.isfile('data.csv'))


	def testIfFileIsReadable(self):
		self.assertTrue(os.access('data.csv',os.R_OK))

if __name__== '__main__':
	unittest.main()

