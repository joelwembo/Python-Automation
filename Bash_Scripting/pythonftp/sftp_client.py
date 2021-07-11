# !/usr/bin/python3
# coding: utf-8
 
from config import sftp_config
 
import paramiko
import os
import platform
import stat
 
 
 # Get connection
def getConnect(host, port, username, password):
    """
    :param host: SFTP ip
    :param port: SFTP port
    :param username: SFTP userName
    :param password: SFTP password
    :return: transport
    """
    print("SFTP connection...")
    result = [1, ""]
 
    try:
        handle = paramiko.Transport((host, port))
        handle.connect(username=username, password=password)
 
        result = [1, "connection success", handle]
    except Exception as e:
        result = [-1, "connection fail, reason:{0}".format(e)]
 
    return result
 
 
 # download file 
def download(handle, remotePath, localAbsDir):
    """
    :param handle:
         :param remotePath: The absolute or relative path of the server file or folder
         :param localAbsDir: The absolute path of the client folder, such as E:/SFTP/downDir/
    :return:
    """
    print("start download file by use SFTP...")
    result = [1, ""]
 
    sftp = paramiko.SFTPClient.from_transport(handle)
    try:
        remotePath = formatPath(remotePath)
        localAbsDir = formatPath(localAbsDir)
 
        remoteRel = ""
        if remotePath == "":
            remotePath = sftp_config.homeDir
        else:
            if remotePath.startswith(sftp_config.homeDir):
                remoteRel = remotePath.replace(sftp_config.homeDir, "/")
                remoteRel = formatPath(remoteRel)
            else:
                remoteRel = remotePath
 
        if localAbsDir == "":
            localAbsDir = sftp_config.localDir
            localAbsDir = formatPath(localAbsDir)
 
        if stat.S_ISREG(sftp.stat(remoteRel).st_mode):  # isFile
            remoteRelPath = remoteRel
            fileName = os.path.basename(remoteRelPath)
            localAbsPath = formatPath(localAbsDir, fileName)
 
            lad = os.path.split(localAbsPath)[0]
            lad = formatPath(lad)
            if not os.path.exists(lad):
                os.makedirs(lad)
 
            sftp.get(remoteRelPath, localAbsPath)
 
            result = [1, "download " + fileName + " success"]
        else:  # isDir
            remoteRelDir = remoteRel
 
            for pd in sftp.listdir(remoteRelDir):  # pd is dir or file 'name
                rp = formatPath(remoteRelDir, pd)
                if isDir(sftp, rp):
                    lad = formatPath(localAbsDir, pd)
                else:
                    lad = localAbsDir
 
                rs = download(handle, rp, lad)
 
                result[1] = result[1] + "\n" + rs[1]
                if rs[0] == -1:
                    result[0] = -1
                else:
                    if result[0] != -1:
                        result[0] = 1
    except Exception as e:
        result = [-1, "download fail, reason:{0}".format(e)]
 
    sftp.close()
    return result
 
    # handle.close()
 
 
 # Upload
def upload(handle, remoteRelDir, localPath):
    """
    :param handle:
         :param remoteRelDir: The relative path of the server folder, which can be None, "", and the file is uploaded to homeDir
         :param localPath: Client file or folder path, when the path starts with localDir, the file is saved to the relative path of homeDir
    :return:
    """
    print("start upload file by use SFTP...")
    result = [1, ""]
 
    sftp = paramiko.SFTPClient.from_transport(handle)
    try:
        remoteRelDir = formatPath(remoteRelDir)
        localPath = formatPath(localPath)
 
        localRelDir = ""
        if localPath == "":
            localPath = sftp_config.localDir
            localPath = formatPath(localPath)
        else:
                         if localPath.startswith(sftp_config.localDir): # absolute path
                localRelDir = localPath.replace(sftp_config.localDir, "/")
                localRelDir = formatPath(localRelDir)
                         else: # Relative (localDir) path
                localPath = formatPath(sftp_config.localDir, localPath)
 
        if remoteRelDir == "":
            remoteRelDir = formatPath("/uploadFiles/", localRelDir)
        else:
            if remoteRelDir.startswith(sftp_config.homeDir):
                remoteRelDir = remoteRelDir.replace(sftp_config.homeDir, "/")
                remoteRelDir = formatPath(remoteRelDir)
 
        if os.path.isdir(localPath):  # isDir
            rs = uploadDir(sftp, remoteRelDir, localPath)
        else:  # isFile
            rs = uploadFile(sftp, remoteRelDir, localPath)
 
        if rs[0] == -1:
            result[0] = -1
        result[1] = result[1] + "\n" + rs[1]
 
    except Exception as e:
        result = [-1, "upload fail, reason:{0}".format(e)]
 
    sftp.close()
    return result
 
    # handle.close()
 
 
 # Upload all under the specified folder
