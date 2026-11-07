# Script to export Git commit log into git_commit_log.txt as required by Regulation 12
git log --graph --pretty=format:'%h -%d %s (%cr) <%an>' --abbrev-commit --date=relative > git_commit_log.txt
Write-Host "Git log exported to git_commit_log.txt successfully."
