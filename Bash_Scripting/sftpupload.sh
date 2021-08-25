sftp -v -oIdentityFile=path user@server <<EOF
put localPath ftpPath
EOF

local_path=/path/to/local/file
remote_path=/path/to/local/file
remote_path=/somewhere/or/other
sftp -v -oIdentityFile=path user@server <<EOF
put $local_path $remote_path
EOF
