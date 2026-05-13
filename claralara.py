# claralara.py ist das Zentrum des Bots.
# Hier werden alle Komponenten gesteuert und gestartet.

# Hier ist die Importliste
# Diese Importen sind ein Teil von Claralara
import claralara_config

# Diese Importen sind die erforderlichen Importierungen, damit Claralara richtig läuft.
import os
import sys
import asyncio
import random
import time
import sqlite3
import aiomysql
import mysql.connector
import datetime
import yaml
import ezcord
from ezcord import I18N
from datetime import timedelta
import discord
# from discord import app_commands
from discord.commands import Option, OptionChoice
from discord.ext import tasks, commands
from discord.ui import Button, View
import json
from dotenv import load_dotenv

# Lade Discord Intents
intents = discord.Intents(guilds=True,
                          members=True, 
                          moderation=True,
                          messages=True,
                          guild_messages=True,
                          message_content=True)

# Hier werde ich zur Discord-Hexe, hihihiiiiiiiiiiiiii
bot = ezcord.PrefixBot(
    command_prefix='c!',
    intents=intents,
    language="de",
    translations_path="lang"
)


# Claralara startet ...
@bot.event
async def on_ready() -> None:

    # Hier werden alle benötigen Informationen für den Betrieb kurz aufgelistet.
    print("==============================================================================")
    print(f"{claralara_config.Clientname} - {claralara_config.EmbedVersion}")
    print(f"Deine beste Freundin auf deinen Discord-Server xD")
    print("==============================================================================")
    print("Ich gehe nun Online als:")
    print(f"{bot.user.name} - {bot.user.id}\n")
    print(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}")
    print(claralara_config.Botseite)
    print("==============================================================================\n")

    # Der Status-Task wird jetzt durchgeführt.
    status_task.start()
    log_task.start()

    # Hier werden ALLE DISCORDSERVER aufgelistet, die Claralara erreichen kann und geloggt.
    with open("claralara_range.txt", "w", encoding="utf-8") as f:
        f.write("==============================================================================\n")
        f.write(f"= Claralara | Version {claralara_config.Version}                         {datetime.datetime.now().strftime(claralara_config.konsole_date_format)}\n")
        f.write("==============================================================================\n")
        f.write(f"{bot.user.name} - {bot.user.id}\n")
        f.write(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}\n")
        f.write("==============================================================================\n")
        f.write(f"{bot.user.name} ist auf {str(len(bot.guilds))} Servern aktiv.\n")
        f.write(f"{bot.user.name} hat insgesamt {str(len(bot.users))} Mitglieder.\n")
        f.write("==============================================================================\n")
        f.write("\n")
        f.write(f"guild.id                      Server-ID\n\n")
        for guild in bot.guilds:
            
            f.write(f"{guild.id:<20}          {guild.name}\n")
        f.write("\n==============================================================================\n")
        f.write("\n")
        f.write(f"member.id                    Mitgliedername\n\n")
        for guild in bot.guilds:
            for member in guild.members:
                f.write(f"{member.id:<20}         {member.name}\n")
        f.write("\n==============================================================================\n")
        f.write("CODESTUBE INTERN\n\n\n\n")
        f.write("©2022-2026 - @clarigeclara - Claralara\n")
        f.write("==============================================================================n")

    # Claralara Online-Bestätigung wird in der Konsole geschickt...
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Ich bin {bot.user.name} - {bot.user.id}!\n» Meine Version: {claralara_config.BotVersion}\n» Ich bin nun Online!\n")
    
    # Claralara bestätigt, dass ihre Aktivitäten nun gezeigt werden.
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Ich habe mein Status-Loop erzeugt.\n")
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Alle 5 Minuten werde ich mal meine Server zählen...\n")
    await asyncio.sleep(2)
    if claralara_config.Botmodus in claralara_config.preview_aktiviert:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara wurde erfolgreich gestartet!\n")        
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | WARN\n» Claralara befindet sich in der Preview - Funktionen könnten instabil sein!\n")
        return
    if claralara_config.Botmodus in claralara_config.Beta_aktiviert:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara wurde erfolgreich gestartet!\n")
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | WARN\n» Claralara befindet sich in der Beta - Funktionen könnten instabil sein!\n")
        return
    else:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara wurde erfolgreich gestartet!\n")

