from git import Repo

repo = Repo('/path/to/local/repo')

# Add files. Accepts a list of files
repo.index.add(['path/to/file_1', '/path/to/file_2',.......,'/path/to/file_n'])

# Commit
repo.index.commit('your commit message')
