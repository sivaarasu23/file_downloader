# file_downloader
Determines the protocal from url and downloads file

# Protocals supported are:
 * Http
 * sftp
 * ftp

# Setup:
  * As the first step create ".credentials" folder inside configuration folder and create a file with name "houston.cfg"
  * Below shows the example of how it should look like, it should have credentials for sftp and ftp server you are trying download
  * You can also add download locations for each protocal or you can set environment variables in the same name.Makse sure its the same name as provided in the example image
  ![](screenshots/config_example.png| width=100)

# How to run:

To start the downloader, run `python initiator.py --url=' '

# To add additional protocal:
* Add credentials if there is any to configuration file
* Add a file with respective protocal class and follow the namming convention for the function names
