@echo off
chcp 65001 > nul
SETLOCAL EnableDelayedExpansion

:: Konfiguration
:: Configuration
SET "PROJEKT_PFAD=D:\clouds\windows\codestube\Coding\Python\Claralara"
SET "PYTHON_EXE=D:\venv\windows\Claralara\Scripts\python.exe"
SET "BOT_SCRIPT=%PROJEKT_PFAD%\claralara.py"

TITLE 🧙🏻‍♀️ Claralara
ECHO.
ECHO »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
ECHO  🧙🏻‍♀️ Claralara Launcher for Windows
ECHO »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» Codestube »»»
ECHO Last Update: 07.04.2026, 14:36
ECHO.

ECHO » 🪄 loading magican spells...
ECHO » 🔎 Connection to the Codestube-Netzwerk is being established...

:: Startet SSH im Hintergrund. 
:: Sarts SSH in the background.
:: 'start /b' ist das Windows-Pendant zum '&' in Linux.
:: 'start /b' is the Windows equivalent to '&' in Linux.
start /b ssh -N db > nul 2>&1

:: Kurze Pause für den Verbindungsaufbau
:: Little timeout to give SSH some time to establish the connection
timeout /t 3 > nul

:: Einfache Prüfung, ob SSH läuft (Pendant zu 'ps -p')
:: Easy check if SSH is running (similar to 'ps -p')
tasklist /FI "IMAGENAME eq ssh.exe" 2>NUL | find /I /N "ssh.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo » 🔴 Connection to the Codestube-Netzwerk could not be established!
    pause
    exit /b 1
)
echo » 🟢 Connection established.

ECHO » 🧙🏻‍♀️ Loading Claralara...

:: Wechselt sicher ins Verzeichnis und startet Python
:: Change Directory and Run Python Script
cd /d "%PROJEKT_PFAD%"
"%PYTHON_EXE%" "%BOT_SCRIPT%"

:: Nach dem Beenden von Python: SSH-Tunnel schließen
:: To close the SSH tunnel after Python exits
echo » ⛓️‍💥 Closing connection...
taskkill /IM ssh.exe /F > nul 2>&1
TITLE 🧙🏻‍♀️ Claralara sleeping :c
ECHO » 🧙🏻‍♀️ Claralara is sleeping... bye bye.
pause