# WILLKOMMEN BEI DER CLARALARA-CONFIG
# Die Software muss neu gestartet werden, damit Änderungen wirksam werden.
# © 2022 - 2026 | @clarigeclara | config 
import datetime
import discord
import aiomysql
import os
from dotenv import load_dotenv

load_dotenv()

# 1 - Bot-Identität

# Wie heißt der Bot?
Clientname = "Claralara"

# 1.1 - Versionsangabe

# Preview-Version
previewversion = 16

# Beta-Version
Betaversion = 1

# Versionstypen
Majorversion = 7
Minorversion = 0
Patchversion = 0
Updatenummer = 93
Buildnummer = f"24{Patchversion}{Updatenummer}"

# 1.2 - Zeitangabe für das Update /claralara info:
# Jahr z.B. 2022:
Buildjahr = "2026"
# Monat z.B. 03:
Buildmonat = "05"
# Tag z.B. 10
Buildtag = "13"
# Stunde z.B. 02
Buildstunde = "22"
# Minute z.B. 37
Buildminute = "16"

# 1.3 - Botmodus-Einstellungen
# 0 | Stable-Release
# 1 | Beta-Release
# 2 | Preview-Release (Entwicklermodus)
Botmodus = 2

# 1.4 - Anzahl angaben:
Befehle = 33
Eastereggs = 32
Witzen = 701
Spiele = 0
Language = "deutsch"

# 1.5 - Claralara Links
Botseite = "https://claralara.de/"
bot_einladen_url = "https://claralara.de/invite"
supportserver = "https://claralara.de/discord"
Claralara_Copyright = f"©2022-{Buildjahr} - @clarigeclara @muninotowo"

# 1.6 - Formatedate_format = "%d.%m.%Y, um %H:%M Uhr."
botinfo_date_format = "%d.%m.%Y - %H:%M"
konsole_date_format = "%d.%m.%Y - %H:%M:%S"
logdataformat = datetime.datetime.now().strftime("%Y.%m.%d")
Startzeit = datetime.datetime.now()

# 1.7 - Kanälen
adminchat = 1141789751951765695
feedback_channel = 1109423978965110817
bugreport_channel = 1109423978965110816
userreport_channel = 1197096013006127104
serverreport_channel = 1197096272818077726
suggestion_channel = 1109423978965110815

# 3.8 Emotes (Zentral)
Error_emote = "<a:Capoo_Work:964760657251684352>"
Support_icon = "<:Emotional_Damage:939113435688493087>"
hinweis_emote = "<:fucking_ring_ring_ring:974961199995318374>"
Befehl_angefordert_emote = "<:fucking_ring_ring_ring:974961199995318374>"
Befehl_abgeschlossen_emote = "<:accepted:1156817130801598584>"
Befehl_fehlgeschlagen_emote = "<:declined:1156816646711812158>"
claralara_hilfe_emote = "<:Claralara:1462012998578081981>"
mitgliedhilfe_emote = "<a:Blob_wob_work:992051095994122291>"
spielhilfe_emote = "<:MK_ItemBox:942051090688528395>"
adminhilfe_emote = "<:MK_Blueshell:939106975847940127>"
Ofenkartoffeln = "<:WG2_Baked_Potato:1071230093868937246>"


# 2.1 - Speichervorgangstexte
Speichervorgangtext = ["ehmmm warte kurz, bitte...",
                       "Ich merkel mir das schnell...",
                       "Uh okay, warte kurz...",
                       "hmmm interesannt...",
                       "Moment bitte... das schreib ich mir auf!",
                       "Ich speichel mir das erstmal...",
                       "Ah okay, so ist das also... warte kurz..."]

# 2.2 - Ofenkartoffeltexte für /daily
gier = ["Ich bin mir gaaaaanz sicher, dass du heute schon von mir was bekommen hast. c:",
        "Nein, nein. Heute nicht nochmal. c:",
        "Du bist so gierig... c:",
        "Die Kinder aus Afirka haben auch hunger, weißt du? c:",
        "Du willst es doch nur nochmal probieren, wa? c:",
        "Meine Shulkerkisten wären eiferüchtig, wenn ich es zulassen würde... c:",
        "Hast du schon deine Kartoffeln schon gegessen!? :o",
        "Ich glaube, du bist süchtig nach täglichen Belohnungen... c:",
        "Morgen kannst du es wieder probieren. c:"]

