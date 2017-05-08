from html.parser import HTMLparser
from urllib import parse

class LinkFinder(HTMLparser):
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self,tag,attrs):
		if tag == 'a':
			for (attribute,values) in attrs:
				if attribute == 'href':
					url = parse.urljoin(self.base_url,value)  #urljoin method takes in 2 values and joins the 2 and makes final url.
					self.links.add(url)

	def return_page_links(self):
		return self.links

	def error(self, message):
		pass				