'''
Class which has functions to download with sftp protocal
'''
import pysftp
from helper.labour import *

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None   


class SFTP_DOWNLOAD:
    def __init__(self,url,file_name,config):
        self.url = url
        self.file_name = file_name
        self.cfg = config

    def _download(self):
        #establish sftp connection
        with pysftp.Connection(
            self.cfg.sftp_host_name, 
            username=self.cfg.sftp_user_name,
            password=self.cfg.sftp_password,cnopts=cnopts) as sftp:
            
            #fetch sftp remote path for the file to download
            remote_location=fetch_remote_location(self.url)
            #Fetch local download location
            sftp_download_location = self.cfg.sftp_download_location if not os.environ.get('sftp_download_location') \
                                     else os.environ.get('sftp_download_location')
            #check if the localtion folder exist,if not create
            directory_check(sftp_download_location)
            try:
                sftp.get(remote_location+self.file_name,
                         preserve_mtime=True,
                         localpath=sftp_download_location+self.file_name)
                return True
            except Exception, e:
                #if failed, remove if there is any partial downloaded file
                print 'SFTP download failed {}'.format(str(e))
                removefile(sftp_download_location+self.file_name)
                return False