# UrbanAg Project

## Git Commands:

### Clone
Creates a fresh new copy of this project on your local computer.  Only do this once - whenever you are starting from scratch on a new computer.
```
git clone https://github.com/flanasonic/UrbanAg.git
```

### Local vs. Remote Repositories
The code stored on GitHub is in what we'll call your **remote** repository.  The code stored on your local computer after you clone is your **local** copy.

The remote repository - the GitHub repository - has the name **origin** by default when you clone.   We'll use this name later...

When there are multiple **local** copies (e.g. when you have cloned on multiple computers or when more than one person has cloned on to their own computer) there may be changes in the GitHub (**remote**) repository that you have not recieved into your local copy yet.

To update your **local** copy, use the git fetch command.

### Fetch
This checks the remote repository for any changes that you do not yet have locally.  To update your local copy, use the name **origin** with the fetch command to tell git you want to fetch updates from the **origin** a.k.a. the GitHub copy.
```
git fetch origin
```

* *Note: this will not make any changes to any files you are currently working on.  It only updates the information git has about the latest changes from the GitHub copy* *


### Branches
By default after you clone you will be on the main branch.

To see all of the branches that have been created/pushed to GitHub go here: https://github.com/flanasonic/UrbanAg/branches 

To show other branches you have locally using git.
```
git branch -l
```
*Note: This command may run a program called "less" to display the list of branches.  If it does this, hit q or ctrl-c to exit when you're done*

To show all branches including those that are on the remote (may include new ones you have not seen before) do:
```
git branch -lv
```

### Status
It's a good idea to set up your local command line (e.g. gitbash on Windows) to show what branch youare working on when you have changed directories into a folder that is inside a git project.   Otherwise, to show what branch you are on:
```
git status
```
If you run this command from inside a folder that is in a git project, the first line you will see will be something like:
```
On branch main
```

### Checkout
To create a new branch based on whatever branch you currently have checked out:
```
git checkout -B newbranchname
```
(replace newbranchname with whatever you want to call your branch)

To switch to another branch, do:
```
git checkout branchname
```
(e.g. substitute main for *branchname* to switch back to the main branch)

*Note if you've made changes to files but have not yet committed those changes git will prevent you from switching branches.  In this case, you can either stash your chages - put them in a temporary holding area - or commit them first before switching branches*

more on git stash here: https://opensource.com/article/21/4/git-stash

### Push
To push changes you've made on the branch you have checked out (see git status above) do:
```
git push origin branchname
```
substitute branchname for the branch you want to push.

### Checking out a branch for the first time
After you fetch (see fetch above) if a new branch was created on the **remote** GitHub repository since your last fetch, you can simply check it out with
```
git checkout branchname
```
See Checkout above - this is the same command.  The only point here is that when you call git checkout for the first time for a branch you did not create locally you will get an up-to-date copy of the files on the **remote**.   After you've checked out, you'll need to use a different command to pull in any changes that someone has pushed to the **remote**. (see below)

### Pulling changes into a branch
If you are working on a branch and expect that there are changes on the **remote** repository that you do not yet have locally, the simplest way to get them is:
1. Make sure you have the branch you want to update checked out
2. Do:
```
git pull
```
If there are chagnes to retrieve, git will display some lines with + and + marks indicating chagnes that were applied by the pull command.

### History of changes for a branch
To show an ordered list of the changes that have been made to a branch:
```
git log
```
This should show the most recent commit at the top of the list and earlier changes follow in order below.

To see a more detailed view of the files changed for each commit do:
```
git log --stat
```
This should display something like the following:
```
commit 454cc60d06609f925952810adedf6048d490f18b (HEAD -> main, origin/main, origin/HEAD)
Author: Julie Flanagan <flanasonic@gmail.com>
Date:   Mon Nov 29 16:33:45 2021 -0500

    some small updates

 UrbanAg.db         | Bin 12288 -> 12288 bytes
 company.json       |   1 +
 data/facility.json |  20 --------------------
 facility.json      |   1 +
 make_api.py        |  39 +++++++++++++++------------------------
 make_json.py       |  33 +++++++++++++++++++++------------
 make_my_db.py      |  41 ++++++++++++++++++++++-------------------
 populate.py        |  46 ++++++++++++++++++++--------------------------
 rowarrays.js       |   0
 9 files changed, 80 insertions(+), 101 deletions(-)
```
There are many more options for viewing details of changes applied over time.   See here for more info:
https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History 

