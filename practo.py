from bs4 import BeautifulSoup
import requests
area = (str(input())).capitalize()
category = (str(input())).capitalize()
source = requests.get(f'https://www.practo.com/search/doctors?results_type=doctor&q=%5B%7B%22word%22%3A%22{category}%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city={area}').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div', class_='u-border-general--bottom'):

    name = article.find('div', class_='u-color--primary uv2-spacer--xs-bottom').h2.text
    print(name)
    specialist = article.find('div', class_='u-d-flex').text
    print(specialist)
    experience = article.find('div', class_="uv2-spacer--xs-top").text
    print(experience)
    fees = article.find('div', class_="uv2-spacer--xs-top").text
    print(fees)
    location = article.find('div', class_="u-bold u-d-inlineblock u-valign--middle").text
    print(location)
  
   