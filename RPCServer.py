from lxml import etree
import xml.etree.ElementTree as ET
from io import BytesIO
import httplib
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

ADDR = "localhost"
PORT = 8080


def Sum(first,second):
		result = first+second
		return result

def Diff(first,second):
	result = first-second
	return result

class RequestHandler(BaseHTTPRequestHandler):  

	def do_POST(self):

		# Recieve message, remove headers and extract xml body
		length = int(self.headers['Content-length'])
		self.send_response(200, "OK")
		self.end_headers()
		xmlstr= self.rfile.read(length)

		# change xml message to DOM tree, extract the method name and the operands from it	
		root1= ET.fromstring(xmlstr)

		methodName= root1[0].text
		firstOperand= root1[1][0].text
		secondOperand= root1[1][1].text



		# Determine which method to perform, perform it and save the result
		if methodName == "Sum":
			result = Sum(int(firstOperand),int(secondOperand))
			
		else:
			result = Diff(int(firstOperand), int(secondOperand))
			

		

		# Form response DOM tree and change it to xml message
		rootResponse = etree.Element('methodResponse')
		paramsResponse = etree.Element('params')
		resultValue = etree.Element('result')
		resultValue.text = str(result);
		paramsResponse.append(resultValue)
		rootResponse.append(paramsResponse)
		xmlstrResponse = ET.tostring(rootResponse, encoding='us-ascii', method='xml')

		#send the xml message as an http response
		self.wfile.write(xmlstrResponse)




httpd = HTTPServer((ADDR, PORT), RequestHandler)
httpd.serve_forever()