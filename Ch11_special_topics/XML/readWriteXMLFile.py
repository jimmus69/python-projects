#! /usr/bin/env python
# readwriteXMLFile.py

def main():
	from xml.etree import ElementTree as ET
	import os
	
	xml_file = os.path.abspath(__file__)
	xml_file = os.path.dirname(xml_file)
	xml_file = os.path.join(xml_file, "our.xml")

	try:
		tree = ET.parse(xml_file)
	except Exception, inst:
		print "Unexpected error opening %s: %s" % (xml_file, inst)
		return
	
	child = ET.SubElement(tree.getroot(), "child")
	child.text = "Three"

	xml_file = os.path.abspath(__file__)
	xml_file = os.path.dirname(xml_file)
	xml_file = os.path.join(xml_file, "our2.xml")
	try:
		tree.write(xml_file)
	except Exception, inst:
		print "Unexpected error writing to file %s: %s" % (xml_file, inst)
		return

if __name__ == "__main__":
	main()
