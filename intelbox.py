import colors as c
import os
import termcolor
import time
import sys


def default_tools():
    print(termcolor.colored('\n[+] Installing dmitry exiftool fierce mat2', 'green', attrs=['bold']))
    os.system('sudo apt install dmitry exiftool fierce mat2 -y')
    aws_inventory_tool()

def aws_inventory_tool():
    print(termcolor.colored("\n[+] Installing AWS Inventory",'green', attrs=['bold']))
    os.system('git clone https://github.com/janiko71/aws-inventory.git')
    os.chdir('aws-inventory')
    os.system('sudo pip3 install -r requirements.txt')
    os.chdir('../')
    badkarma()

def badkarma():
    print(termcolor.colored('\n[+] Installing BadKarma','green', attrs=['bold']))
    os.system('git clone https://github.com/r3vn/badKarma.git')
    os.chdir('badKarma')
    os.system('sudo pip3 install -r requirements.txt')
    os.chdir('../')
    basedomainname()

def basedomainname():
    print(termcolor.colored('\n[+] Installing basedomainname','green', attrs=['bold']))
    os.mkdir("basedomainname")
    os.chdir("basedomainname")
    os.system("sudo apt install ruby")
    os.system("wget http://morningstarsecurity.com/downloads/basedomainname-0.1.tar.gz")
    os.system("tar -xvzf basedomainname-0.1.tar.gz")
    os.chdir('../')
    bfac()

def bfac():
    print(termcolor.colored('\n[+] Installing Bfac','green', attrs=['bold']))
    os.system('git clone https://github.com/mazen160/bfac.git')
    os.chdir('bfac')
    os.system('sudo python3 setup.py install')
    os.chdir('../')
    bing_ip2hosts()

def bing_ip2hosts():
    print(termcolor.colored('\n[+] Installing bing_ip2hosts','green', attrs=['bold']))
    os.system('git clone https://github.com/urbanadventurer/bing-ip2hosts.git')
    os.chdir('bing-ip2hosts')
    os.system("sudo cp ./bing-ip2hosts /usr/bin/ && chmod +x bing-ip2hosts")
    os.chdir('../')
    catnthecanary()

def catnthecanary():
    print(termcolor.colored('\n[+] Installing catnthecanary','green', attrs=['bold']))
    os.system('git clone https://github.com/packetassailant/catnthecanary.git')
    os.chdir('catnthecanary')
    os.system('pip3 install -U -r environment.txt')
    os.chdir('../')
    recon_ng()

def recon_ng():
    print(termcolor.colored('\n[+] Installing Recon NG','green', attrs=['bold']))
    os.system('git clone https://github.com/lanmaster53/recon-ng.git')
    os.chdir('recon-ng')
    os.system('pip3 install -r REQUIREMENTS')
    os.chdir('../')
    finalrecon()

def finalrecon():
    print(termcolor.colored('\n[+] Installing FinalRecon','green', attrs=['bold']))
    os.system('git clone https://github.com/thewhiteh4t/FinalRecon.git')
    os.chdir('FinalRecon')
    os.system('pip3 install -r requirements.txt')
    os.chdir('../')
    osintgram()

def osintgram():
    print(termcolor.colored('\n[+] Installing Osintgram','green', attrs=['bold']))
    os.system('git clone https://github.com/Datalux/Osintgram.git')
    os.chdir('Osintgram')
    os.system('sudo apt install libncurses5-dev -y && pip install gnureadline==6.3.3') 
    os.system('pip3 install -r requirements.txt')
    os.chdir('../')
    theharvester()

def theharvester():
    print(termcolor.colored('\n[+] Installing theharvester','green', attrs=['bold']))
    os.system('git clone https://github.com/laramies/theHarvester.git')
    os.chdir('theHarvester')
    os.system('sudo python3 -m pip install -r requirements/base.txt')
    os.chdir('../')
    spiderfoot()

