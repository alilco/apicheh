import requests
from flask import *

app = Flask(__name__)

@app.route('/api/info=<email>')
def info(email):
    email1 = email
    try:
        url = 'https://www.instagram.com/api/v1/web/accounts/login/ajax/?hl=ar'
        headers = {
    'Host': 'www.instagram.com',
    'content-length': '322',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Not A(Brand";v="99", "Android WebView";v="121", "Chromium";v="121"',
    'x-ig-www-claim': '0',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-device-id': '0A2B0FB8-243D-4F72-9781-1E456CB34DC8',
    'dpr': '1.75',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Android WebView";v="121.0.6167.178", "Chromium";v="121.0.6167.178"',
    'x-csrftoken': 'PWlSM95SKa80_wY819MwNH',
    'sec-ch-ua-model': '"Lenovo K12"',
    'sec-ch-ua-platform': '"Android"',
    'x-ig-app-id': '1217981644879628',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua-mobile': '?1',
    'x-instagram-ajax': '1011606959',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; Lenovo K12 Build/QOGS30.569-83-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.178 Mobile Safari/537.36',
    'viewport-width': '412',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'x-asbd-id': '129477',
    'origin': 'https://www.instagram.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.instagram.com/accounts/login/?hl=ar',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'csrftoken=PWlSM95SKa80_wY819MwNH;ps_l=0;ps_n=0;ig_did=0A2B0FB8-243D-4F72-9781-1E456CB34DC8;ig_nrcb=1;dpr=1.75;_js_ig_did=0A2B0FB8-243D-4F72-9781-1E456CB34DC8;_js_datr=doHYZdH9fk1pr9niSosv4FFl;mid=ZdiBdgABAAECWGqUQvAJf2vOsjxC',
        }
        data = f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A10%3A1708687786%3AAWdQAA5dXzWQAlVLYNbJZrI8%2FJcAYp1RZbsMXgS9GbYb7RBTnSDKsP12sToWYUeDQn56NuWmG2N%2BOyDdE51YdokpSN2tJl8mK80MmSWdDbdIMXW1Hv%2FB3XzvejomEPng%2B%2Buof2rARLuB85W2yiY%3D&optIntoOneTap=false&queryParams=%7B%22hl%22%3A%22ar%22%7D&trustedDeviceRecords=%7B%7D&username={email}'
        req = requests.post(url, headers=headers, data=data).text
        if '"user":true' in req:
            return '{"user":true}'
        else:
            return '{"False":"email"}'
    except IndexError:
        info(email)
