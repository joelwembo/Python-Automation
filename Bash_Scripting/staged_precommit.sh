#!/bin/bash

# Pre commit
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep ".py\{0,1\}$")
if [[ "$STAGED_FILES" = "" ]]; then
  exit 0
fi

# Flake8 and autopep8
PASS=true
printf "\nValidating Finesse Engine Python Files:\n"
for FILE in $STAGED_FILES
do
  autopep8 --in-place --aggressive --aggressive "$FILE"
  flake8 --ignore F,W "$FILE"
  if [[ "$?" == 0 ]]; then
    printf "\n\033[32mFlake8 Passed: $FILE\033[0m"
    git add "$FILE"
  else
    printf "\n\033[41mFlake8 Failed: $FILE\033[0m"
    PASS=false
  fi
done

# Printing messages
printf "\nPython validation completed!\n"
if ! $PASS; then
  printf "\033[41mCOMMIT FAILED: LINTING FAILED:\033[0m Your commit contains files that should pass Flake8 but do notn.\n"
  exit 1
else
  printf "\033[42mLINTING SUCCEEDED\033[0m\n"
fi

# Django tests module
printf "\n You are Executing Django Tests"
python ./manage.py test
if [[ "$?" == 0 ]]; then
  printf "\033[42mTest Passes\033[0m\n"
else
  printf "\033[41mCOMMIT REJECTED:\033[0m Found Failed Test Cases. Please fix them before commiting\n"
  exit 1
fi
printf "\n Python Tests completed"
exit $?
