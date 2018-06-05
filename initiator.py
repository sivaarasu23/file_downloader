##Initiator to get the url and parse it respective downloader
import sys,re
import argparse
from configuration import houston
from downloaders.helper.labour import *

parser = argparse.ArgumentParser(description='Ultimate file downnloader.')
parser.add_argument('-url','--url',help='url to download')

#parsing arguments and loading configurations
args = parser.parse_args()
config = houston.base()

#process url and determince protocal to download and filename
protocal,file_name=process_url(args.url)

if file_name == '':
	raise ValueError('Filename cannot be empty')

"""
Import the Downloader class dynamically based on the prefix.
"""
downloader_name = protocal.upper() + '_' + 'DOWNLOAD'
downloaderClass = getattr(__import__('downloaders', fromlist=[downloader_name]), downloader_name)

downloader = downloaderClass(args.url,file_name,config)
downloader._download()