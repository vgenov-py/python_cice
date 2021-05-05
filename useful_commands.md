## BASIC COMMANDS

* pwd --> working directory
* touch 
* cd --> stands for Change Directory
* (program you want to use) (file that you want to open with that program) // code main.py
* cd .. --> One level up of your pwd
* (program to open the pwd) . // code  .
* ls
* rm (remove file)
* rmdir (remove d if it's empty)
* rm /directory - r (rmdir if it's full)

## VENV

* python3 -m venv environment
* source environment/bin/activate
* pip install module_package

## GIT

* git init
* git remote add origin <url>
* git remote set-url <url> (para cambiar link remoto)
* git branch <name_of_branch> (crear rama)
* git checkout <name_of_branch> (cambiar rama)
* git add file <file2>
* git commit -m <"Your MSG"> (crear commit) 
* git push origin <name_of_branch> (pushear rama) (de local a remoto)
* git pull origin <name_of_branch> (pullear rama) (de remoto a local)
* git log (para ver todos nuestros commits)
* PARA MERGEAR
  1. git checkout <rama_donde_se_hará_el_mergeo>
  2. git merge <rama_a_mergear>
