# coding: utf-8
from django.utils import unittest
from .templatetags.formatlink import *

class linkFormat(unittest.TestCase):
	def test_simple_link(self):
		string = 'http://www.youtube.com/watch?v=4XytY4FVQKM'
		self.assertEqual(format(string), 'http://www.youtube.com/embed/4XytY4FVQKM')

	def test_complex_link(self):
		string = 'http://www.youtube.com/watch?feature=player_embedded&v=hWvu2vcj0yI'
		self.assertEqual(format(string), 'http://www.youtube.com/embed/hWvu2vcj0yI')

	def test_shortened_link(self):
		string = 'http://youtu.be/fqBlxpKbheg'
		self.assertEqual(format(string), 'http://www.youtube.com/embed/fqBlxpKbheg')

	def test_correct_link(self):
		string = 'http://www.youtube.com/embed/fqBlxpKbheg'
		self.assertEqual(format(string), 'http://www.youtube.com/embed/fqBlxpKbheg')		