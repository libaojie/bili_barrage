@echo off

python -m pipenv --venv

:: 复制必要的dll
md C:\Users\li\.virtualenvs\dataflow_tool-1zxvCElD\DLLS\
copy C:\Users\li\Documents\01_Code\09_Gitlab\dataflow_tool\package\windows\sqlite3.dll C:\Users\li\.virtualenvs\dataflow_tool-1zxvCElD\DLLS\sqlite3.dll

:: 打包
rd /s /q build
python -m pipenv run python setup.py build



pause