abgeholt = ["Guten Hunger! c:",
            "Komm' morgen wieder! Da gibt es vielleicht mehr c:\n-# oder auch nicht xD",
            "Ich hoffe, dir platzt der Magen nicht... c:",
            "Mit Kräuterquark schmeckt's am besten! c:",
            "Hmmmmmm lecker :yum: ...",
            "Du bekommst von mir die HEILIGEN OFENKARTOFFELN. c:",
            "Ich hoffe, du hast bald keine 500.000 Stück... xD",
            "Wieso? Keine Ahnung! c:",
            "Yeeeeeeeee Ofenkartoffeln! c:",
            "Bei anderen hast du Kekse, bei mir hast du Ofenkartoffeln! c:",
            "Ofenkartoffeln auf die **#1**! c:",
            "Ich bin nicht bescheuert, aber du bist hungrig, deswegen gönn' dir ein Paar! c:" ]

wusstest_du_Schon = ["Alexander der Große war klein: gerade mal 1,50 Meter groß. - Selbst mein Minikühlschrank ist größer.",
                     "Jeder 3. Deutsche telefoniert täglich mit seiner Mutter. - Und ich mach's mit deiner.",
                     "34 Prozent der Deutschen träumen nachts von ihrer Arbeit. - Wie dumm.",
                     "Zu den Nebenwirkungen von Aspirin gehören Kopfschmerzen. - Deswegen nutze ich Ibo400",
                     "An einer Supermarktkasse steht man in Deutschland im Schnitt 7 Minuten. - naja...",
                     "Der Film „Titanic“ dauert genauso lange, wie das echte Schiff unterging. - Ein Trauerspiel.",
                     "87% aller Treppenunfällen passieren auf Treppen :D - nicht von Gumball geklaut. xD",
                     "Jeder, der die AfD wählt, fickt sich selbst, wenn die AfD gewinnen sollte. - Quelle: ",
                     "Bei der Ampelregierung fiel das gelbe Licht zuerst aus, weil die SPD rot sah. - xD",
                     "Wenn du im Supermarkt arbeitest, merkst du, wie dumm einige Kunden wirklich sind.",
                     "Wenn du eine Pfandflasche abgibst, hast ein Viertel eines Euros - Ein Viertel Euro c:",
                     "Wenn du im GTA V Online von direkt nach den Spawn von einen NoobBike geklascht wirst, weißt du, dass der Spieler erst 13 ist und bei Englisch ne 5 geschrieben hat.",
                     "Mit einer Cola kannst du ein Klo putzen. - Hab ich bei deiner Schwester getestet. ",
                     "Dein Bruder ist schlecht in Fortnite :D",
                     "Wenn du 50,00 € abhebst, wird dir 50,00 € vom Konto abgezogen.",
                     "Lösche ein Ölbrand mit Wasser, wenn du ein Kücheninferno haben möchtest\nHinweis: Wenn du es tatsächlich tun solltest, dann bist du einfach nur dumm.",
                     ""]


# 2.3 - Emotes mit Spruch
Error_title = "<:Emotional_Damage:939113435688493087> Ein Fehler ist aufgetreten!"


