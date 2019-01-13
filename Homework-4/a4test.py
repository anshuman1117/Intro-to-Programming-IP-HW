# a4test.py
# Shloak Aggarwal - 2017107 - A2
# Anshuman Singh - 2017025 - A2
#################################

import unittest
from a4 import swapRows
from a4 import RowTransformation
from a4 import MatrixRank

class testpoint(unittest.TestCase):

	def test_MatrixRank(self):
		self.assertEqual(MatrixRank([[0,0,0],[0,1,0],[0,0,0]]),1)
		self.assertEqual(MatrixRank([[10,20],[-20,-30],[30,50],[20,40]]),0)
		self.assertEqual(MatrixRank([[2,4,3],[1,0,9],[9,6,8]]),3)
		self.assertEqual(MatrixRank([[10,20,10],[-20,-30,10],[30,50,0]]),2)
		self.assertEqual(MatrixRank([[1,2,3,4],[4,5,6,7],[7,8,9,9]]),3)

if __name__=='__main__':
	unittest.main()