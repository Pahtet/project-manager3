#!python3 
# -*- coding: utf-8 -*-

import unittest
import os.path


class JavaEntryTestCase(unittest.TestCase):
  	
 	def setUp(self):
 		self.javafile = JavafileEntryManager('classname','path','new')

	def runTest(self):
   		self.assertTrue(os.path.exists(self.path))


if __name__=="__main__":
	unittest.main()

