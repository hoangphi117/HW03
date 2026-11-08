# Script to export Git commit log into git_commit_log.txt as required by Regulation 12 (UTF-8 encoding)
git log --graph --pretty=format:'%h -%d %s (%cr) <%an>' --abbrev-commit --date=relative | Out-File -FilePath git_commit_log.txt -Encoding utf8
Write-Host "Git log exported to git_commit_log.txt successfully (UTF-8)."
