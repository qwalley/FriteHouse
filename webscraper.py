# author: Will Alley
# date: February 20, 2017

import requests
from BeautifulSoup import BeautifulSoup

def getArticles (mainURL):
	response = requests.get(mainURL)
	html = response.content
	soup = BeautifulSoup(html)
	links = []
	for item in soup.findAll('div', attrs={'class': 'views-field views-field-title'}):
		tag = item.find('a')
		links.append("https://www.whitehouse.gov" + tag['href'])
	return links

def processArticle (url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html)
	article = soup.find('div', attrs={'class': 'field-item even'})

	for paragragh in article.findAll('p'):
		newPar = replaceWords(paragragh)
		print '<p>' + newPar + '</p>' + '<br>'

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
	newSample = newSample.replace('the media', 'the Rebel Alliance')
	newSample = newSample.replace('President', 'Supreme Leader')

	return newSample

mainURL = "https://www.whitehouse.gov/briefing-room/speeches-and-remarks"
articleLinks = getArticles (mainURL)
for url in articleLinks:
	print url



