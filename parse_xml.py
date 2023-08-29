import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot() # person
# print(root[0].text)
name = tree.findtext('name').strip()
last_name = tree.findtext('last_name').strip()
print(f"Hi {name} {last_name}")
 
#Today     is     ok
# Hi A B
# f string



