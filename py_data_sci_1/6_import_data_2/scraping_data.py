#use beautifulsoup to parse and extract structered data from HTML

from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup/'

r = requests.get(url)

html_doc = r.text

#create beautiful soup object and prettify it
soup = BeautifulSoup(html_doc, 'lxml')
pretty_soup = soup.prettify()
print(pretty_soup)

#get title
bs_title = soup.title
print(bs_title)

#get text
bs_text = soup.get_text()
print(bs_text)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))
