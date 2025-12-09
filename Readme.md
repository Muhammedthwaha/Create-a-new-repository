Here i am experimenting with Git and Github

i tried different git commands
like:

first if we need:
    we need to fork the repository and clone it
    so clone command:
    
    git clone "Project file forked url (which is getting from 'Code')
     eg: git clone https://github.com/YOUR_github_USERNAME/EXAMPLE_REPO.git
        

    1. git init  (initialization)

    2. git remote add origin(url giving location name, we can choose any name, normally it is origin) <github url>

    3. git branch -M main

    4. git add (*.html:py, or file name, or . -> dot meansentire files) : transfer files to staging area

    5. git commit -m 'Commit message'

    6. git status (To check the status of files, like shere it is added or not, or commited or not, or to sport any modification)

    7. git push -u origin main (first time push, origin means url location name, main: branch name)

    8. git push (after first time use only these two words)

    9. git branch new-branch-name (to create new branch)

    10. git switch new-branch-name (To switch in to the newly created branch) / git checkout new-branch-name 

    11. git checkout -b <new-branch-name> (We can also create and switch to a new branch in a single command)

    12. git checkout new-branch-name (To switch in to the newly created branch)

    13. git merge <branch name> (merge one branch to another branch)

    14. git pull origin main (Pull the latest changes from the main, or default branch)
