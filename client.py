from lxml import etree
import xml.etree.ElementTree as ET
from io import BytesIO

# create XML 
root = etree.Element('methodCall')

# another child with text
methodName = etree.Element('methodName')
methodName.text = 'Sum'
root.append(methodName)


params = etree.Element('params')

firstParam = etree.Element('firstParam')
firstParam.text = '3';
params.append(firstParam)

secondParam = etree.Element('secondParam')
secondParam.text = '4';
params.append(secondParam)

root.append(params)



# pretty string
#s = etree.tostring(root, pretty_print=True)
#print s

xmlstr = ET.tostring(root, encoding='us-ascii', method='xml')
print(xmlstr)

root1= ET.fromstring(xmlstr)

name= root1[0].text
first= root1[1][0].text
second= root1[1][1].text
print(name)
print(first)
print(second)

