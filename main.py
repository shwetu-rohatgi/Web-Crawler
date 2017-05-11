import os

#as we crawl through a website a new folder is created every time and the list is generated.
def create_project_folder(directory):
	if not os.path.exists(directory):
		print ('Creating new path '+ directory)
		os.makedirs(directory)

def create_project_file(project_name,base_url):
	queue = project_name + '/queue.txt' 
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue,base_url)
	if not os.path.isfile(crawled):
		write_file(crawled,'')

def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

def append_to_file(path,data): #appends new links at the end of the file.
	with open(path, 'a') as file:
		file.write(data + '\n')

def clear_file(path):
	with open(path, 'w'):
		pass #deletes previous and creates a new file with no data that is the function of the pass.

def file_to_set(file_name):
	results = set()
	with open(file_name,'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
	return results

def set_to_file(links,file_name):
	clear_file(file_name)
	for link in links:
		append_to_file(file_name,link)

