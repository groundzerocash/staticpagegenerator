from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		if isinstance(other, TextNode):
			return (self.text == other.text and
				self.text_type == other.text_type and
				self.url == other.url)
		return False

	def __repr__(self):
		return f"TextNode(text={repr(self.text)}, text_type={repr(self.text_type)}, url={repr(self.url)})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("URL is required for LINK type")
        return LeafNode(tag="a", value=text_node.text, href=text_node.url)
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("URL is required for IMAGE type")
        return LeafNode(tag="img", value="", src=text_node.url, alt=text_node.text)  # Using `text` as alt
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")