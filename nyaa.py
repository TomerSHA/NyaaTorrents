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
    logging.info("download start " + tname)
    f = urllib2.urlopen(link)
    data = f.read()
    with os.open(tname + ".torrent", "wb") as code:
        code.write(data)
    code.close()
    logging.info("download ended")



def anime_go(name,page):
    logging.info('found page ' + name)
    soup = BeautifulSoup(page).body
    linklist = soup.find("tr",{"class":"trusted tlistrow"})

    for tr in linklist:
        print tr.prettify()
        '''tname = tr.find("td",{"class":"tlistname"}).a.get_text()
        if "[HorribleSubs]" in tname:
            download_torrent(tname,tr.find("td",{"class":"tlistdownload"}).a.get("href"))
            logging.info(tname + "file found")'''

def find_anime(name):
    values = { 'page':'search', 'cats':'0_0','filter':'0', 'term':'[HorribleSubs] ' + name + ' 720'}
    data = urllib.urlencode(values)
    print data
    req = req = urllib2.Request(SITE, data)
    response = urllib2.urlopen(req)
    anime_go(name,response.read())

def main():
    if len(sys.argv) < 2:
        logging.critical('no download page links found')
        exit(-1)
    for anime in sys.argv[1:]:
        find_anime(anime)

if __name__ == '__main__':
    main()
