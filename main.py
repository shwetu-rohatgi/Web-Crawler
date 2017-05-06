import os

#as we crawl through a website a new folder is created every time and the list is generated.
def create_project_folder(directory):
	if not os.path.exists(directory):
		print ('Creating new path '+ directory)
		 
