#!/bin/sh
files=$(git diff –cached –name-only –diff-filter=ACM | grep ‘.py$’)
if [ -z files ]; then
exit 0
fi
unfmtd=$(pyfmt -l $files)
if [ -z unfmtd ]; then
exit 0
fi
echo “Some .py files are not properly fmt’d”
exit 1
