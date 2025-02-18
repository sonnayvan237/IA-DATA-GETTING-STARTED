import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

# je viens d'importer les bbibliotheque qui vont me servir
url = 'https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal'
response = requests.get(url)
# l'adresse vers laquelle je sollocite faire une extractions de données
print(response.text)


contenupage = BeautifulSoup(response.text, 'html.parser')
contenupage.prettify()
print(contenupage.text)

premierH1 = contenupage.find_all('img')[1]

print(premierH1)


