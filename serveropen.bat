@echo off

echo web server open
call forfastapi\Scripts\activate
cd backend
python main.py