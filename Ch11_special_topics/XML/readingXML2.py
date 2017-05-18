#! /usr/bin/env python

def main():
	from xml.etree import ElementTree as ET
	
	element = ET.XML( '<root><child val="One" val2="uga"/><child val="Two"/></root>')

	for subelement in element:
		print subelement.tag, subelement.attrib

if __name__ == "__main__":
	main()
