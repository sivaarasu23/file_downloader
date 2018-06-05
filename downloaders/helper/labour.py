'''
Contains helper function
'''
import re
import os
import errno

def process_url(url):
    """
    Using regex, split protocal at the beginning of the 
    url and file name at the end

    Parameters
    ----------
    url : str
        Url which should be processed

    """
    pattern = '(.*)(://)(.*)/(.*$)'
    try:
        resp = re.match(pattern,url)
    except Exception, e:
        print 'Url is invalid - {}'.format(str(e))

    return resp.group(1),resp.group(4)
    

def directory_check(path):
    """
    check if the folder path exist,if not create

    Parameters
    ----------
    Path : str
        Folder path that needs to be checked

    """
    try:
        if not os.path.exists(path):
            print 'creating directory..'
            os.makedirs((path))
            return True
    except Exception, e:
        print 'Cannot create directory - {}'.format(str(e))
        return False


def fetch_remote_location(url):
    """
    Using regex, finds the file path excluding the filename

    Parameters
    ----------
    url : str
        Url from which remote_location has to taken

    """
    pattern = '(.*)(://)([0-9a-zA-Z].+?)(/.*/)(.*$)'
    try:
        resp = re.match(pattern,url)
        return resp.group(4)
    except Exception, e:
        print 'Couldnt find the remote location - {}'.format(str(e))
        return None

def removefile(file_path):
    """
    removes a file and all the intermediate directories that might be
    missing.

    Parameters
    ----------
    file_path : str
        File path to be removed.

    """
    # import ipdb;ipdb.set_trace()
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except OSError as error:
        if error.errno != errno.EEXIST or os.path.exists(file_path):
            raise

