@echo off

cd backend
pip install -r ..\requirements.txt
cd ..

cd fronted
npm install
cd ..