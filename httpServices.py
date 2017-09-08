import urllib2
import urllib

import utils

def get(relativeUrl = ""):
    baseUrl = utils.ConfigGet("Network")['url']
    return urllib2.urlopen(baseUrl + relativeUrl).read()
