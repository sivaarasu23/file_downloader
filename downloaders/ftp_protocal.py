'''
Class which has functions to download with sftp protocal
'''
from ftplib import FTP
import re
from helper.labour import *


class FTP_DOWNLOAD:
    def __init__(self,url,file_name,config):
        self.url = url
        self.file_name = file_name
        self.cfg = config

    def _get_client(self):
        ftp = FTP()
        ftp.connect(self.cfg.ftp_host_name,1026)
        ftp.login(user=self.cfg.ftp_user_name, passwd=self.cfg.ftp_password)
        return ftp

    def _download(self):
        #get ftp client
        ftp = self._get_client()

        #Fetch local download location
        ftp_download_location=self.cfg.ftp_download_location if not os.environ.get('ftp_download_location') \
                             else os.environ.get('ftp_download_location')
                             
        #check if the localtion folder exist,if not create
        directory_check(ftp_download_location)
        download_file = ftp_download_location+self.file_name

        #fetch ftp remote path for the file to download
        remote_location=fetch_remote_location(self.url)
        # ftp.cwd(remote_location)
        try:
            with open(download_file, 'wb') as f:  
                ftp.retrbinary('RETR ' + self.file_name, f.write, 1024)
            return True
        except Exception, e:
            print 'FTP download failed {}'.format(str(e))
            removefile(download_file)
            return False