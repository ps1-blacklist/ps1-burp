import os
import time

R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
B = "\033[34m"
M = "\033[35m"
C = "\033[36m"
W = "\033[37m"
reset = "\033[0m"

def ban():
    os.system('clear')
    banner = rf"""{G}
               ___      __                   
    ____  ____<  /     / /_  __  ___________ 
   / __ \/ ___/ /_____/ __ \/ / / / ___/ __ \
  / /_/ (__  ) /_____/ /_/ / /_/ / /  / /_/ /
 / .___/____/_/     /_.___/\__,_/_/  / .___/ 
/_/                                 /_/          v1.0
    
    {C}ps1-burp | Automated Burp Suite Installer on Termux X-11
                By @ps1-blacklist{reset}
    """
    print(banner)

ban()
time.sleep(3)

print(f"{Y}installing...{reset}")
time.sleep(1)

DBUS_PATH = '/data/data/com.termux/files/home/.dbus'
BURP_DIR = '/data/data/com.termux/files/home/.tools-image/burp'
BURP_JAR = f"{BURP_DIR}/burpsuite.jar"
DESKTOP_FILE = '/data/data/com.termux/files/home/Desktop/burp.desktop'

print(f'{C}⚡ Updating...{reset}')
os.system('apt update -y')

print(f'{C}⚡ Upgrading...{reset}')
os.system('apt upgrade -y')




print(f'{C}⚡ Installing Python...{reset}')
os.system('pkg install python -y')
os.system(f'rm -f "{BURP_JAR}"')

if not os.path.exists(DBUS_PATH):
    print(f"{R}First install Termux X-11 : https://github.com/ps1-blacklist/ps1-x11.git{reset}")
    exit()

os.makedirs(BURP_DIR, exist_ok=True)

if not os.path.exists(BURP_JAR):
    print(f"{C}⚡ Installing Wget...{reset}")
    os.system("pkg install wget -y")

    print(f"{C}⚡ Downloading Burp Suite...{reset}")
    os.system(f'wget "https://portswigger.net/burp/releases/download?product=community&type=Jar" -O "{BURP_JAR}"')

    os.system(f'cp -r "kindpng_2064380.png" "{BURP_DIR}"')

    print(f"{G}✔ Burp Suite Downloaded Successfully!{reset}")
else:
    print(f"{Y}✔ Burp Suite Already Installed!{reset}")

print(f"{C}⚡ Installing Java...{reset}")
os.system("pkg install openjdk-21 -y")

if not os.path.exists(DESKTOP_FILE):
    print(f"{C}⚡ Creating Desktop Shortcut...{reset}")
    with open(DESKTOP_FILE, "w") as f:
        f.write(f"""[Desktop Entry]
Name=Burp Suite
Exec=java -jar {BURP_JAR}
Icon={BURP_DIR}/kindpng_2064380.png
Type=Application
Terminal=false
""")
else:
    os.system(f'cp "{DESKTOP_FILE}" "{BURP_DIR}/"')

ban()

des = rf"""{G}
Go To Desktop → Double Click To Run Burp Suite
https://github.com/ps1-blacklist

{Y}⚡ Follow Me On Github...{reset}
"""
print(des)