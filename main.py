import requests , re , threading , random , os , colorama, sys,time
import colored 
import webbrowser
bannar_color =[
colored.fg("magenta") + colored.attr("bold"), 
colored.fg("orchid")  + colored.attr("bold"),
colored.fg("cyan")    + colored.attr("bold"),
colored.fg("yellow")  + colored.attr("bold"),
colored.fg("#bc000b") + colored.attr("bold"),
colored.fg("white")   + colored.attr("bold"),
colored.fg("green")   + colored.attr("bold"),
colored.fg("#aa557f") + colored.attr("bold"),
colored.fg("#33ff29") + colored.attr("bold"),
colored.fg("plum_3")  + colored.attr("bold"),
colored.fg("#ff1d00") + colored.attr("bold"),
colored.fg("#ab01ff") + colored.attr("bold"),
colored.fg("#c81d59") + colored.attr("bold"),
colored.fg("blue")    + colored.attr("bold"),
colored.fg("#c81d59") + colored.bg("cyan")+colored.attr("bold"),]
W = bannar_color[3] #yellow
Y = bannar_color[0] #magenta
B = bannar_color[2] #cyan
G = bannar_color[6] #green
R = bannar_color[4] #red
M = bannar_color[7] ##aa557f
X = bannar_color[8] ##33ff29
Z = bannar_color[9] ##ff1d00
Q = bannar_color[10]##ab01ff
GG = bannar_color[11]##c81d59
WI = bannar_color[5]#white
BOOLD = bannar_color[12]
bl = bannar_color[-2]
F = bannar_color[-1]




os.system("cls && mode con:cols=75 lines=40 && title Spotify Validator By Mf4Tn ")
colorama.init(autoreset=True)
red = colorama.Fore.LIGHTRED_EX
green = colorama.Fore.LIGHTGREEN_EX
reset = colorama.Fore.RESET
greend = colorama.Fore.GREEN
clear = "\x1b[0m"
colors = [36, 32, 34, 35, 31, 37]
x= """
███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗                
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝                
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝                 
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝                  
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║                   
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝                   
                                                                      
██╗   ██╗ █████╗ ██╗     ██╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██║   ██║██╔══██╗██║     ██║██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██║   ██║███████║██║     ██║██║  ██║███████║   ██║   ██║   ██║██████╔╝
╚██╗ ██╔╝██╔══██║██║     ██║██║  ██║██╔══██║   ██║   ██║   ██║██╔══██╗
 ╚████╔╝ ██║  ██║███████╗██║██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                    
"""
for N, line in enumerate( x.split( "\n" ) ):
    sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
    time.sleep( 0.05 )



print(f"{greend}Spotify Validator By {red}Mf4Tn - @United_Of_Spammers{reset}\n\n\n")
#os.system("start ")
webbrowser.open_new_tab('https://mf4team.net')  


valid = 0
invalid = 0
retries = 0
checked = 0
title = f"title Total Checked {checked} - Valids {valid} - Invalids {invalid} - Retries {retries}"
def check_folder(folder):
    if(not os.path.exists(folder)):
        os.mkdir(folder)
def check(user):
    global proxies_file,valid,invalid,retries,checked,title
    if(":" in user):
        user = user.split(':')[0]
    while True:
        random_proxy = random.choice(proxies_file)
        proxy = {
            "http":"http://"+random_proxy,
            "https":"http://"+random_proxy
        }
        try:
            headers = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'origin': 'https://www.spotify.com',
                'referer': 'https://www.spotify.com/',
                'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
            }
            r = requests.get("https://spclient.wg.spotify.com/signup/public/v1/account?validate=1&email="+user,headers=headers,proxies=proxy,timeout=5).text
            
            if("That email is already registered to an account" in r):
                valid +=1
                checked+=1
                os.system(f"title Total Checked {checked} - Valids {valid} - Invalids {invalid} - Retries {retries}")
                print(f"{green}[Valid]{reset} "+user)
                check_folder("Results")
                with open("Results/live.txt","a")as mfa:mfa.write(user+"\n")
                return True
            else:
                checked +=1
                invalid +=1
                os.system(f"title Total Checked {checked} - Valids {valid} - Invalids {invalid} - Retries {retries}")
                print(f"{red}[Invalid]{reset} "+user)
                return False 
        except:
            os.system(f"title Total Checked {checked} - Valids {valid} - Invalids {invalid} - Retries {retries}")
            retries +=1


threads = []
combo = input(f'{GG}[>] {Y}Enter List:{WI} ')
prox = input(f'{GG}[>] {Q}Enter Proxy File (HTTP):{WI} ')
proxies_file = open(prox,"r").read().splitlines()
emails_file = open(combo,"r").read().splitlines()
threads_number = int(input(f"{green}[>] Threads Number: {reset}"))
os.system("cls && mode con:cols=68 lines=40")
for line in range(len(emails_file)):

    if(len(emails_file)-line < threads_number):
        threading.Thread(target=check,args=(emails_file[line],)).start()
    else:
        for i in range(threads_number):
            thread = threading.Thread(target=check,args=(emails_file[line+i],))
            threads.append(thread)
            thread.start()
        for th in range(round(len(threads) * (70/100))):
            threads[th].join()