def uploadDir(sftp, remoteRelDir, localAbsDir):
    """
    :param sftp:
         :param remoteRelDir: The relative path of the server folder, which can be None, "", and the file is uploaded to homeDir at this time
         :param localAbsDir: client folder path, when the path starts with localDir, the file is saved to the relative path of homeDir
    :return:
    """
    print("start upload dir by use SFTP...")
    result = [1, ""]
 
    try:
        for root, dirs, files in os.walk(localAbsDir):
            if len(files) > 0:
                for fileName in files:
                    localAbsPath = formatPath(localAbsDir, fileName)
                    rs = uploadFile(sftp, remoteRelDir, localAbsPath)
                    if rs[0] == -1:
                        result[0] = -1
                    result[1] = result[1] + "\n" + rs[1]
 
            if len(dirs) > 0:
                for dirName in dirs:
                    rrd = formatPath(remoteRelDir, dirName)
                    lad = formatPath(localAbsDir, dirName)
                    rs = uploadDir(sftp, rrd, lad)
                    if rs[0] == -1:
                        result[0] = -1
                    result[1] = result[1] + "\n" + rs[1]
 
            break
    except Exception as e:
        result = [-1, "upload fail, reason:{0}".format(e)]
 
    return result
 
 
 # Upload the specified file
def uploadFile(sftp, remoteRelDir, localAbsPath):
    """
    :param sftp:
         :param remoteRelDir: The relative path of the server folder, which can be None, "", and the file is uploaded to homeDir at this time
         :param localAbsPath: client file path, when the path starts with localDir, the file is saved to the relative path of homeDir
    :return:
    """
    print("start upload file by use SFTP...")
    result = [1, ""]
 
    try:
        try:
            sftp.chdir(remoteRelDir)
        except:
            try:
                sftp.mkdir(remoteRelDir)
            except:
                print("U have no authority to make dir")
 
        fileName = os.path.basename(localAbsPath)
        remoteRelPath = formatPath(remoteRelDir, fileName)
 
        sftp.put(localAbsPath, remoteRelPath)
 
        result = [1, "upload " + fileName + " success"]
    except Exception as e:
        result = [-1, "upload fail, reason:{0}".format(e)]
 
    return result
 
 
 # Determine remote path isDir or isFile
def isDir(sftp, path):
    try:
        sftp.chdir(path)
        return True
    except:
        return False
 
 
# return last dir'name in the path, like os.path.basename
def lastDir(path):
    path = formatPath(path)
    paths = path.split("/")
    if len(paths) >= 2:
        return paths[-2]
    else:
        return ""
 
 
 # Format path or splicing path and format
def formatPath(path, *paths):
    """
         :param path: path 1
         :param paths: path 2-n
    :return:
    """
    if path is None or path == "." or path == "/" or path == "//":
        path = ""
 
    if len(paths) > 0:
        for pi in paths:
            if pi == "" or pi == ".":
                continue
            path = path + "/" + pi
 
    if path == "":
        return path
 
    while path.find("\\") >= 0:
        path = path.replace("\\", "/")
    while path.find("//") >= 0:
        path = path.replace("//", "/")
 
         if path.find(":/")> 0: # With disk character NOT EQ ZERO, os.path.isabs NOT WORK
        if path.startswith("/"):
            path = path[1:]
    else:
        if not path.startswith("/"):
            path = "/" + path
 
    if os.path.isdir(path):  # remote path is not work
        if not path.endswith("/"):
            path = path + "/"
    elif os.path.isfile(path):  # remote path is not work
        if path.endswith("/"):
            path = path[:-1]
    elif path.find(".") < 0:  # maybe it is a dir
        if not path.endswith("/"):
            path = path + "/"
    else:  # maybe it is a file
        if path.endswith("/"):
            path = path[:-1]
 
    # print("new path is " + path)
    return path
