from listtoxml import listToXml
import csv

listObj = ['AsdfAsdf', 'zxcvxcv', 155, 200, 3]


test = {
	'parentXmlName':
	{
		'_attr':
		{
			'someTag': 0,
			'another': 1
		},
		'_child':
		{
			'loremIpsum':
			{
				'_attr':
				{
					'jetzt': 3,
					'abcd': 2
				},
				'_child':
				{
					'hghg':
					{
						'_attr':
						{
							'rrrr': 4
						}	
					}
				}
			}	
		}
		
	}
}


#xmlObject = listToXml( test, listObj)
#xmlObject.parse()
#xmlObject.recursiveParseRule(test)
#print( xmlObject.getXml() )
#xmlString = xmlObject.getXml()

#outputFile= open('output.txt', 'ab')
#outputFile.write( xmlString )

#print(xmlObject.recursiveParseRule(test))

inputFile = open('input.csv', 'r')
inputList = []

for row in inputFile:
	line = str(row)
	inputList.append( line.split(',') )


for i in inputList:
	xmlObject = listToXml(test, i)
	xmlObject.parse()
	output = open('output.txt', 'ab')
	output.write( xmlObject.getXml() )
