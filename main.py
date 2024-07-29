








import requests
from flask import Flask,jsonify
app = Flask(__name__)
@app.route("/")
def gmail():
    try:
        host1='1:bJF6fwl6pi8dpEBJYhlgj-LilfRh9A:3QzueA6kta8qieh3'
        u='https://accounts.google.com/lifecycle/flows/signup?flowName=GlifWebSignIn&amp;flowEntry=SignUp&amp;dsh=S-2080027205%3A1708756695873425&amp;theme=glif'
        h={'Host': 'accounts.google.com', 'Cookie': f'__Host-GAPS={host1};', 'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Full-Version': '""', 'Sec-Ch-Ua-Arch': '""', 'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Ch-Ua-Platform-Version': '""', 'Sec-Ch-Ua-Model': '""', 'Sec-Ch-Ua-Bitness': '""', 'Sec-Ch-Ua-Wow64': '?0', 'Sec-Ch-Ua-Full-Version-List': '', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'X-Client-Data': 'CJPuygE=', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://support.google.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Priority': 'u=0, i'}

        AFRITON=requests.get(u,headers=h).text
        at=AFRITON.split('"SNlM0e":"')[1].split('",')[0]
        
        tl=AFRITON.split('?flowName%3DGlifWebSignIn%26TL%3D')[2].split("',")[0]
        return {"at": at,"tl":tl}
        host=requests.get('https://accounts.google.com/v3/signin/_/AccountsSignInUi/data/batchexecute?rpcids=V1UmUe&source-path=%2Fv3%2Fsignin%2Fidentifier&f.sid=9040880579683811499&bl=boq_identityfrontendauthuiserver_20240211.08_p0&hl=en-US&_reqid=343345&rt=c',
                                            headers={
'Cookie': f'__Host-GAPS=1:Z7bv_bm_SFYF0xEj3AP2BTXVHdwr4w:b7ZMMlLrGhrrvUGa',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
            'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
}
).cookies.get_dict()['__Host-GAPS']
        h={'Host': 'accounts.google.com', 
                    'Cookie': f'__Host-GAPS={host}', 
                    'Content-Length': '208', 'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"', 'X-Goog-Ext-278367001-Jspb': '["GlifWebSignIn"]', 'X-Same-Domain': '1', 'X-Goog-Ext-391502476-Jspb': '["S-402181831:1712329129495995","mail"]', 'Sec-Ch-Ua-Mobile': '?0', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36', 'Sec-Ch-Ua-Arch': '""', 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Sec-Ch-Ua-Full-Version': '""', 'Sec-Ch-Ua-Platform-Version': '""', 'Sec-Ch-Ua-Full-Version-List': '', 'Sec-Ch-Ua-Bitness': '""', 'Sec-Ch-Ua-Model': '""', 'Sec-Ch-Ua-Wow64': '?0', 'Sec-Ch-Ua-Platform': '"Windows"', 'Accept': '*/*', 'Origin': 'https://accounts.google.com', 'X-Client-Data': 'CJPuygE=', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'https://accounts.google.com/', 'Priority': 'u=1, i'}

        u1=f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=ink9M&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fbirthdaygender&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&hl=ar&TL={tl}&_reqid=364735&rt=c'
                    
                    

    except:return {"FOX":"@UUYFU" ,"gmail":"error"}

if __name__ == "__main__":
	app.run()
