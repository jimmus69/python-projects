#! /usr/bin/env python
# readingXML.py

def main():
	from xml.etree import ElementTree as ET
	
	# ET.XML returns an element object 
	# creates element as an iterator
	element = ET.XML(  """<root> 
                                    <child>One</child>
                                    <child>Two</child>
                              </root>""")

	for subelement in element:
		if subelement.text is not None:
			print subelement.text

if __name__ == "__main__":
main()
