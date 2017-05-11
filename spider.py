from urllib.request import urlopen
from start import LinkFinder
from domain import *
from main import *

class Spider:
	# Class variables (These variables are shared amonst all the instances)
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_files = ''
	crawled_files = ''
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name   # we use Spider.variable_name scheme as it is a static variable and it must use class name just like java does.
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_files = Spider.project_name + "/queue.txt"
		Spider.crawled_files = Spider.project_name + "/crawled.txt"
		self.boot()   # first methid that runs when a page is to be crawled for the first time
		self.crawl_page("First Spider",Spider.base_url)

	# Creates directory and files for project on first run and starts the spider
	@staticmethod  #a static method specifier as a static method uses on instance variables and doesn't use self argument.
	def boot():
		create_project_folder(Spider.project_name)
		create_project_file(Spider.project_name,Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_files)  # creates a queue set from a file
		Spider.crawled = file_to_set(Spider.crawled_files)  # creates a crawled set from a file

	# Updates user display, fills queue and updates files
	@staticmethod
	def crawl_page(spider_name, page_url):
		if page_url not in Spider.crawled:
			print(spider_name+ " now crawling "+ page_url)
			print("Queue "+ str(len(queue))+ " | Crawled "+ str(len(crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))  #first we gather all the single page urls from page_url into a handle and name it gather_links and then we add these urls into queue using the function add_links_to_queue.
			Spider.queue.remove(page_url)   #removes already crawled urls from queue set.
			Spider.crawled.add(page_url)	#adds the removed urls to crawled set.
			Spider.make_changes_to_files()    #changes made into set must be made permanently into files.

	# Converts raw response data into readable information and checks for proper html formatting
	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			response = urlopen(page_url)     #returns 0's and 1's string as response.
			if 'text/html' in response.getheader('Content-Type'):
				html_bytes = response.read()  #reads 0's and 1's and stores them into variable
				html_string = html_bytes.decode("utf-8")   #variable is converted into html format
			finder = LinkFinder(Spider.base_url, page_url) 
			finder.feed(html_string)
		except Exception as e:
			print(str(e))
			return set()
		return finder.page_links()  #returns page address after successful running of try block


	# Saves queue data to project files
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			if Spider.domain_name != get_domain_name(url):
				continue
			Spider.queue.add(url)

	@staticmethod
	def make_changes_to_files():
		set_to_file(Spider.queue, Spider.queue_files)
		set_to_file(Spider.crawled, Spider.crawled_files)


