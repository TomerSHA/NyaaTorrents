import urllib2
import urllib
from bs4 import BeautifulSoup
import logging
import errno
import os
import sys


logging.basicConfig(filename='downloads.log',level=logging.DEBUG)
logging.info("NEW RUN@@@@@")
SITE = 'https://www.nyaa.se/'

def download_torrent(name,link):
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
            os.popen(filename)
            logging.info("executed")
            os.popen("DEL \"" + filename + "\"")
            logging.info("deleted")
    except Exception as e:
        code.close()
        logging.critical('could not save file ' + name)
        exit(-2)
    logging.info("download ended")



def anime_go(name,page):
    logging.info('found page ' + name)
    soup = BeautifulSoup(page).body
    linklist = soup.find_all("tr",{"class":"trusted tlistrow"})

    for tr in linklist:
        tname = tr.find("td",{"class":"tlistname"}).a.get_text()
        if "[HorribleSubs]" in tname:
            download_torrent(tname,tr.find("td",{"class":"tlistdownload"}).a.get("href"))

def find_anime(name):
    values = { 'page':'search', 'cats':'0_0','filter':'0', 'term':'[HorribleSubs] ' + name + ' 720'}
    data = urllib.urlencode(values)
    logging.info(SITE + '?' + data)
    response = urllib2.urlopen(SITE + '?' + data)
    anime_go(name,response.read())

def main():
    if len(sys.argv) < 2:
        logging.critical('no download page links found')
        exit(-1)
    anime = sys.argv[1]
    for animem in sys.argv[2:]:
        anime += ' ' + animem
    logging.info('anime arg :' + anime)
    find_anime(anime)

if __name__ == '__main__':
    main()
