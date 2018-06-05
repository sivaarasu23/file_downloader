'''
Class which has functions to download with http protocal
'''
import urllib2,requests
from helper.labour import *


class HTTP_DOWNLOAD:
	def __init__(self,url,file_name,config):
		self.url = url
		self.file_name = file_name
		self.cfg = config

	def _download(self):
		filedata = requests.get(self.url)  
		#Fetch local download location
		http_download_location=self.cfg.http_download_location if not os.environ.get('http_download_location') \
								 else os.environ.get('http_download_location')
		#check if the localtion folder exist,if not create
		directory_check(http_download_location)

		download_file = http_download_location+self.file_name
		
		try:
			with open(download_file, 'wb') as f:  
			    f.write(filedata.content)
			return True
		except Exception, e:
			print 'HTTPS download failed {}'.format(str(e))
			removefile(download_file)
			return False