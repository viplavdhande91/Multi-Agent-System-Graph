@echo off
cmd /k "cd /d %userprofile%\Desktop\tosend\MAS\venv_MAS\Scripts & activate & cd /d %userprofile%\Desktop\tosend\MAS &   start http://127.0.0.1:8000    & python manage.py runserver"

