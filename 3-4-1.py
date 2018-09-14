import sys
import io
from bs4 import BeautifulSoup
import requests

#Rest : POST, GET, PUT:UPDATE, REPLACE(FETCH:UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'login_id':'',
    'login_pwd':''
}

#Session 생성
with requests.Session() as s:
    login_req = s.post('http://domebon.com/?menuType=member&mode=json&act=login',data=LOGIN_INFO)
    #HTML 소스확인
    #print('login_req',login_req.text)
    #Header 확인
    #print('headers',login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('http://domebon.com/?menuType=product&mode=view&prodCode=2018091100419')
        post_one.raise_for_status()

        soup = BeautifulSoup(post_one.text,'html.parser')
        #print(soup.prettify())

        #form > div.prodDetailWrap > div.detailInfo > ul:nth-child(1) > li.prodName
        article = soup.select_one("ul > li.prodName")
        #print(article.)
        for i in article:
            if i.string is not None:
                print(i.string)
