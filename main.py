import requests
from flask import *
from time import time
from hashlib import md5
from fastapi.responses import JSONResponse

app = Flask(__name__)
csrftoken = md5(str(time()).encode()).hexdigest()
@app.route('/api/info/email=<email>')
def info(email):
    email1 = email
    try:
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/signup/email/',
        'user-agent': generate_user_agent(),
        'x-csrftoken': csrftoken
    }
        data = {
        'email': email,
    }
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/check_email/', headers=headers, data=data)
        if 'email_is_taken' in str(response.text):
            return '{"email_is_taken",}'
            data1 ={
            'email': email,
            'email': 'email_is_taken',
            'BY': '@UUYFU'
    }
            return JSONResponse(content=data1)
        else:
            data2 ={
            'email': email,
            'email': ' bad email',
            'BY': '@UUYFU'
    }
            return JSONResponse(content=data2)
    except IndexError:
        info(email)