# 6.0.0 Memes und Gifsammlung:
ups = ["https://media1.tenor.com/m/B00IxZIObHIAAAAC/ups-shurjoka.gif",
       "https://media1.tenor.com/m/uAoffBgXwhUAAAAC/collapse.gif",
       "https://media1.tenor.com/m/VlrUPAyJ52QAAAAd/fail-paletjack.gif",
       "https://media1.tenor.com/m/pB6aU5t1ieoAAAAd/turdis-blown.gif",
       "https://media1.tenor.com/m/SPyV9ahcTa4AAAAC/taco-bell.gif",
       "https://media1.tenor.com/m/CEcDl9Keri8AAAAd/pie-cake.gif",
       "https://media1.tenor.com/m/rEuThB12E2YAAAAd/spongebob-chum-bucket.gif",
       "https://media1.tenor.com/m/ScSG7QhShm0AAAAC/spongebob-squidward.gif",
       "https://media1.tenor.com/m/XgLY1xuzvPoAAAAC/spongebob-explode.gif",
       "https://media1.tenor.com/m/QYbrVKNZGc4AAAAd/forklift-accident.gif",
       "https://media1.tenor.com/m/mSLxOhZjIxAAAAAC/car-crash-bust.gif",
       "https://media1.tenor.com/m/uGp2Q9e39a0AAAAd/accident-escape.gif",
       "https://media1.tenor.com/m/EjysW9dWLQEAAAAd/westernwlnd-squidward.gif",
       "https://media1.tenor.com/m/tPAufO_SUq4AAAAC/squidward-trolled.gif"
       "https://media1.tenor.com/m/vFfNobV3F38AAAAC/spongebob-squidward.gif",
       "https://media1.tenor.com/m/7HUogy7rXs4AAAAC/feel-me-think-about-it.gif",
       "https://media1.tenor.com/m/ZVwQtkeksfQAAAAC/the-blues-brothers-toys-r-us.gif"]

banned = ["https://media1.tenor.com/m/ajMUAZf2ozkAAAAC/fake-news.gif",
          "https://media1.tenor.com/m/bHzU4vveMsUAAAAC/tanmay-bhat-noob.gif",
          "https://media1.tenor.com/m/Ow2L8IP50uYAAAAd/champoy-el-risitas.gif",
          "https://media1.tenor.com/m/9zCgefg___cAAAAC/bane-no.gif",
          "https://media1.tenor.com/m/gnXapwOEaTEAAAAC/spongebob-ban.gif",
          "https://media1.tenor.com/m/atbWSwDthPkAAAAC/case-caseoh.gif",
          "https://media1.tenor.com/m/3zg6UVAaWTsAAAAC/ban-elmo.gif",
          "https://media1.tenor.com/m/If9jKEgWxNYAAAAC/spongebob-patrick.gif",
          "https://media1.tenor.com/m/Nh4zsPX9mYsAAAAd/you-are-banned-banned.gif",
          "https://media1.tenor.com/m/u53w---Rf9EAAAAd/when-your-team-too-good-ban.gif",
          "https://media1.tenor.com/m/-3HWCDKFwLEAAAAd/caseoh-caseoh-games.gif",
          "https://media1.tenor.com/m/_bkhBrWDRZ4AAAAC/trump-donaldtrump.gif",
          "https://media1.tenor.com/m/1DB5w_53GeUAAAAd/axel-voss-video.gif",
          "https://media1.tenor.com/m/Q5hHkkZhK7IAAAAd/minions-banned.gif"]

syntax_error = ["https://media1.tenor.com/m/MxvGiauFTesAAAAC/helpies.gif",
                "https://media1.tenor.com/m/58QLsz1tPowAAAAd/error-glitch.gif",
                "https://media1.tenor.com/m/CXzCRtvwoNYAAAAd/shdw-genesysgo.gif",
                "https://media1.tenor.com/m/8ES7IbzvcGsAAAAC/404-355.gif",
                "https://media1.tenor.com/m/PPOe9MawAvsAAAAd/404-not-found.gif",
                "https://media1.tenor.com/m/96ydiYB2lkkAAAAC/developers-fuck.gif"]

Gone = ["https://media1.tenor.com/m/z0X6U7McZPcAAAAd/bye-im-out.gif",
        "https://media1.tenor.com/m/st5gnG_jxsAAAAAC/that%27s-all-folks.gif",
        "https://media1.tenor.com/m/N928xgJE5tQAAAAC/gotosleep-final.gif"]

OHHHH = ["https://media1.tenor.com/m/EfSi6uDyZ9UAAAAC/terminalmontage-star-fox.gif"]


##################################################################################################################
# 999.0.0 - GEFAHRENZONE!
# Hier endet die Config für dich, denn hier beginnt die Logik.
##################################################################################################################

