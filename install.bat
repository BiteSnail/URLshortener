@echo off

cd backend
if exist .\forfastapi\(
    
)
else (
    python -m venv forfastapi
)
call forfastapi\Scripts\activate
pip install -r requirements.txt
call forfastapi\Scripts\deactivate.bat
cd ..

cd fronted
npm install
cd ..