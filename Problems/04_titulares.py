#First:
#pip install GoogleNews
from GoogleNews import GoogleNews

'''
Language: lang as English
Period: period as number, N, representing news from last N days
'''
#Crea las busqueda de noticias
googlenews_1d = GoogleNews(lang='es', period='1d') #'en' for englis
#Busca el termino
googlenews_1d.search('Colombian News')
#Returns JSON objets representing differen news
results_1 = googlenews_1d.results(sort=True)
#Clear googlenews to do a fresh search next time
googlenews_1d.clear()


'''
Print the title, description and URL of the news
'''
for i in results_1:
  print('\n\nTITLE:', i['title'], '\nDESC:', i['desc'], '\nURL: ', i['link'])


#BeautifulSoup  or Urlib.request can also be use
