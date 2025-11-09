@echo off
echo Starting School Management System...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install/upgrade dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet
echo.

REM Run the application
echo Launching application...
echo.
streamlit run app.py

pause
