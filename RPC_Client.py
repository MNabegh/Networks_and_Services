from lxml import etree
import xml.etree.ElementTree as ET
from io import BytesIO
import httplib

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


xmlstr = ET.tostring(root, encoding='us-ascii', method='xml')



conn = httplib.HTTPConnection("localhost:8000")
conn.request("POST", "/testurl", xmlstr)
#conn.send(xmlstr)
response = conn.getresponse()
print(response)
root2= ET.fromstring(response)
result= root2[0].text
conn.close()
print(result)
