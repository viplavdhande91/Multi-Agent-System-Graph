@echo off
cmd /k "cd /d %userprofile%\Desktop\tosend\MAS  &  python -m venv ./venv_MAS & cd /d  %userprofile%\Desktop\tosend\MAS\venv_MAS\Scripts & activate   & cd /d  %userprofile%\Desktop\tosend\MAS & pip install -r requirements.txt"

