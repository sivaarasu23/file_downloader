'''
Integration test for all _download function in each protocal class
'''
from configuration import houston
import unittest
from downloaders.http_protocal import HTTP_DOWNLOAD
from downloaders.sftp_protocal import SFTP_DOWNLOAD
from downloaders.ftp_protocal import FTP_DOWNLOAD
import os
from downloaders.helper.labour import *


class IntegrationTestCase(unittest.TestCase):
    """Tests for all downloaders."""
    http_url='http://www.bit-com.info/kawa24/wp-content/uploads/2016/04/agoda.png'
    sftp_url='sftp://google_mc@47.88.158.69/product_feeds/google_mc/sg/apple_day/googlemc_sg_apple_day_marketing_feed.tsv'
    ftp_url='ftp://127.0.0.1:1026/home/sivaa/daus_sg.csv'

    def test_http_downloaders(self):

        protocal,file_name=process_url(self.http_url)
        config = houston.base()
        
        downloader_name = protocal.upper() + '_' + 'DOWNLOAD'
        downloaderClass = getattr(__import__('downloaders', fromlist=[downloader_name]), downloader_name)
        downloader = downloaderClass(self.http_url,file_name,config)

        ## check dynamically imported class is correct
        self.assertIsInstance(downloader,HTTP_DOWNLOAD)

        #proceed with the download using the validated instance
        #assertTrue to make sure download is successfull
        self.assertTrue(downloader._download())
    def test_sftp_downloaders(self):

        protocal,file_name=process_url(self.sftp_url)
        config = houston.base()
        
        downloader_name = protocal.upper() + '_' + 'DOWNLOAD'
        downloaderClass = getattr(__import__('downloaders', fromlist=[downloader_name]), downloader_name)
        downloader = downloaderClass(self.sftp_url,file_name,config)

        ## check dynamically imported class is correct
        self.assertIsInstance(downloader,SFTP_DOWNLOAD)

        #proceed with the download using the validated instance
        #assertTrue to make sure download is successfull
        self.assertTrue(downloader._download())
    def test_ftp_downloaders(self):

        protocal,file_name=process_url(self.sftp_url)
        config = houston.base()
        
        downloader_name = protocal.upper() + '_' + 'DOWNLOAD'
        downloaderClass = getattr(__import__('downloaders', fromlist=[downloader_name]), downloader_name)
        downloader = downloaderClass(self.sftp_url,file_name,config)

        ## check dynamically imported class is correct
        self.assertIsInstance(downloader,SFTP_DOWNLOAD)

        #proceed with the download using the validated instance
        #assertTrue to make sure download is successfull
        self.assertTrue(downloader._download())


if __name__ == '__main__':
    unittest.main()