# Das hier ist die Aktivität von Claralara.
@tasks.loop()
async def status_task() -> None:
    if claralara_config.Botmodus in claralara_config.preview_aktiviert:
        # Wenn der Botmodus-Modus bei Claralara-Config aktiviert wurde, geht es hier weiter...
        # Wenn nicht, dann scroll etwas runter, bis du "else:" liest.

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "auf XX Servern" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'trolle auf {str(len(bot.guilds))} Servern.'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "Preview-Modus" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'Preview-Modus'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(10)

    if claralara_config.Botmodus in claralara_config.Beta_aktiviert:
        # Wenn der Botmodus-Modus bei Claralara-Config aktiviert wurde, geht es hier weiter...

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "auf XX Servern" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'trolle auf {str(len(bot.guilds))} Servern.'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "Preview-Modus" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'Beta-Modus'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(10)
        

    if claralara_config.Botmodus in claralara_config.Beta_deaktiviert:
        # Wenn der Botmodus-Modus bei Claralara-Config deaktiviert ist, geht es hier weiter...

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "auf XX Servern" für 10 Sekunden angegeben.
        await bot.change_presence(activity=discord.CustomActivity(f'trolle auf {str(len(bot.guilds))} Servern.'),status=discord.Status.idle)
        await asyncio.sleep(10)

        # Und es wird ständig wiederholt

@tasks.loop()
async def log_task() -> None:
    while True:
        # print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Ich glaub' ich schau mich mal kurz rum...\n")
        with open("claralara_live_range.txt", "w", encoding="utf-8") as f:
            f.write("==============================================================================\n")
            f.write(f"= Claralara | Version {claralara_config.Version}                         {datetime.datetime.now().strftime(claralara_config.konsole_date_format)}\n")
            f.write("==============================================================================\n")
            f.write(f"{bot.user.name} - {bot.user.id}\n")
            f.write(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}\n")
            f.write("==============================================================================\n")
            f.write(f"{bot.user.name} ist auf {str(len(bot.guilds))} Servern aktiv.\n")
            f.write(f"{bot.user.name} hat insgesamt {str(len(bot.users))} Mitglieder.\n")
            f.write("==============================================================================\n")
            f.write("\n")
            f.write(f"guild.id                      Server-ID\n\n")
            for guild in bot.guilds:
                
                f.write(f"{guild.id:<20}          {guild.name}\n")
            f.write("\n==============================================================================\n")
            f.write("\n")
            f.write(f"member.id                    Mitgliedername\n\n")
            for guild in bot.guilds:
                for member in guild.members:
                    f.write(f"{member.id:<20}         {member.name}\n")
            f.write("\n==============================================================================\n")
            f.write("CODESTUBE INTERN\n\n\n\n")
            f.write("©2022-2026 - @clarigeclara - Claralara\n")
            f.write("==============================================================================n")
        await asyncio.sleep(600)

# Hier wird der Bot gestartet.
if __name__ == "__main__":
    # Der Token wird abgerufen.
    load_dotenv()

    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Ich starte nun alle meine Module...")

    # Der Cog "claralara_cmd" wird gestartet. (Die Cog-ID ist 001)
    # bot.load_extension("system.basis.claralara_cmd")
    # print(f"» Ich habe den Cog 'system.basis.claralara_cmd' erfolgreich geladen.")

    # Der Bot loggt sich ein und schließt die Logdatei.
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Ich logge mich ein...\n")
    bot.run(os.getenv(claralara_config.token))
