# Author:YSY

import xml.etree.cElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)
