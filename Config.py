import ConfigParser

def ConfigGet(section):
    Config = ConfigParser.ConfigParser()
    Config.read("config.ini")
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def getDefaultQuality():
    return ConfigGet("Attributes")['quality']

def getDefaultSubGroup():
    return ConfigGet("Attributes")['subs']
def getUrl():
    return ConfigGet("Network")['url']
def getSearchPrefix():
    return ConfigGet("Network")['searchPrefix']
