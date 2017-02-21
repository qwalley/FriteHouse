# author: Will Alley
# date: February 20, 2017

import requests
from BeautifulSoup import BeautifulSoup

def replaceWords (sample):
	newSample = sample.text.replace(' good ', ' bad ')
	newSample = newSample.replace('&nbsp;', ' ')
	newSample = newSample.replace(' love ', ' hate ')
	newSample = newSample.replace('incredible', 'impossibly stupid')
	newSample = newSample.replace('tremendous', 'terrible')
	newSample = newSample.replace('wonderful', 'deplorable')
	newSample = newSample.replace('spectacular', 'deplorable')
	newSample = newSample.replace('amazing', 'aweful')
	newSample = newSample.replace('fantastic', 'miserable')
	newSample = newSample.replace(' won ', ' lost ')
	newSample = newSample.replace(' win ', ' lose ')
	newSample = newSample.replace(' well ', ' poorly ')
	newSample = newSample.replace(' more ', ' less ')
	newSample = newSample.replace(' happy ', ' sad ')
	newSample = newSample.replace(' first ', ' last ')
	newSample = newSample.replace(' new ', ' old ')
	newSample = newSample.replace(' open ', ' close ')
	newSample = newSample.replace(' create ', ' destroy ')
	newSample = newSample.replace('beautiful', 'ugly')
	newSample = newSample.replace('Applause', 'Boo-ing')
	newSample = newSample.replace('applause', 'boo-ing')
	newSample = newSample.replace('Laughter', 'Cries of dismay')
	newSample = newSample.replace('laughter', 'cries of dismay')
	newSample = newSample.replace('Governor', 'Demon-Overseer')
	newSample = newSample.replace('governor', 'Demon-Overseer')
	newSample = newSample.replace('Senator', 'Elf-Lord')
	newSample = newSample.replace('senator', 'Elf-Lord')

	return newSample

url = "https://www.whitehouse.gov/the-press-office/2017/02/17/remarks-president-trump-unveiling-boeing-787-dreamliner-aircraft"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
article = soup.find('div', attrs={'class': 'field-item even'})

for paragragh in article.findAll('p'):
	newPar = replaceWords(paragragh)
	print '<p>' + newPar + '</p>' + '<br>'