import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

respone = requests.get(url)

status = respone.status_code
print(status)
content = respone.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title)
print(soup.title.get_text())