# LOGIKBLOCK - Bitte nichts ändern!
print("\n\n\n==============================================================================")
print(f"= Claralara | Build: {Majorversion}.{Minorversion}.{Patchversion} ({Buildnummer})                    {datetime.datetime.now().strftime(konsole_date_format)}")
print("==============================================================================")
Update = f"Zul. aktualisiert: {Buildtag}.{Buildmonat}.{Buildjahr} - {Buildstunde}:{Buildminute}"
Beta_aktiviert = [1, "y", "ja", "JA", "yes", "YES"]
Beta_deaktiviert = [0, "nein", "n", "no"]
preview_aktiviert = [2, "pre", "preview", "demo"]
KeinModus = [3, 4, 5, 6, 7, 8, 9, " "]

if Botmodus in Beta_aktiviert: 
    token = "CLARABETA"
    Version = f"{Majorversion}.{Minorversion}.{Patchversion}"
    TextVersion = f"Version {Version} (Beta {Betaversion})"
    EmbedVersion = f"Ver. {Version} (Beta {Betaversion})"
    BotVersion = f"Ver. {Version} (Beta {Betaversion})"
    Build = f"{Buildnummer}"
    anzahl_feedback = "---"
    anzahl_top_gg_sterne = "-,- ⭐"
    anzahl_sterne = "-,- ⭐"
    anzahl_befehle = "---"
    anzahl_eastereggs = "---"
    anzahl_witzen = "---"
    anzahl_spiele = "---"
    Sprache = Language
    Cooldown_dauer = 120

    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» Der BETA-MODUS ist aktiviert!\n")
    Datenbank = {
        'host': os.getenv("DBHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DB1"),
        }
    ZentraleDatenbank = {
        'host': os.getenv("DBHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DBHQ"),
        }
    emote_continue = "<:continue:1302717401342939177>"
    emote_back = "<:back:1302717392865988670>"
    emote_settings = "<:settings:1302717384741752902>"
    emote_slash = "<:slash:1302717377057919066>"
    emote_error = "<:error:1302717367851421770>"
    emote_done = "<:done:1302717359592706168>"
    emote_witcherhat = "<:witcherhat:1302714643952701491>"
    emote_web = "<:web:1302714636574920754>"
    emote_wartungen = "<:wartungen:1302714621299523595>"
    emote_wartung = "<:wartung:1302714612247953471>"
    emote_timeout = "<:timeout:1302714604576571394>"
    emote_time = "<:time:1302714597253451908>"
    emote_ticket = "<:ticket:1302713949854236815>"
    emote_tester = "<:tester:1302713941256048732>"
    emote_star = "<:star:1302713934469533726>"
    emote_skull = "<:skull:1302714540714360833>"
    emote_smile = "<:smile:1302714548939390977>"
    emote_snowflake = "<:snowflake:1302714558955126865>"
    emote_shopping = "<:shopping:1302714532287877120>"
    emote_shield = "<:shield:1302714525581316216>"
    emote_share = "<:share:1302714515846205450>"
    emote_searching = "<:searching:1302714499933012048>"
    emote_reboot = "<:reboot:1302714491972223068>"
    emote_question = "<:question:1302714484757889044>"
    emote_ping = "<:ping:1302714472636354590>"
    emote_newby = "<:newby:1302714459696922746>"
    emote_mod_action = "<:mod_action:1302714448678621204>"
    emote_members = "<:members:1302714436624187457>"
    emote_member = "<:member:1302714428122468372>"
    emote_mail = "<:mail:1302714413001736322>"
    emote_lolli = "<:lolli:1302714405557112852>"
    emote_like = "<:like:1302714399315853434>"
    emote_keule = "<:keule:1302714393242505357>"
    emote_idea = "<:idea:1302714386409852939>"
    emote_help = "<:help:1302714379464216586>"
    emote_heart = "<:heart:1302714371511685202>"
    emote_gift = "<:gift:1302714363722862735>" 
    emote_forbidden = "<:forbidden:1302714356773027910>"
    emote_fire = "<:fire:1302714348317179914>"
    emote_event = "<:event:1302714341128146996>"
    emote_dislike = "<:dislike:1302714320139980920>"
    emote_dev = "<:dev:1302714311998967943>"
    emote_deleted = "<:deleted:1302714304780566558>"
    emote_conversation = "<:conversation:1302714296492359780>"
    emote_Booster = "<:Booster:1302714285939621899>"
    emote_bann = "<:bann:1302714271087460402>"
    emote_attention = "<:attention:1302714264422711449>"
    emote_announcement = "<:announcement:1302714247381385316>"

