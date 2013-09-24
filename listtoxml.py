from lxml import etree
"""
	This class will convert a list into XML
	based on a rules dictionary.
	The library comes with a convention for convertion. Assuming
	that you have the next list:
	myList = ['john', 'michael', 'therry', 'david', 10, 5, 12, 7]
	and you want to generate the following structure of Xml:
	<classroom>
		<student name="john" note="10" />
		<student name="therry" note="12" />
		<teachers>
			<teacher name="david" />
		</teachers>
	</classroom>
	The rule for generating this is:
	rule = {
		'classroom':
		{
			'_attr':
			{
				'name': 0,
				'note': 4
			},
			'_child':
			{
				'teachers':
				{
					'_attr':
					{
						'name': 3
					}
				}
			}

		}
	}

	The library provides two constructs:
	_attr - this will be a dictionary with attributes for the current element. The key of the dictionary will represents the attribute name and the value will represent the index from the list.

	_child - this will be the child element

	Call the object:
	listXml = listToXml(rule, myList)
	listXml.parse()
	print( listXml.getXml() ) 
	
	This will print the indented unicode Xml.
"""
class listToXml:
	def __init__(self, rules, listObj):
		root = list(rules.keys())
		self.xml = etree.Element( root[0] )
		self.rules = rules
		self.listObj = listObj
	'''
	Creating the XML object using lxml library
	'''
	def parseToXml(self, rules, currentNode = None):
		if currentNode == None:
			currentNode = self.xml
		for i in rules:
			node = etree.Element(i)
			if rules.get(i).get('_attr') != None:
				for attr in rules.get(i).get('_attr'):
					value = rules.get(i).get('_attr').get( attr )
					node.attrib[attr] = str( value )
					#node.text = ''
			if rules.get(i).get('_child') != None:
				self.parseToXml( rules.get(i).get('_child'), node )
					
			currentNode.append( node )
	'''
	This method should be called to populate the xml variable
	'''
	def parse(self):
		parsedObject = self.recursiveParseRule(self.rules)
		self.parseToXml(parsedObject)

	'''
	Parse the rules dictionary. This method will replace the number
	of an attribute(which represent the index from a list with values) with 
	the coresponding value from that list.
	'''
	def recursiveParseRule(self, rules):
		for i in rules:
			if rules.get(i).get('_attr') != None:
				for attr in  rules.get(i).get('_attr'):
					if isinstance(rules.get(i).get('_attr').get(attr), int):
						if len(self.listObj) >= rules.get(i).get('_attr').get(attr):
							rules.get(i).get('_attr')[attr] = self.listObj[ rules.get(i).get('_attr').get(attr) ]
							
			if rules.get(i).get('_child') != None:
				self.recursiveParseRule( rules.get(i).get('_child') )
		return rules
	'''
	Get the xml - this method should return an indented xml
	'''
	def getXml(self):
		parser = etree.XMLParser(remove_blank_text = True)
		xml = etree.fromstring( etree.tostring(self.xml), parser)
		return etree.tostring(xml, pretty_print = True)
