import ConfigParser, os
import errno
config = ConfigParser.ConfigParser()

def makedirs(dir_path):
    """
    Creates a directory and all the intermediate directories that might be
    missing. However this method is different from using `os.makedirs`
    directly in that this one does not raise an exception if the directory
    already exists.

    Parameters
    ----------
    dir_path : str
        Directory path to be created.

    """
    try:
        os.makedirs(dir_path)
    except OSError as error:
        if error.errno != errno.EEXIST or not os.path.isdir(dir_path):
            raise

def getmypath(init=__file__):
    """
    path to caller file
    """
    p = os.path.realpath(init)
    a, b = os.path.split(p)
    return a

AGODA_HOME = os.environ.get('AGODA_HOME') if os.environ.get('AGODA_HOME') else getmypath(__file__)
AGODA_HOME='/data/working_dir/user/siva/agoda/'
CREDENTIALS_FOLDER = os.environ.get('credential_path') if os.environ.get('credential_path') else AGODA_HOME + '.test_credentials'
# makedirs(CREDENTIALS_FOLDER)

# Credentials basic load from enviroment variables or from cfg file
AGODA_CONFIG_FILE = os.path.join(CREDENTIALS_FOLDER, 'houston.cfg')

if len(config.read(AGODA_CONFIG_FILE)) == 0:
	raise Exception('No config file found!')

class base():
	def __init__(self):
		pass

SECTIONS=['ftp', 'sftp','credentials','download_location']

for section in SECTIONS:
	for c,v in config.items(section):
		setattr(base, c, v)

