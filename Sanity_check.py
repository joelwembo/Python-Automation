#!/bin/sh

# steps to be undertaken to configure git repository so that it runs the code sanity checking tooks before any commits
# prevent it from happening again if the sanity testing fails

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
