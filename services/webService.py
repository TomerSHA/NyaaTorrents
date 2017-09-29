from bs4 import BeautifulSoup
import httpServices
import Config

def searchAnime(animeName, quality, subGroup):
    return httpServices.get(createSearchRequest(animeName, quality, subGroup))

def createSearchRequest(animeName,quality, subGroup):
    parsedArgsList = map(lambda str1: str1.replace(' ', '+'), [animeName, quality, subGroup])
    searchSuffix = reduce((lambda str1, str2: '{}+{}'.format(str1, str2)), parsedArgsList)
    return ''.join([Config.getUrl(), Config.getSearchPrefix(), searchSuffix])
