import sys,os,requests,re
from bs4 import BeautifulSoup 
from logging import warning

# os.system("python app.py 6005&")
def illgetagoodlookingnamesoon(debut : str,fin :str) :
    retour = [debut]
    for i in range(ord(debut.capitalize())+1,ord(fin.capitalize())+1):
        retour.append(chr(i))
    return retour

#Port & intervale de lettres
port =  sys.argv[2]
inter = sys.argv[1].split('-',1)
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
data_cleaned=[]
for url in pages:
    with requests.get(url) as p:
        p.encoding='utf-8'
        soup = BeautifulSoup(p.text,'html.parser')
        soup = soup.find('ul',class_='substances list_index has_children')
        data = soup.findAll('li')
        data_cleaned.extend([i.text.strip() for i in data])
if __name__ == "__main__":
    print("yalkiwi")
    with open('subst.dic','w',encoding='utf-16-le') as f:
            for i in data_cleaned :
                f.write(i+','+'.N+subst\n')
    with open('info.txt','w') as file :
        lettersDico = {}
        k=0
        for i in data_cleaned:
            lettersDico.setdefault(i[0],[])
            lettersDico[i[0]].append(i)
        for i in lettersDico:
            k+=len(lettersDico[i])
            file.write('{}:{}\n'.format(i.upper(),len(lettersDico[i])))
        file.write("Total:{}".format(len(data_cleaned)))
        print(k)
    print(len(data_cleaned))
    a={'z':'b'}
    
