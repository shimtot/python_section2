import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


#Rest : POST, GET, PUT:UPDATE, REPLACE(FETCH:UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#요청  URL
URL = "https://www.wishket.com/accounts/login/"

#Fake User-Agent 생성
ua = UserAgent()
#print(ua.ie)
#print(ua.chrome)
#print(ua.random)

with requests.Session() as s:
    #URL 연결
    s.get(URL)
    #Login 정보 PayLoad
    LOGIN_INFO = {
        'identification': '****@naver.com',
        'password': '****',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
    print('headers',s.headers)
    #요청
    response = s.post(URL,data=LOGIN_INFO,headers={'UserAgent':str(ua.chrome), 'Referer':'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인
    print('response',response.text)