def spiderfoot():
    print(termcolor.colored('\n[+] Installing spiderfoot','green', attrs=['bold']))
    os.system('wget https://github.com/smicallef/spiderfoot/archive/v4.0.tar.gz')
    os.system('tar zxvf v4.0.tar.gz && sudo rm v4.0.tar.gz')
    os.chdir('spiderfoot-4.0')
    os.system('pip3 install -r requirements.txt')
    os.chdir('../')
    twint()

def twint():
    print(termcolor.colored('\n[+] Installing twint','green', attrs=['bold']))
    os.system('git clone --depth=1 https://github.com/twintproject/twint.git')
    os.chdir('twint')
    os.system('sudo pip install aiohttp==3.7.0 && pip3 install . -r requirements.txt') 
    os.system('pip3 install twint')
    os.system('../')
    phoneinfoga()

def phoneinfoga():
    print(termcolor.colored('\n[+] Installing Phoneinfoga','green', attrs=['bold']))
    os.mkdir('phoneinfoga')
    os.chdir('phoneinfoga')
    os.system('curl -sSL https://raw.githubusercontent.com/sundowndev/phoneinfoga/master/support/scripts/install | bash')
    os.system('sudo mv ./phoneinfoga /usr/bin/phoneinfoga')
    os.chdir('../')
    google_earth_pro()

def google_earth_pro():
    print(termcolor.colored('\n[+] Installing Google Earth Pro','green', attrs=['bold']))
    os.mkdir('google_earth_pro')
    os.chdir('google_earth_pro')
    os.system('wget -O google-earth64.deb http://dl.google.com/dl/earth/client/current/google-earth-stable_current_amd64.deb')
    os.system('sudo dpkg -i google-earth64.deb && apt-get -f install')
    os.chdir('../')
    eyewitness()


def eyewitness():
    print(termcolor.colored('\n[+] Installing EyeWitness','green', attrs=['bold']))
    os.system('git clone https://github.com/FortyNorthSecurity/EyeWitness.git')
    print(termcolor.colored('[+] Installed EyeWitness'))
    maltego()

def maltego():
    print(termcolor.colored('\n[+] Installing Maltego','green',attrs=['bold']))
    os.mkdir('maltego')
    os.chdir('maltego')
    os.system('wget https://maltego-downloads.s3.us-east-2.amazonaws.com/linux/Maltego.v4.3.1.deb')
    os.system('sudo dpkg --install Maltego.v4.3.1.deb')
    os.chdir('../')
    metagoofil()

def metagoofil():
    print(termcolor.colored('\n[+] Installing Metagoofil ','green', attrs=['bold']))
    os.system('git clone https://github.com/opsdisk/metagoofil.git')
    os.chdir('metagoofil')
    os.system('pip3 install -r requirements.txt')
    os.chdir('../')
    osrframework()

def osrframework():
    print(termcolor.colored('\n[+] Installing osrframework','green', attrs=['bold']))
    os.system('sudo apt install python-setuptools -y')
    os.system('sudo pip3 install osrframework')
    photon()

def photon():
    print(termcolor.colored('\n[+] Installing Photon', 'green', attrs=['bold']))
    os.system('git clone https://github.com/s0md3v/Photon.git')
    os.chdir('Photon')
    os.system('sudo pip3 install -r requirements.txt')
    print(termcolor.colored('[+] Installed Photon','green', attrs=['bold']))
    sublist3r()

def sublist3r():
    print(termcolor.colored('\n[+] Installing Sublist3r','green', attrs=['bold']))
    os.system('git clone https://github.com/aboul3la/Sublist3r.git')
    os.chdir('Sublist3r')
    os.system('sudo pip3 install -r requirements.txt')
    os.chdir('../')
    print(termcolor.colored('[+] Installed Sublist3r','green', attrs=['bold']))
    sherlock()

def sherlock():
    print(termcolor.colored('\n[+] Installing Sherlock','green', attrs=['bold']))
    os.system('git clone https://github.com/sherlock-project/sherlock.git')
    os.chdir('sherlock')
    os.system('sudo python3 -m pip install -r requirements.txt')
    os.chdir('../')
    print(termcolor.colored('[+] Installed Sherlock ', 'green', attrs=['bold']))
    ccrawldns()

