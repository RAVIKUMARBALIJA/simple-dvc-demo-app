create a directory manually

open cmd > code .

conda create -n windoweq python=3.7 -y

conda activate windoweq

pip install -r requirements.txt

create directories using template.py

create datagiven and place the data set in it

git init

dvc init

dvc add .\datagiven\wineqality.csv

git add .

git config --global user.mail ****************

git config --global user.name ***************

git commit -m "first commit"

update readme now

git add .

git commit -m "update readme"

git remote add origin repo_link
git branch -M main

git push origin main

update params.yaml
write get_data
write load_data - to load raw data
write dvc.yaml - dvc run -n stages - tedius

dvc.yaml
dvc repro

split_data.py

dvc.yaml
dvc repro
train_and_evaludate.py

dvc.yaml

dvc metrics show
dvc metrics diff

tox command  - tox

for rebuilding -
'''bash
tox -r

pyetst command
'''bash
pytest -v

setup commands
'''bash

pip install -e .

build  your own package commands-
'''bash
python setup.py sdist wheel - to create a package for app

pip install jupyterlab
jupyter-lab notesbooks 


conda activate windoweq
   2 & "C:/Users/Poornima T/.conda/envs/windoweq/p... 
   pytest -v
   4 tox
   5 tox
   7 notepad setup.py
   8 pip install -e .
   9 pip freeze

