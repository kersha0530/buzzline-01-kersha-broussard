## Git Add-Commit-Push

After making changes on our machine, we need to:

1. git **add** the files to source control.
2. git **commit** the files as a named set of changes.
3. git **push** the files to the GitHub repository.

Reading takes longer than the commands. 
The first times are more difficult, but we'll do these often and you'll soon be proficient.

Open a terminal (PowerShell if Windows, default for Mac/Linux) and run each command one at a time, waiting for it to finish before running the next. 

Use the up arrow to access a previously entered command. 

```shell
git add .
git commit -m "Initial change"
git push -u origin main
```

IMPORTANT: Always change the commit message to reflect what you did - e.g., "Add new producer", "Add new consumer", "Customize producer", "Update consumer alert", "Update README.md".
Professional communication skills make valuable team members.  

Later git pushes can be simplified - try just git push and see how it goes. 

```
git push
```

