import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time, os, sys, logging, math
from platform import system
import re
def clear():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
clear()
import traceback
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33', '\033', '\33', '\33', '\033', '\033', '\033'

sys.stdout.write(RED +'''

[*] Search In Google OR Bing With Dork
[*] Usage : Enter Link WebSite(You Can Delet The Section!) And WordSearch(Like : php?id=
[*] By KH PROG
''' + END)
site = (input(" Enter Link WebSite : "))
wordsearch = (input(" Enter Word Search : "))

url = 'http://www.google.com/search?q=site:'+site+'+inurl:'+wordsearch+'&sa'
print('[*]Scaning... ','\n'," ", url)
openurl = urllib.request.urlopen(url)
read = openurl.read()
soup = BeautifulSoup(read, 'html.parser')
print('[*]Result : ')
for i in soup.findAll("h3", {"class":"r"}):
        print(re.search('url\?q=(.+?)\&sa', i.a['href']).group(1))
