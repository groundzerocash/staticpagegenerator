import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	def test_url(self):
		node = TextNode("blank", TextType.BOLD, url="monkey.com")
		node2 = TextNode("blank", TextType.BOLD)
		self.assertNotEqual(node, node2)
	def test_enum(self):
		node = TextNode("blank", TextType.ITALIC)
		node2 = TextNode("blank", TextType.BOLD)
		self.assertNotEqual(node, node2)
	def test_enum2(self):
		node = TextNode("blank",TextType.BOLD)
		node2 = TextNode("blank",TextType.BOLD)
		self.assertEqual(node, node2)
	def test_text_type(self):
		text_node = TextNode("Hello, World", TextType.TEXT)
		html_node = text_node_to_html_node(text_node)
		assert html_node.to_html() == "Hello, World", f"Expected 'Hello, World', but got {html_node.to_html()}"
	def test_bold_type(self):
		text_node = TextNode("Bold Text", TextType.BOLD)
		html_node = text_node_to_html_node(text_node)
		assert html_node.to_html() == "<b>Bold Text</b>", f"Expected '<b>Bold Text</b>', but got {html_node.to_html()}"
	def test_link_type_missing_url(self):
		text_node = TextNode("Click Here", TextType.LINK)
		try:
			text_node_to_html_node(text_node)
		except ValueError as e:
			assert str(e) == "URL is required for LINK type", f"Expected 'URL is required for LINK type', but got {str(e)}"





if __name__ == "__main__":
    unittest.main()
