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

class LeafNode(HTMLNode):
	def __init__(self, value, tag=None, props=None):
		super().__init__(tag, props)
		if value is None:
			raise ValueError('LeafNode must have value')
		self.value = value
		self.tag = tag
		self.props = props

	def to_html(self):
		if self.tag is None:
			return self.value

		html = f'<{self.tag}>{self.value}</{self.tag}>'
		return html

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,children,props)
        
        self.tag = tag
        self. children = children
        self.props = props
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode must have tag')
        elif self.children is None:
            raise ValueError('ParentNode must have children')
        
        children_html = ''.join(child.to_html() for child in self.children)
        return f"<{self.tag}>{children_html}</{self.tag}>"