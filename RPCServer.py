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
		print(self.path)
		# print(self.rfile.read())
		length = int(self.headers['Content-length'])
		self.send_response(200, "OK")
		self.end_headers()
		xmlstr= self.rfile.read(length)
		print(xmlstr) 
		root1= ET.fromstring(xmlstr)
		name= root1[0].text
		first= root1[1][0].text
		second= root1[1][1].text

		if name == "Sum":
			result = Sum(int(first),int(second))
			#result = int(first)+int(second)
		else:
			result = Diff(int(first), int(second))
			#result = int(first)-int(second)

		print (result)

		# Form response tree
		rootR = etree.Element('methodResponse')

		paramsR = etree.Element('params')

		resultN = etree.Element('result')
		resultN.text = str(result);
		paramsR.append(resultN)

		rootR.append(paramsR)
		xmlstrR = ET.tostring(rootR, encoding='us-ascii', method='xml')

		print(xmlstrR)
		self.wfile.write(xmlstrR)




httpd = HTTPServer((ADDR, PORT), RequestHandler)
httpd.serve_forever()