import requests
import sys
from bs4 import BeautifulSoup 
import re
from logging import warning

def illgetagoodlookingnamesoon(debut : str,fin :str) :
    retour = [debut]
    for i in range(ord(debut.capitalize())+1,ord(fin.capitalize())+1):
        retour.append(chr(i))
    return retour

if __name__ == "__main__":
    #Port & intervale de lettres
    port =  sys.argv[1]
    inter = sys.argv[2].split('-',1)
    #source /le lien de debut etc etc
    src = 'http://localhost:{}'.format(port) 
    #warning au cas ou les parametres mechi cheban
    if len(inter[0]) > 1 or len(inter[1]) > 1 :
        warning("bounds can only be one character long !")
        exit()
    if inter[0].capitalize() > inter[1].capitalize() :
        warning("bounds error!")
        exit()
    letters = illgetagoodlookingnamesoon(inter[0],inter[1])
    pages = ['{}/vidal/vidal-Sommaires-Substances-{}.htm'.format(src,i) for i in letters]
    
    for url in pages:
        print(url)
        p = requests.get(url,{'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(p.text,'html.parser')
        soup = soup.find('ul',class_='substances list_index has_children')
        data = soup.findAll('li')
        data_cleaned = [i.text.strip() for i in data]
        print(*data_cleaned,sep='\n')
        