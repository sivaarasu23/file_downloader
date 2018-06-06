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

    def _get_client(self):
        '''
        Creates connection object for sftp 
        '''
        try:
            key = self.cfg.sftp_private_key
        except Exception, e:
            key=None

        try:
            if key is not None:
                sftp=pysftp.Connection(
                            self.cfg.sftp_host_name, 
                            username=self.cfg.sftp_user_name,
                            private_key=self.cfg.sftp_private_key)
                return sftp
            else:
                sftp=pysftp.Connection(
                        self.cfg.sftp_host_name, 
                        username=self.cfg.sftp_user_name,
                        password=self.cfg.sftp_password )
                return sftp
        except Exception, e:
            raise ValueError('Connection to sftp server failed {}'.format(str(e)))

    def _download(self):

        #establish sftp client
        sftp = self._get_client()
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