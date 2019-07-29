# -*- coding: UTF-8 -*-
from fbchat import Client
from fbchat.models import *
import requests
import json
from bs4 import BeautifulSoup
import time

login_url = "https://candidature.1337.ma/users/sign_in"

def get_token(headers):
    global login_url
    response = requests.get(login_url,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.select_one('meta[name="csrf-token"]')['content']

def log_in(email,pass_word):
    global login_url
    with requests.Session() as session:
        session.get(login_url)
        headers = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"en-US,en;q=0.9,fr;q=0.8,ar;q=0.7",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"_ga=GA1.2.2033346846.1563723718; _gid=GA1.2.25041123.1563723718; meta=https%3A%2F%2Fcandidature.1337.ma%2F; _session_id="+session.cookies['_session_id'],
        "Host":"candidature.1337.ma",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
        }
        authenticity_token = get_token(headers)
        data = {
            "authenticity_token":authenticity_token,
            "user[email]":email,
            "user[password]":pass_word,
            "commit":"Se connecter"
        }
        r_login = session.post(login_url,data=data,headers=headers)
        return r_login.text


e_mail = str(input("Please entre your school email :"))
pass_word = str(input("Please entre your school password:"))
face_email = str(input("Please entre your facebook email :"))
face_pass = str(input("Please entre your facebook password :"))

client = Client(face_email, face_pass)

if "Pool is loading" in log_in(e_mail,pass_word):
    print("Pool is loading ...")
    client.send(Message(text="Pool is loading ..."), thread_id=client.uid, thread_type=ThreadType.USER)
    while True:
        if "S'inscrire" in log_in(e_mail,pass_word):
            print("I found a pool place.")
            client.send(Message(text="I found a pool place."), thread_id=client.uid, thread_type=ThreadType.USER)
            break
        time.sleep(5)

elif "1337 veut te voir" in log_in(e_mail,pass_word):
    print("Check in is loading ...")
    client.send(Message(text="Check in is loading ..."), thread_id=client.uid, thread_type=ThreadType.USER)
    while True:
        if "S'inscrire" in log_in(e_mail,pass_word):
            print("I found a check in place.")
            client.send(Message(text="I found a check in place."), thread_id=client.uid, thread_type=ThreadType.USER)
            break
        time.sleep(5)

client.logout()
