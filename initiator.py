##Initiator to get the url and parse it respective downloader
import sys,re
import argparse
from configuration import houston
from downloaders.helper.labour import *
from multiprocessing import Pool, cpu_count
from functools import partial
import pandas as pd

parser = argparse.ArgumentParser(description='Ultimate file downnloader.')
parser.add_argument('-url','--url',help='url to download')
parser.add_argument('-file','--file',help='text file with urls to download')
parser.add_argument('-chunk_size','--chunk_size',help='text file with urls to download',default=10)

####parsing arguments and loading configurations
args = parser.parse_args()
config = houston.base()

def imake_chunks(ll, chunk_size=10):
    for x in xrange(0, len(ll), chunk_size):
        yield ll[x:x + chunk_size]

def main(url):

	#process url and determince protocal to download and filename
	protocal,file_name=process_url(url)

	if file_name == '':
		raise ValueError('Filename cannot be empty')

	"""
	Import the Downloader class dynamically based on the prefix.
	"""
	downloader_name = protocal.upper() + '_' + 'DOWNLOAD'
	downloaderClass = getattr(__import__('downloaders', fromlist=[downloader_name]), downloader_name)

	downloader = downloaderClass(url,file_name,config)
	downloader._download()

if __name__ == '__main__':
	if args.url:
		main(args.url)
	elif args.file:
		df = pd.read_csv(args.file,header=None)
		df.columns=['urls']
		for chunks in imake_chunks(df,chunk_size=int(args.chunk_size)):
		    pool = Pool(cpu_count())
		    pool.map(main, [items['urls'] for _,items in chunks.iterrows()])
		    pool.close()
		    pool.join()
	else:
		print '''
				Either pass single url under -url argument
				or pass all the urls in a text file under -file argument
			  '''




