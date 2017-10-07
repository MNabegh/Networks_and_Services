from lxml import etree
import xml.etree.ElementTree as ET
from io import BytesIO
import httplib

# Create DOM tree
root = etree.Element('methodCall')

# Add method name to tree
methodName = etree.Element('methodName')
methodName.text = raw_input("Enter Sum to perform Summation or Diff to perform Subtraction\n")
root.append(methodName)

# Create parameters element
params = etree.Element('params')

#Create first operand element
firstParam = etree.Element('firstParam')
firstParam.text = raw_input("Enter the value of the first operand\n");
params.append(firstParam)

#Create second operand element
secondParam = etree.Element('secondParam')
secondParam.text = raw_input("Enter the value of the second operand\n");
params.append(secondParam)

# Add to tree message
root.append(params)

# Change DOM to xml format
xmlstrRequest = ET.tostring(root, encoding='us-ascii', method='xml')


# Form HTTP connection and send request
conn = httplib.HTTPConnection("localhost:8080")
conn.request("POST", "/testurl", xmlstrRequest)

# recieve response and extract xml message
response = httplib.HTTPResponse.read(conn.getresponse())

# Change xml message to DOM tree and extract result
root2= ET.fromstring(response)
result= root2[0][0].text

# Close connection and print result
conn.close()
if methodName.text == "Sum":
	print ("The sum value is " + result)
			
else:
	print ("The difference value is " + result)