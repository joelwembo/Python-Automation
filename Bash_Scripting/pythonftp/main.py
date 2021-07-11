# !/usr/bin/python3
# coding: utf-8
 
from config import sftp_config
from clients import sftp_client
 
 
def runSFTP(remotePath, localPath):
    result = sftp_client.getConnect(
        host=sftp_config.host,
        port=sftp_config.port,
        username=sftp_config.username,
        password=sftp_config.password
    )
 
    if result[0] != 1:
        print(result[1])
        sys.exit();
    else:
        print("connection success")
 
    handle = result[2]
 
    result = sftp_client.upload(
        handle=handle,
        remoteRelDir=remotePath,
        localPath=localPath
    )
 
    # result = sftp_client.download(
    #     handle=handle,
    #     remotePath=remotePath,
    #     localAbsDir=localPath
    # )
 
    handle.close()
 
         print("All success" if result[0] == 1 else "Partial failure")
    print(result[1])
    sys.exit()
    
    def main():
    remotePath = input("Enter the relative path of the server file or folder:")
         localPath = input("Enter the absolute path of the client folder:")
    runSFTP(remotePath, localPath)
    
    # Console:

#Enter the relative path of the server file or folder: upDir
#Enter the absolute path of the client folder: E:/SFTP/dir1
#SFTP connection...
#connection success
#start upload file by use SFTP...
#start upload dir by use SFTP...
#start upload file by use SFTP...
#start upload file by use SFTP...
#start upload file by use SFTP...
#start upload dir by use SFTP...
#start upload file by use SFTP...
#start upload file by use SFTP...
#start upload file by use SFTP...
#all successful

#upload dir1_file1.txt success
#upload dir1_file2.txt success
#upload dir1_file3.txt success

#upload dir2_file1.txt success
#upload dir2_file2.txt success
#upload dir2_file3.txt success


 
 
