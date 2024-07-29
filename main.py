








import names,uvicorn
import requests,random
from flask import *
from chinesename import ChineseName
from requests import Session
from re       import search
from flask import Flask,jsonify
from vn_fullname_generator import generator
import indian_names
app = Flask(__name__)
@app.route('/api/gmail=<email>')
def gmail(email):
    try:
        g=email.split('@')[0]
        for i in g[0]:
            if i in '1234567890._':
                    return "erorg" 
            else:
                if '4' in str(len(g)) or '5' in str(len(g))or '3' in str(len(g))or '2' in str(len(g))or '_' in g:
                    pass
                else:
                    host1='1:bJF6fwl6pi8dpEBJYhlgj-LilfRh9A:3QzueA6kta8qieh3'
                    u='https://accounts.google.com/lifecycle/flows/signup?flowName=GlifWebSignIn&amp;flowEntry=SignUp&amp;dsh=S-2080027205%3A1708756695873425&amp;theme=glif'
                    h={'Host': 'accounts.google.com', 'Cookie': f'__Host-GAPS={host1};', 'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Full-Version': '""', 'Sec-Ch-Ua-Arch': '""', 'Sec-Ch-Ua-Platform': '"Windows"', 'Sec-Ch-Ua-Platform-Version': '""', 'Sec-Ch-Ua-Model': '""', 'Sec-Ch-Ua-Bitness': '""', 'Sec-Ch-Ua-Wow64': '?0', 'Sec-Ch-Ua-Full-Version-List': '', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'X-Client-Data': 'CJPuygE=', 'Sec-Fetch-Site': 'same-site', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Referer': 'https://support.google.com/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Priority': 'u=0, i'}

                    AFRITON=requests.get(u,headers=h).text
                    at=AFRITON.split('"SNlM0e":"')[1].split('",')[0]
                    tl=AFRITON.split('?flowName%3DGlifWebSignIn%26TL%3D')[2].split("',")[0]
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
                    
                    ww= names.get_last_name()
                    d1=f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{ww}%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
                    r=requests.post(u1,headers=h,data=d1).text
                    if 'birthdaygender' in r:
                        u2=f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=eOY7Bb&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fbirthdaygender&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&hl=ar&TL={tl}&_reqid=464735&rt=c'
                        d2=f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B1996%2C4%2C1%5D%2C3%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C1%5D%2C%5C%22%3CoGxqbDQCAAYWzUtINs2N3OZY2i2GvWL0ADQBEArZ1KjttJFc2s-CxI6lv_CEONfeEr22ysC-Kj8h-sITKjlfEA_F7RhqKRJzr5RucAz8zQAABHKdAAAAGKcBB7EAR42aaBczFMRSIYu8Q0Kcw5y1t915GDRyzjF8yksPO42yMWVIgD3JlaWVEX99afnbaqzE2ZSigQ7CWw_Hwj4E2dww7V4f2txUVgi40WYS4Eo96vUJqPY3SnLA6wYXxCBoXzvvL6718JrT-An8rOXkLCx6mIbhQyjKpwWV9zOKe9-G4WO4wp7UWHgiEAO0iLAolO4YJrr3CIaH8atnsUk0C8bLAjSUsguqPnG2H-sBLlmwEIHTGm45c0J-LzIs5MAMEhT3RtdRQQ3Ro5tSeOhOUTFNIRs4sclH4d4u1WzpMrlIWZKplMhHjqB2h-l7SFRrQglusRk40g1EbVFIud977oxTJ9-Oia18ZY0un6lh6FxiH2jdTj7FbUNVA2KP54Ean1YJwuHnICmTN69r7umzsrjTNlB0BiQhfSYJ_nsPqYqnWsVIA6N3mLATm6n6uGEgJQd7UcieqNiH0wicI2H-lF3cPON26luRlt5K3K-2JbD6DdZ3Y2eO4cjm8TW5Slz4JK0HFkmgP8tYHZRW5vTYUlqKBJ1EK05d7lmvMgGsU-9PQeqg_X9YF7wsiLI0b4Yu-fYS2G8RX0Kejt0oWTU8w3K7Z0rQoAGc991YmV_mCv0nqsyjgb_EPvWzmNyYxDZLPobr0f7_lMCjetZn0U-GTX2Jp0j0sKdvpa8oZVI453YjNXTI1Bmjcy7QtzuE188VG9iO9voj9KLSiHwX5PJQUWCMKvmRvmwLDcAnZ5LPfnERRWlvIhIGHMbX6PJOTdcqP--VwzF7bmVBiOkYCDz_fSgndB7O01-k6PCs4UbgEsFAtd-AZkxA4rsGyDtnR2gfyt5aEgf7cj85URGTqEzssrHrnj3qHR-VoqN7hp89_LN4PK2-GCWNSbn0pbRw0_901p9hCdfII-RXgCAdd1QmFED1QETCtC_ydrajDnG_-qca3o9TyxzNJ2x2u8U63taF6EE4O2EqgAqUpFazI9HnTKuv3Dv5GM_6cBrLvriRRMmfLwDryFiBpq9ySozjUYtT0azi6gyzEjyY944kNppkE2pTfxaB_0N6PEc0eb5DWKOrxYCGwaURd--jnRfwhmWuRVfpZD2_fPF-aQg-y5Q-2vrusIBc5uPrxD2OELbtz8QHlkTMd9BfSyClFbSUESJ6-v2sPikAsDQdDOkinjF_ltusi_LH1x_MIC1Z6XnKVoYBSYaoDxjp836tcbu2uve5tf-tQQUr_N-Ky4qP6h1JwpohYpV6j2pI745FXPxqwq4-q0E9l543B4q31owADbghsMSM_SVKtUm0w-Y-GCym1nx3kM5yv3Dplc2-Ocqk2_NHNgCBuWrO0SeAWj6car5XxcYPma892jwSkMw0crUK409bnP02tyWWeThNrYoihGj1-iwdFSU-ORgmmyxw7202CYmDH81XHs0PLIPVBoUL754sAKUnuXJMj_tZSf4zy84uoSgRaQEnkBEmIuLpzC-tDzeT6lDRHULoJOxmYS6ZZV_V1teGXJiFQ9DOn-Ak8PszwehMMzI98EQGKQduWjl94bTPpNJqY-cyKqv9qJp9c0c_BhiSmrJMkP0sAAfGiSxbouw1y9EtabhNfKH1WJg_4cCwBrWmv4_rS4OhpBi7gocgFib2HdqUDeYlcosF-fem6NQQ7OjDk4zDjpOQspogfY9EnV46CyhMkClll0M1F_yc1DfyDmRQJp3Ijp0NRtav2w41AlJaFM6LiBS67eG-th_utPR05fcLnmBWdqGMOPl7DsfujIg1bhnJxUOcHYCP7I0pwlc8Ldhl87GBQcEQmNgl9juFOsj4rcZZ8UdBRdT-9VhDomX6Cl3yGbS0dbanITD37TUhFp3hICgt5x1WGEF5p36VW5_PXTwFY2nGFXZJNyyHOZJcXhZNTTZtXNPZVJd1M_FCvfOKqj5Je698-tU-GslAt5nNXoHqYGMzC1enylH-ROSPJFJHnczWcRq9d3VgcYtBqKigFunvZDPWQu2U8Eozvp1gbqrCkO0Pr4MeJHcbY0ZDDCAxFjvAiSj-iKpbtBBcjdIv81x2ZB0xEafzJX-Kijuo1ivM7oQqxYasTqRfV7qJrewetbphRQEq8yDUINS4ddbhUl3Z_6-Aw4PaaDgqm-gXyMnDQ4I0fuKXmbvx8UYr1KAFdR-HDHoKTLEHqO-yKCf_S4dqV86p00aqsiyJ8WMkAK72ufl6hNrhoz_fcp86ayf1baqoqEEQUhH9Rd-mR34orLcBh9y38o1u3JejfHmGOaxEqtilP3qAeT4cnp2UUQhIXsAkmHYCpXvTqfETWEJdUS_c4-AwDmt2j1TNAJjCxit6YVG7P3BdysbGJEuYBZ7u6lNX2UlKdjMPFDK0e5PyhqytkvLnTUp_f4xUH9i2alspPEm2DYR4md1-yTZWpALTaTvChWjqRCCEm0gPRaH5VWrlnbhJ-MS3QGGL-FHoekY_fInHA8HBriTW0xlaV6OjM9ykUWZ0kT4zL64iGoujS7w51sOuehv5aRG2ZQ-4fGmdkWlQmH1Mqd0LslIN6t8YbFUQ3vvbW30JjZoqKUQTrtM7DN4vPxvmGrkuUOHa1n8jYtnfC_pu6R_ab702buqGGUozEI_tF92PVZbgNA7X8xCU9tFStpnJ5cC-a8l0fOXZ4Do90JaWMqLHKx2PThWgNsYB4TIvBlURvCd2fAg9yviNbvNMo3f2idcbY5LjRnHxqweE_zibEn_DWivRdVOCMAdxU9Cb49p9-7lJJRBOSrb4jKsfFIZxjyBhxq4lA0NzUkZ5nivPtz2XbJhkI9aocw2HOMVz2BTIC18VkDbkMbiKFmtXC9fpwag7bFCsA6bAxWNs_eM07XW44q8zdC01zsnZ8nvbDk8AYAbFVSspwqO34thjfAHSskyTZO_-owOrhqeKs0BuFpZ_TbQicDtuf9AdftxvkQhiQ547bklgoZDvpNxLHwzMjw2VSVKCLC66EN3dMPsiJvH02RE-q8aG2sx2G6JJuNGCBLJlqS1uvTToq9ApzLOwO7zcn8HoIBj5aXLNQqVijP1pP9WSXSHRe-JzCYX9TezRbH1sbFkchVXYW1OJXP_5%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
                        r=requests.post(u2,headers=h,data=d2).text
                        if 'steps/signup/username' in r:
                                u=f'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute?rpcids=NHJMOd&source-path=%2Flifecycle%2Fsteps%2Fsignup%2Fusername&f.sid=6778458678089707255&bl=boq_identity-account-creation-evolution-ui_20240403.07_p0&TL={tl}&_reqid=664735&rt=c'
                            
                                d=f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{g}%5C%22%2C1%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C0%2C7681%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'

                                r=requests.post(u,headers=h,data=d).text
                                if 'steps/signup/password' in r:
                                    return "GOOD"
                                else:
                                    return "erorg" 
                        else:
                                return "erorg"
                    else:
                        return "erorg"

    except:return "erorg" 

if __name__ == "__main__":
	app.run()