if Botmodus in preview_aktiviert:
    token = "CLARAALPHA"
    Version = f"{Majorversion}.{Minorversion}.{Patchversion}"
    TextVersion = f"Version {Version} (Pre {previewversion})"
    EmbedVersion = f"Ver. {Version} (Pre {previewversion})"
    BotVersion = f"Ver. {Version} (Pre {previewversion})"
    Build = f"{Buildnummer}"
    anzahl_feedback = "---"
    anzahl_top_gg_sterne = "-,- ⭐"
    anzahl_sterne = "-,- ⭐"
    anzahl_befehle = "---"
    anzahl_eastereggs = "---"
    anzahl_witzen = "---"
    anzahl_spiele = "---"
    Sprache = Language
    Cooldown_dauer = 10
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» Der PREVIEW-MODUS ist derzeit aktiviert!\n")
    Datenbank = {
        'host': os.getenv("DBDEVHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DB1"),
        }
    ZentraleDatenbank = {
        'host': os.getenv("DBDEVHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DBHQ"),
        }
    emote_continue = "<:continue:1302717576178302996>"
    emote_back = "<:back:1302717569332936796>"
    emote_settings = "<:settings:1302717563397996594>"
    emote_slash = "<:slash:1302717556242518056>"
    emote_error = "<:error:1302717547535143083>"
    emote_done = "<:done:1302717540996218910>"
    emote_witcherhat = "<:witcherhat:1302714000467034275>"
    emote_web = "<:web:1302713992212381759>"
    emote_wartungen = "<:wartungen:1302713984855834694>"
    emote_wartung = "<:wartung:1302713977830113311>"
    emote_timeout = "<:timeout:1302713965876613200>"
    emote_time = "<:time:1302713958532255755>"
    emote_ticket = "<:ticket:1302713949854236815>"
    emote_tester = "<:tester:1302713941256048732>"
    emote_star = "<:star:1302713934469533726>"
    emote_skull = "<:skull:1302713907923783723>"
    emote_smile = "<:smile:1302714203303575654>"
    emote_snowflake = "<:snowflake:1302713927171444857>"
    emote_shopping = "<:shopping:1302713898578739200>"
    emote_shield = "<:shield:1302713891435970680>"
    emote_share = "<:share:1302713851934150728>"
    emote_searching = "<:searching:1302713844413763605>"
    emote_reboot = "<:reboot:1302713833290338377>"
    emote_question = "<:question:1302713824293421217>"
    emote_ping = "<:ping:1302713817121161216>"
    emote_newby = "<:newby:1302713809311498240>"
    emote_mod_action = "<:mod_action:1302713801161834628>"
    emote_members = "<:members:1302713790072225875>"
    emote_member = "<:member:1302713781411119145>"
    emote_mail = "<:mail:1302713771201925172>"
    emote_lolli = "<:lolli:1302713757264248874>"
    emote_like = "<:like:1302713748187910156>"
    emote_keule = "<:keule:1302713701626937376>"
    emote_idea = "<:idea:1302713695511646290>"
    emote_help = "<:help:1302713681167126608>"
    emote_heart = "<:heart:1302713672753217648>"
    emote_gift = "<:gift:1302713661252702279>"
    emote_forbidden = "<:forbidden:1302713653115490427>"
    emote_fire = "<:fire:1302713641241542656>"
    emote_event = "<:event:1302713632316194896>"
    emote_dislike = "<:dislike:1302713624367726622>"
    emote_dev = "<:dev:1302713615677128714>"
    emote_deleted = "<:deleted:1302713596589113475>"
    emote_conversation = "<:conversation:1302713588917604352>"
    emote_Booster = "<:Booster:1302713578914054175>"
    emote_bann = "<:bann:1302713565731491870>"
    emote_attention = "<:attention:1302713557602795620>"
    emote_announcement = "<:announcement:1302713548631310377>"

