from ftplib import FTP

ftp = FTP('')
ftp.connect('ftp.drivehq.com')
ftp.login("Vishnusai1234098", "Vishnusai123!")
ftp.cwd('//') #replace with your directory
ftp.retrlines('LIST')
print(ftp.pwd())


def uploadFile(filename, path):
 ftp.storbinary('STOR '+filename, open(path, 'rb'))
 
def downloadFile(filename):
 localfile = open("C:/Users/dell/Desktop/input/downdes.txt", 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
 ftp.quit()
 localfile.close()

def close():
 ftp.quit()
