listToXml
=========

A simple library written in Python that converts  a list into an XML based on a dictionary set of rules. This mini library requires lxml to work.

This class will convert a list into XML
	based on a rules dictionary.
	The library comes with a convention for convertion. Assuming
	that you have the next list:
```
	myList = ['john', 'michael', 'therry', 'david', 10, 5, 12, 7]
```
	and you want to generate the following structure of Xml:
```
	<classroom>
		<student name="john" note="10" />
		<student name="therry" note="12" />
		<teachers>
			<teacher name="david" />
		</teachers>
	</classroom>
```
	The rule for generating this is:
```
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
```
	The library provides two constructs:
	_attr - this will be a dictionary with attributes for the current element. The key of the dictionary will represents the attribute name and the value will represent the index from the list.

	_child - this will be the child element

	Calling the object:
```
	listXml = listToXml(rule, myList)
	listXml.parse()
	print( listXml.getXml() ) 
```	
	This will print the indented unicode Xml.

