import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
