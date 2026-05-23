# claralara.py ist das Zentrum des Bots.
# Hier werden alle Komponenten gesteuert und gestartet.

# claralara.py is the center of the bot.
# Here all components are controlled and started.

# Hier ist die Importliste
# Diese Importen sind ein Teil von Claralara

# These are the import list
# These imports are a part of Claralara
import claralara_config

# Diese Importen sind die erforderlichen Importierungen, damit Claralara richtig läuft.
# These imports are the required imports for Claralara to run properly.
import os
import sys
import asyncio
import random
import time
import sqlite3
import aiomysql
import mysql.connector
import datetime
from datetime import timedelta
import discord
# from discord import app_commands
from discord.commands import Option, OptionChoice
from discord.ext import tasks, commands
from discord.ui import Button, View
import json
from dotenv import load_dotenv

# Lade Discord Intents
# Load Discord Intents
intents = discord.Intents(guilds=True,
                          members=True, 
                          moderation=True,
                          messages=True,
                          guild_messages=True,
                          message_content=True)

# Hier werde ich zur Discord-Hexe, hihihiiiiiiiiiiiiii
# Here I become the Discord witch, hihihiiiiiiiiiiiiii
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None, case_insensitive=True)

# Claralara startet ...
# starts Claralara ...
@bot.event
async def on_ready() -> None:

    # Hier werden alle benötigen Informationen für den Betrieb kurz aufgelistet.
    # Here all the necessary information for the operation is briefly listed.
    print("==============================================================================")
    print(f"{claralara_config.Clientname} - {claralara_config.EmbedVersion}")
    print(f"Deine beste Freundin auf deinen Discord-Server xD")
    print(f"Your best friend on your Discord server xD")
    print("==============================================================================")
    print("I go online as:")
    print(f"{bot.user.name} - {bot.user.id}\n")
    print(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}")
    print(claralara_config.Botseite)
    print("==============================================================================\n")

    # Der Status-Task wird jetzt durchgeführt.
    # The status task is now being executed.
    status_task.start()
    log_task.start()

    # Hier werden ALLE DISCORDSERVER aufgelistet, die Claralara erreichen kann und geloggt.
    # Here all DISCORD SERVERS that Claralara can reach are listed and logged.
    with open("claralara_range.txt", "w", encoding="utf-8") as f:
        f.write("==============================================================================\n")
        f.write(f"= Claralara | Version {claralara_config.Version}                         {datetime.datetime.now().strftime(claralara_config.konsole_date_format)}\n")
        f.write("==============================================================================\n")
        f.write(f"{bot.user.name} - {bot.user.id}\n")
        f.write(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}\n")
        f.write("==============================================================================\n")
        f.write(f"{bot.user.name} is on {str(len(bot.guilds))} servers.\n")
        f.write(f"{bot.user.name} has a total of {str(len(bot.users))} members.\n")
        f.write("==============================================================================\n")
        f.write("\n")
        f.write(f"guild.id                      Guild Name\n\n")
        for guild in bot.guilds:
            
            f.write(f"{guild.id:<20}          {guild.name}\n")
        f.write("\n==============================================================================\n")
        f.write("\n")
        f.write(f"member.id                    Member Name\n\n")
        for guild in bot.guilds:
            for member in guild.members:
                f.write(f"{member.id:<20}         {member.name}\n")
        f.write("\n==============================================================================\n")
        f.write("Claralara by Codestube\n\n\n\n")
        f.write("©2022-2026 Codestube, @ClarigeClara\n")
        f.write("==============================================================================n")

    # Claralara Online-Bestätigung wird in der Konsole geschickt...
    # Claralara online confirmation is sent in the console...
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» I'm {bot.user.name} - {bot.user.id}!\n» My Version: {claralara_config.BotVersion}\n» I'm now Online!\n")
    
    # Claralara bestätigt, dass ihre Aktivitäten nun gezeigt werden.
    # Claralara confirms that her activities are now being shown.
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» I have created my Status-Loop.\n")
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» Every 5 minutes I will count my servers...\n")
    await asyncio.sleep(2)
    if claralara_config.Botmodus in claralara_config.preview_enabled:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara started successfully!\n")        
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | WARN\n» Claralara is in the Preview mode - features might be unstable!\n")
        return
    if claralara_config.Botmodus in claralara_config.Beta_enabled:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara started successfully!\n")
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | WARN\n» Claralara is in the Beta mode - features might be unstable!\n")
        return
    else:
        print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Info\n» Claralara started successfully!\n")

