@echo off
chcp 65001 > nul
SETLOCAL EnableDelayedExpansion

:: Konfiguration
SET "PROJEKT_PFAD=D:\clouds\windows\codestube\Coding\Python\Claralara"
SET "PYTHON_EXE=D:\venv\windows\Claralara\Scripts\python.exe"
SET "BOT_SCRIPT=%PROJEKT_PFAD%\claralara.py"

TITLE 🧙🏻‍♀️ Claralara
ECHO.
ECHO »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»
ECHO  🧙🏻‍♀️ Claralara Launcher for Windows
ECHO »»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» Codestube »»»
ECHO Letztes Update: 07.04.2026, 14:36
ECHO.

ECHO » 🪄 lade Zaubersprüchen...
ECHO » 🔎 Verbindung zum Codestube-Netzwerk wird hergestellt...

:: Startet SSH im Hintergrund. 
:: 'start /b' ist das Windows-Pendant zum '&' in Linux.
start /b ssh -N db > nul 2>&1

:: Kurze Pause für den Verbindungsaufbau
timeout /t 3 > nul

:: Einfache Prüfung, ob SSH läuft (Pendant zu 'ps -p')
tasklist /FI "IMAGENAME eq ssh.exe" 2>NUL | find /I /N "ssh.exe">NUL
if "%ERRORLEVEL%"=="1" (
    echo » 🔴 Verbindung zum Codestube-Netzwerk konnte nicht hergestellt werden!
    pause
    exit /b 1
)
echo » 🟢 Verbindung hergestellt.

ECHO » 🧙🏻‍♀️ Claralara wird gestartet...

:: Wechselt sicher ins Verzeichnis und startet Python
cd /d "%PROJEKT_PFAD%"
"%PYTHON_EXE%" "%BOT_SCRIPT%"

:: Nach dem Beenden von Python: SSH-Tunnel schließen
echo » ⛓️‍💥 Beende Verbindung...
taskkill /IM ssh.exe /F > nul 2>&1
TITLE 🧙🏻‍♀️ Claralara beendet :c
ECHO » 🧙🏻‍♀️ Claralara wurde beendet.
pause