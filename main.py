import requests
from flask import *

app = Flask(__name__)

@app.route('/api/info/{email}')
def info(email):
    email1 = email
    try:
        url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
        headers = {
	
		 'Host': 'www.instagram.com',
	
		 'content-length': '22',
	
		 'sec-ch-ua': '"Android WebView";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
	
		 'x-ig-www-claim': '0',
	
		 'sec-ch-ua-platform-version': '"11.0.0"',
	
		 'x-requested-with': 'XMLHttpRequest',
	
		 'dpr': '2',
	
		 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
	
		 'x-csrftoken': 'VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
	
		 'sec-ch-ua-model': '"RMX3231"',
	
		 'sec-ch-ua-platform': '"Android"',
	
		 'x-ig-app-id': '1217981644879628',
	
		 'sec-ch-prefers-color-scheme': 'light',
	
		 'sec-ch-ua-mobile': '?1',
	
		 'x-instagram-ajax': '1010142781',
	
		 'user-agent': 'Mozilla/5.0 (Linux; Android 10; Lenovo K12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
	
		 'viewport-width': '360',
	
		 'content-type': 'application/x-www-form-urlencoded',
	
		 'accept': '*/*',
	
		 'x-asbd-id': '129477',
	
		 'origin': 'https://www.instagram.com',
	
		 'sec-fetch-site': 'same-origin',
	
		 'sec-fetch-mode': 'cors',
	
		 'sec-fetch-dest': 'empty',
	
		 'referer': 'https://www.instagram.com/accounts/signup/email/',
	
		 'accept-encoding': 'gzip, deflate, br',
	
		 'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	
		 'cookie': 'csrftoken=VePQfPfUYHlwXGsHe74dBAYcUJ4dwNR6',
	
		 'cookie': 'mid=ZWlr6AABAAHM2vzmuOS-uwLYhgXX',
	
		 'cookie': 'ig_nrcb=1',
	
		 'cookie': 'datr=5GtpZXKDqnzbfcIZg0FLkRqv',
	
		 'cookie': 'ig_did=B2B00EA7-37E3-45D1-B806-DA1FFFB7D82D',
	
	}
        data = {
            'email':f'{email1}@gmail.com'
        }
        response = requests.post(url, headers=headers, data=data).text
        if '"email_is_taken"' in response:
            return '{"email_is_taken",}'
        else:
            return '{"False":"email"}'
    except IndexError:
        info(email)
