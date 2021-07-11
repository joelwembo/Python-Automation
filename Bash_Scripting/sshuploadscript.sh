cd
cat >.netrc<<EOF
machine 127.0.0.1
login user
password password
EOF
chmod 600 .netrc
