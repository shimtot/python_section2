import sys
import io
from bs4 import BeautifulSoup
import requests
import urllib.parse as rep
import urllib.request as req
import os

#Rest : POST, GET, PUT:UPDATE, REPLACE(FETCH:UPDATE, MODIFY), DELETE

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#로그인 유저정보
LOGIN_INFO = {
    'log': 'shimtot',
    'pwd': '****',
    'user-submit': rep.quote_plus('로그인'),
    'user-cookie': 1
}

#Session 생성
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F',data=LOGIN_INFO)
    #HTML 소스확인
    #print('login_req',login_req.text)
    #Header 확인
    #print('headers',login_req.headers)

    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/members/shimtot/')
        post_one.raise_for_status()

        soup = BeautifulSoup(post_one.text,'html.parser')
        #print(soup.prettify())

        #u_0_1 > div._1dro._2ph-.clearfix > a > img
        badges = soup.select("div._1dro._2ph-.clearfix > a > img")
        #print(article.)
        for i,z in enumerate(badges,1):
            fullFileName = os.path.join("c:/Django/",str(i)+'.jpg')
            #print(z)
            freq.urlretrieve(z['src'],fullFileName)
