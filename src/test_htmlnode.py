import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
	def test_empty_node(self):
		node = HTMLNode("", "")
		leadnode = LeafNode("","")
		assert repr(node) == "HTMLNode(tag='', value='', children=[], props={})"
		assert leadnode.to_html() == '<></>'

	def test_node_with_props(self):
		node = HTMLNode("a", "Click here", props={"href": "https://www.google.com"})
		assert repr(node) == "HTMLNode(tag='a', value='Click here', children=[], props={'href': 'https://www.google.com'})"
		leafnode = LeafNode("test","b")
		assert leafnode.to_html() == '<b>test</b>'

	def test_simple_node(self):
		node = HTMLNode("p", "This is a paragraph.")
		assert repr(node) == "HTMLNode(tag='p', value='This is a paragraph.', children=[], props={})"
	
	def test_parent_node_with_children(self):
		# Test case: Parent node with valid children and tags
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),  # Valid tag 'b'
				LeafNode("span", "Normal text"),  # Valid tag 'span'
				LeafNode("i", "italic text"),  # Valid tag 'i'
				LeafNode("span", "Normal text"),  # Valid tag 'span'
			]
		)
		result = node.to_html()
		expected = "<p><b>Bold text</b><span>Normal text</span><i>italic text</i><span>Normal text</span></p>"
		assert result == expected, f"Expected: {expected}, but got: {result}"

	def test_parent_node_with_children(self):
		# Test case: Parent node with valid children and tags
		node = ParentNode(
			"p",
			[
				LeafNode("Bold text", "b"),  # Valid tag 'b'
				LeafNode("Normal text", None),  # No tag, just text
				LeafNode("italic text", "i"),  # Valid tag 'i'
				LeafNode("Normal text", None),  # No tag, just text
			]
		)
		result = node.to_html()
		expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
		assert result == expected, f"Expected: {expected}, but got: {result}"

	def test_parent_node_with_missing_children(self):
		# Test case: Parent node with missing children (should raise ValueError)
		node = ParentNode("p", None)
		try:
			node.to_html()
		except ValueError as e:
			assert str(e) == "ParentNode must have children", f"Expected ValueError with message 'Children are missing', but got: {str(e)}"

