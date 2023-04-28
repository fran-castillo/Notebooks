import requests
from bs4 import BeautifulSoup as bs

insta_user = input('ingrese usuario: ')
url = 'https://instagram.com/'+ insta_user
r =  requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt' : 'Foto del perfil de ' + insta_user})['src']
print(profile_image)