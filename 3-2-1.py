import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

s = requests.Session()
#r = s.get('http://domebon.com')   #PUT, DELETE, GET, POST
#print('1',r.text)
#r = s.get('http://httpbin.org/cookies',cookies={'from':'myName'})
#print(r.text)

url = "http://httpbin.org/get"
headers = {'from':'myName'}
#r = s.get(url,headers=headers)
#print(r.text)
s.close()

with requests.Session() as s:
    r = s.get("http://httpbin.org/get")
    print(r.text)
