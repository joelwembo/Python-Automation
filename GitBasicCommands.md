How to re-initialize the repo
--------------------------------------
git reset --soft HEAD^

git add -A .

git commit -m "rewriting history"

git push --force origin master

------------------------Adding a file to a repository using the command line-------------

On your computer, move the file you'd like to upload to GitHub into the local directory that was created when you cloned the repository.
Open Git Bash.
Change the current working directory to your local repository.
Stage the file for commit to your local repository.
$ git add .
# Adds the file to your local repository and stages it for commit. To unstage y
