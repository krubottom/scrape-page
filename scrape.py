from lxml import html
import requests

page = requests.get('http://bruhchristmas.duckdns.org/states')
tree = html.fromstring(page.content)

print page
