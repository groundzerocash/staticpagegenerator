class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children if children else []
		self.props = props if props else {}
	
	def to_html(self):
		raise(NotImplementedError)

	def props_to_html(self):
		return ' '.join(f'{key}={value}' for key, value in self.props.items())

	def __repr__(self):
		return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={repr(self.children)}, props={repr(self.props)})"

