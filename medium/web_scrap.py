from bs4 import BeautifulSoup
import requests


URL = 'https://pylint.readthedocs.io/en/latest/tutorial.html'
response = requests.get(URL, timeout= 10)
print(response)
soup = BeautifulSoup(response.content,'html.parser')
titles = soup.find_all('h2')
for title in titles:
    print(title.text)
