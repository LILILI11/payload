#!/usr/bin/python3
# 1~6 숫자 중 10개를 랜덤으로 출력해서 나온 각 횟수를 구한다.

import random

count =[0] * 6

for n in range(10):
    number=random.randint(1, 6)
    count[number-1] += 1

for i in range(6):
    print(f'{i+1}의 횟수: {count[i]}')



