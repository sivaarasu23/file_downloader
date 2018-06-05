import unittest
from downloaders.helper.labour import *
import shutil, tempfile
import os

class LabourTestCase(unittest.TestCase):
    """Tests for `labour.py`."""
    test_urls_1=[
        ('http://www.bit-com.info/kawa24/wp-content/uploads/2016/04/agoda.png','http','agoda.png'),
        ('sftp://test@sftserver/home/joe/employee.csv','sftp','employee.csv'),
        ('ftp://test@ftpserver/home/joe/employee.csv','ftp','employee.csv'),
        ('sftp://test@sftserver/','sftp','')]

    test_urls_2=[
        ('http://www.bit-com.info/kawa24/wp-content/uploads/2016/04','http','agoda.png'),
        ('sftp://test@sftserver/home/joe/employe.csv','sftp','employee.csv'),
        ('fftp://test@ftpserver/home/joe/employee.csv','ftp','employee.csv')]

    test_urls_3='sftp://test@sftserver/'

    test_urls_4='sftp://test@sftserver/home/joe/employe.csv'

    path = '/tmp/test/'

    def test_process_url(self):
        """see if the function sends protocal and filename"""
        
        for url,protocal,filename in self.test_urls_1:
          self.assertEqual(process_url(url),(protocal,filename))

        for url,protocal,filename in self.test_urls_2:
          self.assertNotEqual(process_url(url),(protocal,filename))

    def test_directory_check(self):
        """ see if function creates directory"""
        os.rmdir(self.path)
        self.assertTrue(directory_check(self.path))

    def test_fetch_remote_location(self):
      """see if the function sends remote_location"""
      
      self.assertEqual(fetch_remote_location(self.test_urls_4),'/home/joe/')

      self.assertIsNone(fetch_remote_location(self.test_urls_3))


if __name__ == '__main__':
    unittest.main()