if Botmodus in Beta_deaktiviert:
    token = "CLARA"
    Version = f"{Majorversion}.{Minorversion}.{Patchversion}"
    TextVersion = f"Version {Version}"
    EmbedVersion = f"Version {Version}"
    BotVersion = f"Version {Version}"
    Build = f"{Buildnummer}"
    anzahl_feedback = "---"
    anzahl_top_gg_sterne = "---"
    anzahl_sterne = "---"
    anzahl_befehle = Befehle
    anzahl_spiele = Spiele
    anzahl_eastereggs = Eastereggs
    anzahl_witzen = Witzen
    Sprache = Language
    Cooldown_dauer = 120
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» Der BETA-MODUS ist deaktiviert!\n")
    ZentraleDatenbank = {
        'host': os.getenv("DBHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DBHQ"),
        }
    Datenbank = {
        'host': os.getenv("DBHOST"),
        'port': int(os.getenv("DBPORT")),
        'user': os.getenv("DBUSER"),
        'password': os.getenv("DBPASSWD"),
        'db': os.getenv("DB0"),
        }
    emoji_continue = "<:continue:1302717504342458540>"
    emoji_back = "<:back:1302717497736429660>"
    emoji_settings = "<:settings:1302717489276256286>"
    emoji_slash = "<:slash:1302717482884137041>"
    emoji_error = "<:error:1302717474827141231>"
    emoji_done = "<:done:1302717468166455337>"
    emoji_witcherhat = "<:witcherhat:1302713462962651197>"
    emoji_web = "<:web:1302713437918597230>"
    emoji_wartungen = "<:wartungen:1302713426233131189>"
    emote_wartung = "<:wartung:1302713416741556266>"
    emote_timeout = "<:timeout:1302713408063279274>"
    emote_time = "<:time:1302713399305699329>"
    emote_ticket = "<:ticket:1302713383094845585>"
    emote_tester = "<:tester:1302713374647390308>"
    emote_star = "<:star:1302713365314932797>"
    emote_skull = "<:skull:1302713333966831719>"
    emote_smile = "<:smile:1302713342351114250>"
    emote_snowflake = "<:snowflake:1302713351314604204>"
    emote_shopping = "<:shopping:1302713313003573288>"
    emote_shield = "<:shield:1302713304069836881>"
    emote_share = "<:share:1302713294876049460>"
    emote_searching = "<:searching:1302713284671045672>"
    emote_reboot = "<:reboot:1302713276127510558>"
    emote_question = "<:question:1302713268649070603>"
    emote_ping = "<:ping:1302713256703561858>"
    emote_newby = "<:newby:1302713255172767784>"
    emote_mod_action = "<:mod_action:1302713241436164168>"
    emote_members = "<:members:1302713233328574634>"
    emote_member = "<:member:1302713226307309669>"
    emote_mail = "<:mail:1302713214223515751>"
    emote_lolli = "<:lolli:1302713208209149992>"
    emote_like = "<:like:1302713200176791634>"
    emote_keule = "<:keule:1302713185446662156>"
    emote_idea = "<:idea:1302713176483303536>"
    emote_help = "<:help:1302713167754952844>"
    emote_heart = "<:heart:1302713159391514775>"
    emote_gift = "<:gift:1302713151216943104>"
    emote_forbidden = "<:forbidden:1302713141637025823>"
    emote_fire = "<:fire:1302713133642547240>"
    emote_event = "<:event:1302713124801085552>"
    emote_dislike = "<:dislike:1302713117477830718>"
    emote_dev = "<:dev:1302713109441417247>"
    emote_deleted = "<:deleted:1302713101736607775>"
    emote_conversation = "<:conversation:1302713074217648178>"
    emote_Booster = "<:Booster:1302713065686437999>"
    emote_bann = "<:attention:1302713051312558173>"
    emote_attention = "<:attention:1302713051312558173>"
    emote_announcement = "<:announcement:1302713041242034358>"



if Botmodus in KeinModus:
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» Der Modus {Botmodus} wurde gewählt.\n")
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | FEHLER\n» KEIN TOKEN GEFUNDEN!\n")
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | Clara\n» what the fu--??\n")
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | Clara\n» Kann es sein, dass du dumm bist oder sowas??\n")
    print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» Start wird abgebrochen...\n\n\n\n\n\n\n\n\n")
    exit()

# LOGIKBLOCK - ENDE!
##################################################################################################################
print(f"{datetime.datetime.now().strftime(konsole_date_format)} | SYSTEM\n» claralara_config.py wurde erfolgreich geladen.\n")























