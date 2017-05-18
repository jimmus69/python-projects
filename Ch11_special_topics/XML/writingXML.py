#! /usr/bin/env python

def main():
	from xml.etree import ElementTree as ET
	
	root_element = ET.Element("root")

	child = ET.SubElement(root_element, "child")
	child.set("val","One")
	child.set("val2","uga")

	child = ET.Element("child")
	child.set("val","Two")
	root_element.append(child)

	print ET.tostring(root_element)

if __name__ == "__main__":
	main()
