@echo off
:: Set the Python version and environment name
set PYTHON_VERSION=3.12
set ENV_NAME=wintts

:: Create the Conda environment with the specified Python version
echo Creating Conda environment with Python %PYTHON_VERSION%...
conda create --name %ENV_NAME% python=%PYTHON_VERSION% -y

:: Activate the Conda environment
echo Activating the Conda environment...
call activate %ENV_NAME%

:: Install pip-tools if not already installed
echo Installing pip-tools...
pip install pip-tools

:: Generate the requirements.txt file from requirements.in
echo Creating requirements.txt from requirements.in...
pip-compile requirements.in

:: Install the requirements from requirements.txt
echo Installing the requirements...
pip install -r requirements.txt

echo Setup complete.
