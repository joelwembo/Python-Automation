Use SFTP to build a file upload and download server

Create a user for SFTP login

useradd sftpuser1
Set a password for this user:

passwd sftpuser1
Set sshd_config:

vi /etc/ssh/sshd_config
Find the Subsystem sftp line and change it to:

Subsystem sftp internal-sftp
UsePAM yes
Match user sftpuser1
ForceCommand internal-sftp
ChrootDirectory /home/ftpdir
Replace the above /home/ftpdir directory with the actual directory you need to qualify.

Note that the user owner of this directory must be root, and the owner of each level of the directory above the directory must also be root.

If the parent directory cannot be set to root, it can be implemented in disguise by establishing the symbolic link ln -s.

Repeat these three lines for multiple users:

Match user sftpuser2
ForceCommand internal-sftp
ChrootDirectory /home/ftpdir
This allows you to set different restricted directories for different users.

Restart sshd:

service sshd restart
Now use SFTP software to log in with sftpuser1 user and you will find that the directory has been restricted to /home/ftpdir.

Note: The directory permissions of /home/ftpdir should be controlled. After the default directory is created, the permissions are 700. If you want to read it, you need to change it to 750. Do not write it as 770. The ssh group permissions for /home/ftpdir do not want to have w permission. If you want to upload files to the directory, you can create a new folder with w permissions under /home/ftpdir.
