import urllib2
import urllib
from bs4 import BeautifulSoup
import logging
import errno
import os
import sys
import glob
import ctypes

class EmptyException(Exception):
    pass


logging.basicConfig(filename='downloads.log',level=logging.DEBUG)
logging.info("NEW RUN@@@@@")
SITE = 'https://www.nyaa.se/'

UTORRENT_DIR_ = lambda name: "C:\Users" + "\\" + name + "\\AppData\Roaming\uTorrent\uTorrent.exe"
SAVE_DIR = "/"
QUALITY_ = lambda quality: str(quality) + "p"

executeT = lambda ut,a,b,c: ut + " \"" + a + "\" \"" + b + "\" \"" + c + "\""

def download_torrent(name,link,UTORRENT_DIR):
    logging.info("download start " + name)
    logging.info("download link: " + link)
    filename = name + ".torrent"
    try:
        f = urllib2.urlopen('https:' + link)
        data = f.read()
    except Exception as e:
        logging.critical('failed to read file ' + name)
        logging.critical(link)
        exit(-2)
    try:
        with open(filename, "wb") as code:
            code.write(data)
            code.close()
            logging.info("saved")
            command = executeT(UTORRENT_DIR,SAVE_DIR,SAVE_DIR,filename)
            logging.info("comm " + command)
            os.popen(command)
            logging.info("executed")
            os.popen("DEL \"" + filename + "\"")
            logging.info("deleted")
    except Exception as e:
        code.close()
        logging.critical('could not save file ' + name)
        exit(-2)
    logging.info("download ended")



def anime_go(name,page,UTORRENT_DIR):
    logging.info('found page ' + name)
    soup = BeautifulSoup(page).body
    linklist = soup.find_all("tr",{"class":"trusted tlistrow"})

    if len(linklist) < 10:
        raise EmptyException()

    for tr in linklist:
        tname = tr.find("td",{"class":"tlistname"}).a.get_text()
        if "[HorribleSubs]" in tname:
            download_torrent(tname,tr.find("td",{"class":"tlistdownload"}).a.get("href"),UTORRENT_DIR)

def find_anime(name,quality,UTORRENT_DIR):
    values = { 'page':'search', 'cats':'0_0','filter':'0', 'term':'[HorribleSubs] ' + name + ' ' + QUALITY_(quality)}
    data = urllib.urlencode(values)
    logging.info(SITE + '?' + data)
    response = urllib2.urlopen(SITE + '?' + data)
    try:
        anime_go(name,response.read(),UTORRENT_DIR)
    except EmptyException:
        logging.error('Anime not found - ' + name)
        ctypes.windll.user32.MessageBoxA(0, "Anime not found! is the name correct?", "woops", 1)
        exit(1)


def main():
    if len(sys.argv) < 4:
        logging.critical('function call failed ' + sys.argv)
        exit(-1)
    if sys.argv[1] == "clean":
        os.exit()
    UTORRENT_DIR = UTORRENT_DIR_(sys.argv[1])
    anime = sys.argv[3]
    for animem in sys.argv[4:]:
        anime += ' ' + animem
    logging.info('anime arg :' + anime)
    find_anime(anime,sys.argv[2],UTORRENT_DIR)

if __name__ == '__main__':
    main()
