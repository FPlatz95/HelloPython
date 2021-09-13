from bs4 import BeautifulSoup 
import urllib2 

def get_stock(ticker_name):
    opener = urllib2.build_opener(
            urllib2.HTTPRedirectHandler(), 
            urllib2.HTTPHandler(debuglevel = 0),
        )
    opener.addheaders = [
        ('User-agent',
        "")
    ]
