#!/usr/bin/python3

from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    cmd = request.args.get('cmd', '')

    if not cmd:
        return "No command provided"
    
    return f'Command received"{cmd}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
    