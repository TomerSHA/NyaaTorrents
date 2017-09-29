import urllib2
import urllib

import Config

def get(relativeUrl = ""):
    baseUrl = Config.getUrl()
    return urllib2.urlopen(baseUrl + relativeUrl).read()
