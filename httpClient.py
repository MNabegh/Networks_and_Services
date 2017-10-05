import httplib

conn = httplib.HTTPConnection("localhost:8000")
conn.request("POST", "/testurl", "clientdata")
#conn.send("clientdata")
response = conn.getresponse()
conn.close()

print(response.read())