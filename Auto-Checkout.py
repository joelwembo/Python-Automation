from git import Repo

repo = Repo('/path/to/a/local/repo')

# List all branches
for branch in repo.branches:
    print(branch)

# Create a new branch
repo.git.branch('my_new_branch')

# To checkout to a branch:
repo.git.checkout('branch_name')
