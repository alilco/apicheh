import requests
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/api/info=<email>')
def check(email):
    try:
        headers = {
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/?lang=en-US&hl=en-gb',
                'user-agent': 'Mozilla/5.0 (Linux; Android 13; ANY-LX2 Build/HONORANY-L22CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.147 Mobile Safari/537.36 InstagramLite 1.0.0.0.145 Android (33/13; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; ar_IQ_#u-nu-latn; 115357035)',
                'x-csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            }

        data = {
            'username': email,
        }

        response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data).text
        if 'showAccountRecoveryModal' in response:
            return {"FOX":"@UUYFU" ,"email":"good"}
        else:
            return {"FOX":"@UUYFU" ,"email":"bad"}

    except:return {"FOX":"@UUYFU" ,"email":"bad"}

if __name__ == "__main__":
	app.run()
