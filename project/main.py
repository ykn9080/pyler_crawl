import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

response = requests.get(
    "http://pyler-front-assignment.surge.sh/index.html")
soup = BeautifulSoup(response.text, 'html.parser')
fetch1 = soup.select('.super-title a')
fetch2 = soup.select_one('.view-count')
fetch3 = soup.find("h1", {"class": "ytd-video-primary-info-renderer"})
fetch4 = soup.find("div", {"id": "description"})

# fetch1
hash_tags = []
for fch in fetch1:
    arr1 = list(fch.text.strip())
    hash_tags.append("".join(arr1[1:]))

# fetch2
title = int(fetch2.text.split()[0].replace(",", ""))

# fetch3
P = pq(str(fetch3))
views = pq(str(P.find("yt-formatted-string"))).text

# fetch4
R = pq(str(fetch4))
S = pq(str(R.find(".style-scope.yt-formatted-string")))
content = S('span').text()

print({"hash_tags": hash_tags,
       "title": title,
       "views": views,
       "content": content
       })
