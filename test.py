import requests
import shutil
import httplib


r = requests.get("http://eee.guc.edu.eg/Courses/Networks/NETW903%20Network%20and%20Services/Assessment/Assignment2.pdf", stream=True)
print r
if r.status_code == 200:
    with open("Assignment2.pdf", 'wb') as f:
		r.raw.decode_content = True
		shutil.copyfileobj(r.raw, f)
