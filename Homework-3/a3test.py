# ANSHUMAN SINGH
# 2017025
# Section A Group 2

import unittest
from a3 import Djikstra
from a3 import minindex
from a3 import bfs

# TEST cases should cover the different boundary cases.

class testpoint(unittest.TestCase):
	
	def test_Djikstra(self):
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[1,1],[1],[1,1,1],[],[1]]
		self.assertEqual(Djikstra(C,W,0),[0, 1, 1, 2, 2])
		C1 = [[1,2],[3],[1,3,4],[],[3]];W1 = [[5,3],[3],[2,5,6],[],[3]]
		self.assertEqual(Djikstra(C1,W1,0),[0, 5, 3, 8, 9])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[2,1],[1],[2,1,1],[],[1]]
		self.assertEqual(Djikstra(C,W,0),[0, 2, 1, 2, 2])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[7,5],[1],[2,1,1],[],[1]]
		self.assertEqual(Djikstra(C,W,0),[0, 7, 5, 6, 6])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[3,4],[1],[2,4,2],[],[1]]
		self.assertEqual(Djikstra(C,W,0),[0, 3, 4, 4, 6])

		
	def test_bfs(self):
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[1,1],[1],[1,1,1],[],[1]]
		self.assertEqual(bfs(C,W,0),[0,1,1,2,2])
		C1 = [[1,2],[3],[1,3,4],[],[3]];W1 = [[5,3],[3],[2,5,6],[],[3]]
		self.assertEqual(bfs(C1,W1,0),[0,5,3,8,9])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[2,1],[1],[2,1,1],[],[1]]
		self.assertEqual(bfs(C,W,0),[0, 2, 1, 3, 2])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[7,5],[1],[2,1,1],[],[1]]
		self.assertEqual(bfs(C,W,0),[0, 7, 5, 8, 6])
		C = [[1,2],[3],[1,3,4],[],[3]];W = [[3,4],[1],[2,4,2],[],[1]]
		self.assertEqual(bfs(C,W,0),[0, 3, 4, 4, 6])

		
	
if __name__=='__main__':
	unittest.main()