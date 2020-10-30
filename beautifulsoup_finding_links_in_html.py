import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
rounds = 1

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Laughlan.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
print(tags[17])

while rounds < 8:
   # print(rounds, tags[17])
    newlink = tags[17]
    finallink = newlink.get('href')
    url = str(finallink)
    print(rounds, url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    rounds = rounds + 1
   # print(rounds, tags[17])
