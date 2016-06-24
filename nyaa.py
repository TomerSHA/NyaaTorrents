import urllib2
from bs4 import BeautifulSoup
import logging
import errno
import os
import sys


logging.basicConfig(filename='downloads.log',level=logging.DEBUG)
logging.info("NEW RUN@@@@@")
SITE = 'https://www.nyaa.se/'

def download_torrent(name,link):
    logging.info("download start " + tname)
    f = urllib2.urlopen(link)
    data = f.read()
    with os.open(tname + ".torrent", "wb") as code:
        code.write(data)
    code.close()
    logging.info("download ended")



def anime_go(download_page):
    page = urllib2.urlopen(download_page)
    soup = BeautifulSoup(page).body
    linklist = soup.find("tr",{"class":"trusted tlistrow"})

    for tr in linklist:
        print tr.prettify()
        '''tname = tr.find("td",{"class":"tlistname"}).a.get_text()
        if "[HorribleSubs]" in tname:
            download_torrent(tname,tr.find("td",{"class":"tlistdownload"}).a.get("href"))
            logging.info(tname + "file found")'''

def find_anime(name):
    

def main():
    if len(sys.argv)<2
        logging.critical('no download page links found')
        exit(-1)
    for anime in sys.argv[1:]:
        find_anime(anime)

if __name__ == '__main__':
    main()
