#!/bin/bash
#SFTP configuration information
#username
USER=root
#password
PASSWORD=5EYS40T04BMF
# Root directory of files to be uploaded
SRCDIR=/u02/dab/sftpFiles
#FTP directory
DESDIR=/u01/sftpFiles
#IP
IP=192.168.10.11
#port
PORT=22022

Get File #
cd ${SRCDIR} ;
All files in the directory #
#FILES=`ls` 
# Xml file modification time prior to the execution time of five minutes
FILES=`find ${SRCDIR} -mmin -50 -name '*.xml'`

for FILE in ${FILES}
do
    echo ${FILE}
# Send file (key part)
lftp -u ${USER},${PASSWORD} sftp://${IP}:${PORT} <<EOF
cd ${DESDIR}/
lcd ${SRCDIR}
put ${FILE}
by
EOF
