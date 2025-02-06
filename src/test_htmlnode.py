import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
	def test_empty_node(self):
		node = HTMLNode("", "")
		assert repr(node) == "HTMLNode(tag='', value='', children=[], props={})"
	
	def test_node_with_props(self):
		node = HTMLNode("a", "Click here", props={"href": "https://www.google.com"})
		assert repr(node) == "HTMLNode(tag='a', value='Click here', children=[], props={'href': 'https://www.google.com'})"

	def test_simple_node(self):
		node = HTMLNode("p", "This is a paragraph.")
		assert repr(node) == "HTMLNode(tag='p', value='This is a paragraph.', children=[], props={})"




