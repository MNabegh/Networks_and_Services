from lxml import etree
import xml.etree.ElementTree as ET

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
s = etree.tostring(root, pretty_print=True)
print s


tree = ET.parse(s)

print firstParam.tag, firstParam.text