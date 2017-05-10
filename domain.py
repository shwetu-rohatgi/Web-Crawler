from urllib.parse import urlparse

# this function returns (name.example.com) type of string
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

# this function returns (example.com) type of string
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		print results[-2] + '.' + results[-1]
		y = raw_input("Enter to exit")
	except:
		return ''