# Das hier ist die Aktivität von Claralara.
# This is the activity of Claralara.
@tasks.loop()
async def status_task() -> None:
    if claralara_config.Botmodus in claralara_config.preview_enabled:
        # Wenn der Botmodus bei Claralara-Config aktiviert wurde, geht es hier weiter...
        # When the bot mode is activated in Claralara-Config, it continues here...
        # If not, scroll down a bit until you read "else:".

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        # Here the status text "Version X.X.X" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "on XX Guilds" für 10 Sekunden angegeben.
        # Here the status text "on XX Guilds" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'on {str(len(bot.guilds))} Guilds.'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "Preview-Modus" für 10 Sekunden angegeben.
        # Here the status text "Preview mode" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'Preview-Mode'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(10)

    if claralara_config.Botmodus in claralara_config.Beta_enabled:
        # Wenn der Botmodus bei Claralara-Config aktiviert wurde, geht es hier weiter...
        # When the bot mode is activated in Claralara-Config, it continues here...

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        # Here the status text "Version X.X.X" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "auf XX Guilds" für 10 Sekunden angegeben.
        # Here the status text "on XX Guilds" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'on {str(len(bot.guilds))} Guilds.'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "Preview-Modus" für 10 Sekunden angegeben.
        # Here the status text "Beta mode" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'Beta-Mode'), status=discord.Status.do_not_disturb)
        await asyncio.sleep(10)
        

    if claralara_config.Botmodus in claralara_config.Beta_disabled:
        # Wenn der Botmodus bei Claralara-Config deaktiviert ist, geht es hier weiter...
        # When the bot mode is deactivated in Claralara-Config, it continues here...

        # Hier wird der Statustext "Version X.X.X" für 10 Sekunden angegeben.
        # Here the status text "Version X.X.X" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'{claralara_config.BotVersion}'), status=discord.Status.idle)
        await asyncio.sleep(10)

        # Hier wird der Statustext "auf XX Servern" für 10 Sekunden angegeben.
        # Here the status text "on XX Servers" is given for 10 seconds.
        await bot.change_presence(activity=discord.CustomActivity(f'auf {str(len(bot.guilds))} Servern.'),status=discord.Status.idle)
        await asyncio.sleep(10)

        # Und es wird ständig wiederholt
        # And it is repeated constantly

@tasks.loop()
async def log_task() -> None:
    while True:
        with open("claralara_live_range.txt", "w", encoding="utf-8") as f:
            f.write("==============================================================================\n")
            f.write(f"= Claralara | Version {claralara_config.Version}                         {datetime.datetime.now().strftime(claralara_config.konsole_date_format)}\n")
            f.write("==============================================================================\n")
            f.write(f"{bot.user.name} - {bot.user.id}\n")
            f.write(f"{claralara_config.Claralara_Copyright} - {claralara_config.Clientname}\n")
            f.write("==============================================================================\n")
            f.write(f"{bot.user.name} is on {str(len(bot.guilds))} servers active.\n")
            f.write(f"{bot.user.name} has a total of {str(len(bot.users))} members.\n")
            f.write("==============================================================================\n")
            f.write("\n")
            f.write(f"guild.id                      Guild Name\n\n")
            for guild in bot.guilds:
                
                f.write(f"{guild.id:<20}          {guild.name}\n")
            f.write("\n==============================================================================\n")
            f.write("\n")
            f.write(f"member.id                    Member Name\n\n")
            for guild in bot.guilds:
                for member in guild.members:
                    f.write(f"{member.id:<20}         {member.name}\n")
            f.write("\n==============================================================================\n")
            f.write("Claralara by Codestube\n\n\n\n")
            f.write("©2022-2026 Codestube, @ClarigeClara\n")
            f.write("==============================================================================n")
        await asyncio.sleep(600)

# Hier wird der Bot gestartet.
# Here the bot is started.
if __name__ == "__main__":
    # Der Token wird abgerufen.
    # The token is retrieved.
    load_dotenv()

    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» I am starting all my modules...\n")

    # Der Cog "claralara_cmd" wird gestartet. (Die Cog-ID ist 001)
    # The cog "claralara_cmd" is started. (The cog ID is 001)
    bot.load_extension("system.basis.claralara_cmd")
    print(f"» I have successfully loaded the Cog 'system.basis.claralara_cmd'.\n")

    # Der Bot loggt sich ein und schließt die Logdatei.
    # The bot logs in and closes the log file.
    print(f"{datetime.datetime.now().strftime(claralara_config.konsole_date_format)} | Clara\n» I am logging in...\n")

    bot.run(os.getenv(claralara_config.token))
