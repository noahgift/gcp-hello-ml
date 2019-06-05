## Steps to setup Github

1.  Create a public repo:
  * check Public
  * Initialize with a READM
  * add .gitignore PYthon
  * Add licence MIT
![github hello](https://user-images.githubusercontent.com/58792/58992683-58739e00-87a0-11e9-9b77-2e13116c2d35.png)

*Note on .gitignore*

It allows you to ignore frequently modified garbage files.  You probably will need to continuously update things in the file.  For example, if you use VSCode, it will create files you should ignore.  If you open in OS X finder, it will create .DS_Store and you should ignore.

2.  Clone locally repo:  two options:  https and ssh

`git clone `

* ssh method.  Set up ssh key
A.  `ssh-keygen -t rsa` press return several times
B.  Save file in `~/.ssh/id_rsa.pub`
C.  Print out public key to stdout

```
cat ~/.ssh/id_rsa.pub
```

Will look like this:

```
i4mQCVoMgB6MBTLuKrQNkYCRPI8
i4mQCVoMgB6MBTLuKrQNkYCRPI8
blah...
```
D.  go to profile and add ssh-key (public key!!!).
E.  git clone your repo using ssh.

* How to do this in Cloud Shell

AA. Launch cloudshell
BB. create src directory: `mkdir -p src && cd src`
CC. do same steps as above



3.  Create a python virtual environment

if on cloud shell could be similar to:

```virtualenv  ~/.hello-github```

4.  Create a Makefile
5.  Create a requirements.txt

