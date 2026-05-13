#!/bin/bash
# » Konfiguration
BOT_PFAD="$HOME/daten/clouds/codestube/Coding/Python/Claralara/claralara.py"
VENV_ACTIVATE="$HOME/daten/venv/Claralara/bin/activate"

echo ""
echo "»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»"
echo " 🧙🏻‍♀️ Claralara Launcher for Ar#ch Linux x3"
echo "»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»» Codestube »»»"
echo "Letztes Update: 19.01.2026, 22:37"
echo ""
echo ""
echo "» 🪄 lade Zaubersprüchen..."
echo "» 🔎 Verbindung zum Codestube-Netzwerk wird hergestellt..."
ssh -N db &
SSH_PID=$!

# 2. Verbindungsaufbau einrichten
# Das Magie: 
# Wenn dieses Skript beendet wird (egal ob fertig oder durch STRG+C),
# wird automatisch der SSH-Tunnel (SSH_PID) gekillt.
trap "kill $SSH_PID 2> /dev/null; echo '» ⛓️‍💥 Verbindung getrennt.'; exit" EXIT INT TERM
sleep 1


# Prüfen, ob der Tunnel ready ist oder abgesoffen ist.
if ! ps -p $SSH_PID > /dev/null; then
    echo "» 🔴 Verbindung zum Codestube-Netzwerk konnte nicht hergestellt werden (1)!"
    exit 1
fi
echo "» 🟢 Verbindung zum Codestube-Netzwerk hergestellt. (PID $SSH_PID)."

# 3. Claralara starten.

echo "» 🧙🏻‍♀️ Claralara holt jetzt ihre Büchern..."
source "$VENV_ACTIVATE"
echo "» 🧙🏻‍♀️ Claralara geht jetzt ins Internet..."
python "$BOT_PFAD"

