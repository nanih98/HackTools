# #pip3 install lxml
# #pip3 install beautifulsoup4
# from io import BytesIO
# from lxml import etree
# import requests
#
# url = 'https://nostarch.com'
# r = requests.get(url)
# content = r.content
#
# parser = etree.HTMLParser()
# content = etree.parse(BytesIO(content), parser=parser)
# for link in content.findall('//a'):
#     print(f"{link.get('href')} -> {link.text}")


from bs4 import BeautifulSoup as bs
import requests
url = 'http://bing.com'
r = requests.get(url)

tree = bs(r.text, 'html.parser') # Parse into tree
for link in tree.find_all('a'): # find all "a" anchor elements.
    print(f"{link.get('href')} -> {link.text}")