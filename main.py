import os

#as we crawl through a website a new folder is created every time and the list is generated.
def create_project_folder(directory):
	if not os.path.exists(directory):
		print ('Creating new path '+ directory)
		os.makedirs(directory)

def create_project_file(project_name,base_url):
	queue = project_name + 'queue.txt' 
	crawled = project_name + 'crawled.text'
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,base_url)

def write_file(path,data):
	f = open(path,"w")
	f.write(data)
	f.close()
	

create_project_folder('thenewboston')