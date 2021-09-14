from bs4 import BeautifulSoup 
import urllib.request

def get_stock_html(ticker_name):
    opener = urllib.request.build_opener(
            urllib.request.HTTPRedirectHandler(), 
            urllib.request.HTTPHandler(debuglevel = 0),
        )
    opener.addheaders = [
        ('User-agent',
        "Mozilla/4.0 (compatible; MSIE 7.0; "
        "Windows NT 5.1; .NET CLR 2.0.50727; "
        ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]

    url = "http://finance.yahoo.com/q?s=" + ticker_name 
    response = opener.open(url) 
    return response.read()
    #return ''.join(response.readlines())

def find_quote_section(html):
    soup = BeautifulSoup(html, features="html.parser")
    quote = soup.find('div', 
                attrs = {'id': 'quote-summary'})
    return quote 

def parse_stock_html(quote):
    result = {}
    tick = ticker_name.lower()


if __name__ == '__main__': 
    html = get_stock_html('GOOG')
    quote = find_quote_section(html)
    print(quote)

