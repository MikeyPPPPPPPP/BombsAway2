from bs4 import BeautifulSoup
import requests
import time
from pytube import YouTube
import os

#'https://www.youtube.com/channel/UCFv1Up3DCWl5LcSDPNwCB6A'

class print_stuff:
    def __init__(self):
        self.url = ''
        self.usetor = False
        self.setchannel = 'set https://www.youtube.com/channel/UCFv1Up3DCWl5LcSDPNwCB6A\n\n'
        self.use = 'use (tor, Tor)\n\n\n'
        self.tor = 'is tor open and running?\n\n\n'

        
    def banner(self):
        print("""
    TOR Powered
      ____                  _                                        _______
     |  _ \                | |             /\                       /  __   \
     | |_) | ___  _ __ ___ | |__  ___     /  \__      ____ _ _   _ |__/  |   |
     |  _ < / _ \| '_ ` _ \| '_ \/ __|   / /\ \ \ /\ / / _` | | | |     /   /
     | |_) | (_) | | | | | | |_) \__ \  / ____ \ V  V / (_| | |_| |    /   /.
     |____/ \___/|_| |_| |_|_.__/|___/ /_/    \_\_/\_/ \__,_|\__, |   /______|
                                                              __/ |
                                                             |___/
                                                             by mikeyP                                               
        """)
        
    def usage(self):
        print("""
    Usage:
        set channel   -set the youtube channel
        tor           -to use tor
        help <x>      -for help with the commands
        go            -starts the program
        quit          -to quit
        """)


    def hhelp(self):
        print('''
    commands
    --------
    set
    tor     (not on by default)
    help <x>
    go 
    quit
        ''')

class connecting:
    def __init__(self,url):
        self.checks = 0
        self.pr = print_stuff()
        self.user_in = []
        self.fi = open('urls.txt','+r') 
        self.channel = url
        self.torr = False
        self.url = self.channel+'/videos'
        self.links2proc = [] #allsites.txt
        self.format_urls = [] #format_urls - allurls.txt
        self.sites = []
        self.session = requests.session()
        self.session.proxies = {}
        self.r = requests.get(str(self.url))
        self.data = self.r.text
        self.soup = BeautifulSoup(self.data, 'lxml')

    def __str__(self):
        al = [self.checks,self.pr,self.user_in,self.channel,self.torr \
              ,self.url,self.links2proc,self.format_urls,self.sites]
        for x in al:
            print(str(x),'\n')
        
    def connect2tor(self): #connects to tor
        print('\t\tRestart with Tor open and connected to the internet')
        
        self.session.proxies['http'] = 'socks5h://127.0.0.1:9150'
        self.session.proxies['https'] = 'socks5h://127.0.0.1:9150'
        torr = True

        
    def get_links2proc(self):
        for link in self.soup.find_all('a'):
            self.soup.find(id='thumbnail')
            self.sites.append(link.get('href'))
            if link.get('href').startswith('/watch') == True:
                self.links2proc.append(str(link.get('href')))
            else:
                pass


    def format_url(self):
        for x in self.links2proc:
            a = 'https://www.youtube.com'+x
            self.format_urls.append(str(a))


    def res(self):
        self.user_in = []

    def get_in(self):
        self.pr.banner()
        self.pr.usage()
        word = input('[0]:')
        for x in word.split():
            if x == 'set' or x == 'tor':
                self.checks += 1
            
            self.user_in.append(x)
        

    def process_ins(self):   
        if self.user_in[0] == 'help' and self.user_in[1] == 'set':
            print(self.pr.setchannel)
            time.sleep(2)
            
        elif self.user_in[0] == 'help' and self.user_in[1] == 'use':
            print(self.pr.use)
            time.sleep(2)
            
        elif self.user_in[0] == 'help' and self.user_in[1] == 'tor':
            print(self.pr.tor)
            time.sleep(2)

        elif self.user_in[0] == 'help' and self.user_in[1] == 'all': 
            print(self.pr.hhelp())
            time.sleep(4)

                
        elif self.user_in[0] == 'set':
            self.channel = self.user_in[1]
            self.checks += 1
        elif self.user_in[0] == 'tor' or self.user_in[0] == 'Tor' or self.user_in[0] == 'TOR':
            self.connect2tor()
            self.checks += 1
        elif self.user_in[0] == 'go' and self.torr == False:
            if self.checks >= 1:
                
                for x in self.format_urls:
                    
                    self.fi.write(x)
                    self.fi.write('\n')
                self.fi.close()
                '''
                for x in self.format_urls:
                    w = requests.get(x)#self.r = requests.get(x)#session.get(url[x])
                    print('ststus code: ', w)
                    
                    
                    time.sleep(3)
                '''
            else:
                print('Tor might be on')
            print('\t\tDone __________________________________________!')
            print('exiting now')
            time.sleep(2)
            #exit()
        elif self.user_in[0] == 'go' and self.torr == True:
            if self.checks >= 2:
                for x in self.format_urls:
                    w = self.session.get(x)#self.r = session.get(x)
                    print('ststus code: ', w)
                    time.sleep(3)
            else:
                print(self.pr.tor)
            print('\t\tDone __________________________________________!')
            print('exiting now')
            time.sleep(2)
            #exit()
        elif self.user_in[0] == 'quit':
            print('exiting now')
            time.sleep(2)
            #exit()
        else:
            print('NOT A COMMAND')
        #self.res()
        
        

    

def menu():
    #pr = print_stuff()
    user = input('channel_url:')#'https://www.youtube.com/channel/UCFv1Up3DCWl5LcSDPNwCB6A'
    conn = connecting(user)
    conn.get_links2proc()
    conn.format_url()
    conn.get_in()
    #conn.get_in()
    #str(conn)
    #conn.process_ins()
    conn.res()
    #for x in range(1,10):
    conn.get_in()
    conn.process_ins()
    conn.res()
        
        #conn.format_urls = conn.format_urls.rstrip()
    conn.format_urls = list(dict.fromkeys(conn.format_urls))
        
    for x in conn.format_urls:
        try:
            yt = YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            yt.download('./videos')
        except:
            print('Format Error while downloading')

    print('\t\tDone!\t\t')
    print('Makeing music file')
    os.mkdir('videos/music')
    arr = os.listdir('videos/.')
    files = []
    for x in range(0,len(arr)-1):
        name = arr[x].split('.')[0]
        os.system('ffmpeg -i '+'"videos/'+arr[x]+'" -acodec libmp3lame -b:a 192k -vn '+'"videos/music/'+name+str(x)+'.mp3"')
            #os.system('ffmpeg -i '+x+' -acodec copy '+name+'.mp3')
    
    print('Finished!') 
        
        
        

        
    

menu()
