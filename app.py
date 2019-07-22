import requests
from bs4 import BeautifulSoup
import time
import random

def banner():
    print(""" 
              ______________________________
            /_   \_____  \\_____  \______  \.
            |   | _(__  <  _(__  <   /    /
            |   |/       \/       \ /    / 
            |___/______  /______  //____/  
                        \/       \/         
            ---------------------------------------------
            -   By Ayman EL Haski                       -
            -   https://www.facebook.com/RyouShinMaster -
            ---------------------------------------------
            WARNING : I do not take responsibility for those who use this script.

    """)

def csrf_skipper(url,session_id,header):
    r = requests.get(url,headers=header)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.select_one('meta[name="csrf-token"]')['content']
    return csrf_token

def main():
    user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    ] 
    banner()
    try:
        e_mail = str(input("Entre your email adress: "))
        password = str(input("Entre your password: "))
    except Exception as err:
        print("Error: {}".format(err))
    else:
        url = "https://candidature.1337.ma/users/sign_in"
        ses = requests.session()
        res = ses.get(url)
        sessionID = ses.cookies['_session_id']
        header = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"en-US,en;q=0.9,fr;q=0.8,ar;q=0.7",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Cookie":"_ga=GA1.2.2033346846.1563723718; _gid=GA1.2.25041123.1563723718; meta=https%3A%2F%2Fcandidature.1337.ma%2F; _session_id="+sessionID,
            "Host":"candidature.1337.ma",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":random.choice(user_agent_list)
        }
        csrf_token = csrf_skipper(url,sessionID,header)
        data = {
            "authenticity_token":csrf_token,
            "user[email]":e_mail,
            "user[password]":password,
            "commit":"Se connecter"
        }
        r = requests.post(url,data=data,headers=header)
        if "1337 veut te voir" in r.text:
            print("Check in is loading ...")
            while True:
                r = requests.get("https://candidature.1337.ma/meetings",headers=header)
                if "Se désinscrire" in r.text:
                    print("I find a check in place!")
                    break
                time.sleep(3)
        elif "Pool is loading" in r.text:
            print("Pool is loading ...")
            while True:
                r = requests.get("https://candidature.1337.ma/piscines",headers=header)
                if "Se désinscrire" in r.text:
                    print("I find a pool place!")
                    break
                time.sleep(3)

if __name__ == "__main__":
    main()