def ccrawldns():
    print(termcolor.colored('\n[+] Installing CCrawlDNS','green', attrs=['bold']))
    os.system('git clone https://github.com/lgandx/CCrawlDNS.git')
    os.chdir('CCrawlDNS')
    os.system('sudo pip3 install requests')
    os.chdir('../')
    print(termcolor.colored('[+] Installed CCrawlDNS','green',attrs=['bold']))
    certgraph()

def certgraph():
    print(termcolor.colored('\n[+] Installing Certgraph','green', attrs=['bold']))
    os.mkdir('Certgraph')
    os.chdir('Certgraph')
    os.system('sudo apt install golang')
    os.system('wget https://github.com/lanrat/certgraph/releases/download/20220513/certgraph-linux-386-20220513.zip')
    os.system('unzip certgraph-linux-386-20220513.zip')
    os.chdir('../')
    print(termcolor.colored('[+] Installed Certgraph','green',attrs=['bold']))
    cloud_buster()

def cloud_buster():
    print(termcolor.colored('\n[+] Installing Cloud Buster', 'green', attrs=['bold']))
    os.system('sudo pip3 install dnspython3 bs4 && git clone https://github.com/SageHack/cloud-buster.git')
    print(termcolor.colored('[+] Installed Cloud Buster','green',attrs=['bold']))
    cloudfail()

def cloudfail():
    print(termcolor.colored('\n[+] Installing Cloudfail','green', attrs=['bold']))
    os.system('git clone https://github.com/m0rtem/CloudFail.git')
    os.chdir('Cloudfail')
    os.system('sudo pip3 install -r requirements.txt')
    os.chdir('../')
    print(termcolor.colored('[+] Installed Cloudfail', 'green', attrs=['bold']))
    cloudmare()
    
def cloudmare():
    print(termcolor.colored('\n[+] Installing Cloudmare','green', attrs=['bold']))
    os.system('git clone https://github.com/mrh0wl/Cloudmare.git')
    print(termcolor.colored('[+] Installed Cloudmare', 'green', attrs=['bold']))
    sys.exit(0)

# Make the Directory in /opt/ folder 
def mkdir():
    
    if os.path.exists('/opt/osint-tools'):
        print("\n\n[" + termcolor.colored("!",'red',attrs=['bold']) + "] Directory Already Exists\n")
        print("[" + termcolor.colored("!",'green',attrs=['bold']) + "] Delete The Existing Directory and then run the script\n")
        sys.exit(0)

    else:
        print(termcolor.colored('==> Installing the tools', 'green', attrs=['bold']))
        os.chdir("/opt/")
        os.system('mkdir osint-tools')
        os.chdir('osint-tools')
        default_tools()


def print_banner():
    banner = """
╦╔╗╔╔╦╗╔═╗╦  ╔╗ ╔═╗═╗ ╦ 
║║║║ ║ ║╣ ║  ╠╩╗║ ║╔╩╦╝
╩╝╚╝ ╩ ╚═╝╩═╝╚═╝╚═╝╩ ╚═
                By @malwaredojo
"""
    
    banner_tab = banner.splitlines()
    code = 33
    keep = True
    
    for b in banner_tab:
        clr = "\u001b[38;5;" + str(code) + "m "
        print(c.colors.bold + clr + b + c.colors.reset)
        if keep:
            code += 36
            keep = False
        else:
            keep = True
    

if __name__ == '__main__':
    if os.geteuid()==0:
        try:
            print_banner()
            print(termcolor.colored('\n[+] All tools are installed in /opt/osint-tools directory ', 'yellow', 'on_grey', attrs=['bold']))
            mkdir()
        except KeyboardInterrupt:
            print("[" + termcolor.colored("!",'red',attrs=['bold']) + "] Keyboard Interrupt detected.....Exiting")

    else:
        print_banner()
        print("\n[" + termcolor.colored("!",'red',attrs=['bold']) + "] Run as " + termcolor.colored("ROOT",'red',attrs=['bold']) + " user\n")
        time.sleep(1)
        sys.exit(0)
