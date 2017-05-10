import threading
from queue import Queue
from spider import Spider
from domain import *
from main import *

PROJECT_NAME = "thenewboston"
HOMEPAGE = "https://thenewboston.com/"
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_THREADS = 8
queue = Queue()  #theading queue this enables to make a queue where jobs can be put into queue.
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links)>0:
		print("Queue currently has "+ str(len(queued_links)))
		create_jobs()

def create_jobs():
	for links in file_to_set(QUEUE_FILE):
		queue.put(links)
	queue.join() #ensures healthy and collision free multi-threading.
	crawl()

def create_spider():
	for i in range NUMBER_OF_THREADS:
		t = theading.Thread(target = work)
		t.daemon = True #once the MutliThread main program dies then our main thread will be killed.
		t.start() #built in func to start a thread.

def work():
	while True:
		url = queue.get() #multithreaded queue is obtained and returns all the threads from there
		Spider.crawl_page(theading.current_thread().name,url)
		queue.task_done() #once done it returns False and while loop ends.

create_jobs()
crawl()