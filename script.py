class Script(object):
    START_TXT = """<b>Hello {},
I A Telegram Auto Filter Bot.Its Easy To Use Me ):\nJust Add Me To Your Group As Admin,Hit The Help Button For More Info</b>"""
    HELP_TXT = """<b>Hey {}
Here Is The Help For My Commands.</b>"""
    ABOUT_TXT = """
<b>➥  My Name</b> : <b><i><a href="https://t.me/MC_MovieBot">Mᴏᴠɪᴇ Bᴏᴛ 😎</a></i></b>
<b>➥  Owner</b> : <b><i><a href="https://t.me/NickxFury">Nɪᴄᴋ Fᴜʀʏ 🇮🇳</a></i></b>
<b>➥ Credits</b> : <code>Everyone in this journey</code>
<b>➥ Data base</b> : <b><a href="https://www.mongodb.com/">MongoDB</a></b>
<b>➥ Language</b> : <code>Python3</code>
<b>➥ Library</b> : <i><a href="https://docs.pyrogram.org">Pyrogram Asyncio 1.13.0 </a></i>
<b>➥ Server</b> : <code>AWS</code>
<b>➥ Build Stats</b> : <code>V6.0 [BETA]</code>
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ  <a href=https://t.me/MOVIECLUB_CHAT>Mᴏᴠɪᴇ Cʟᴜʙ</a>"""
    SOURCE_TXT = """
<code>All the files in this bot are freely available on the internet or posted by somebody else.This bot is indexing files which are already uploaded on Telegram for easy of searching, We respect all the copyright laws and works in compliance with DMCA and EUCD. If anything is against law please contact us so that it can be removed asap.</code>"""

    MANUALFILTER_TXT = """Help: <b>Filter
- Filter is the feature were users can set automated replies for a particular keyword and the bot will respond whenever a keyword is found the message
NOTE:
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
Commands and Usage:
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code></b>"""
    BUTTON_TXT = """Help: <b>Buttons
- <a href=https://t.me/MC_MovieBot>This Bot</a> Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
URL buttons:
<code>[Button Text](buttonurl:https://t.me/MOVIECLUB_CHAT)</code>
Alert buttons:
<code>[Button Text](buttonalert:This is an alert message)</code></b>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter
NOTE:
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db.</b>"""

    CONNECTION_TXT = """Help: <b>Connections
- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.
NOTE:
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
Commands and Usage:
• /connect  - connect a particular chat to your PM.
• /disconnect  - disconnect from a chat.
• /connections - list all your connections.</b>"""

    AUTO_MANUAL_TXT = """Help: <b>Filters

Select A Filters Fype Below:</b>"""


    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
• /paste [text] - paste the given text on Pasty
• /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    INFO_TXT = """<b>𝖧𝖾𝗅𝗉: 🐶 𝖲𝗁𝗈𝗐 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 
𝖭𝖮𝖳𝖤: 𝗍𝗁𝖾𝗌𝖾 𝖺𝗋𝖾 𝗍𝗁𝖾 𝖾𝗑𝗍𝗋𝖺 𝖿𝖾𝖺𝗍𝗎𝗋𝖾𝗌 𝗈𝖿 Me 
Commands and Usage:
• /id - <code>get id of a specifed user.</code>
• /info or /whois - <code>get information about a user.</code>
•/imdb or /search - <code>get the film information from various sources.</code>
• /paste [text] - <code>paste the given text on Pasty.</code>
• /paste [reply] - <code>paste the replied text on Pasty.</code>
• /genpassword or /genpw <code>20</code>
• /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph."""


    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
• /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• Bot can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.

<b>NOTE:</b>
• IMDb should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
• /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on group.
• These commands can be used by Only admin."""

    RESTRIC_TXT = """<b>𝖡𝖺𝗇𝗌:  
𝖲𝗈𝗆𝖾 𝗉𝖾𝗈𝗉𝗅𝖾 𝗇𝖾𝖾𝖽 𝗍𝗈 𝖻𝖾 𝗉𝗎𝖻𝗅𝗂𝖼𝗅𝗒 𝖻𝖺𝗇𝗇𝖾𝖽; 𝗌𝗉𝖺𝗆𝗆𝖾𝗋𝗌, 𝖺𝗇𝗇𝗈𝗒𝖺𝗇𝖼𝖾𝗌, 𝗈𝗋 𝗃𝗎𝗌𝗍 𝗍𝗋𝗈𝗅𝗅𝗌.  
𝖳𝗁𝗂𝗌 𝗆𝗈𝖽𝗎𝗅𝖾 𝖺𝗅𝗅𝗈𝗐𝗌 𝗒𝗈𝗎 𝗍𝗈 𝖽𝗈 𝗍𝗁𝖺𝗍 𝖾𝖺𝗌𝗂𝗅𝗒, 𝖻𝗒 𝖾𝗑𝗉𝗈𝗌𝗂𝗇𝗀 𝗌𝗈𝗆𝖾 𝖼𝗈𝗆𝗆𝗈𝗇 𝖺𝖼𝗍𝗂𝗈𝗇𝗌, 𝗌𝗈 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾 𝗐𝗂𝗅𝗅 𝗌𝖾𝖾!   
𝖠𝖽𝗆𝗂𝗇 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌: 
- /ban: 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋. 
- /tban: 𝖳𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾 𝗍𝗂𝗆𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝟦𝗆 = 𝟦 𝗆𝗂𝗇𝗎𝗍𝖾𝗌, 𝟥𝗁 = 𝟥 𝗁𝗈𝗎𝗋𝗌, 𝟨𝖽 = 𝟨 𝖽𝖺𝗒𝗌, 𝟧𝗐 = 𝟧 𝗐𝖾𝖾𝗄𝗌. 
- /unban: 𝖴𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.  
𝖤𝗑𝖺𝗆𝗉𝗅𝖾𝗌:
 - 𝖡𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗈𝗋 𝗍𝗐𝗈 𝗁𝗈𝗎𝗋𝗌. 
-> /tban @𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 𝟤𝗁</b>"""

    JSON_TXT ="""<b>Help JSON:
𝖡𝗈𝗍 𝗋𝖾𝗍𝗎𝗋𝗇𝗌 𝗃𝗌𝗈𝗇 𝖿𝗈𝗋 𝖺𝗅𝗅 𝗋𝖾𝗉𝗅𝗂𝖾𝖽 𝗆𝖾𝗌𝗌𝖺𝗀𝖾𝗌 𝗐𝗂𝗍𝗁 /json. 
𝖥𝖾𝖺𝗍𝗎𝗋𝖾𝗌:
𝖬𝖾𝗌𝗌𝖺𝗀𝖾 𝖤𝖽𝗂𝗍𝗍𝗂𝗇𝗀 JSON
𝖯𝗆 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 
𝖦𝗋𝗈𝗎𝗉 𝖲𝗎𝗉𝗉𝗈𝗋𝗍
/Json 𝖠𝗅𝗍𝖾𝗋𝗇𝖺𝗍𝗂𝗏𝖾𝗌:
/js or /showjson or /json</b>"""
    PIN_MESSAGE_TXT = """Help: <b>Pin Message</b>

All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!

<b>Commands and Usage:</b>
• /pin: Pin the message you replied to. Add 'loud' or 'notify' to send a notification to group members.
• /unpin: Unpin the current pinned message. If used as a reply, unpins the replied to message.

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works only group.
• These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - to get the rescent errors.
• /stats - to get status of files in db.
• /delete - to delete a specific file from db.
• /users - to get list of my users and ids.
• /chats - to get list of the my chats and ids.
• /leave - to leave from a chat.
• /disable - do disable a chat.
• /ban_users - to ban a user.
• /unban_users - to unban a user.
• /channel - to get list of total connected channels.
• /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>• Saved Files:</b> <code>{}</code>
<b>• Users:</b> <code>{}</code>
<b>• Groups:</b> <code>{}</code>
<b>• DB Usage:</b> <code>{}</code> MiB"""

    FORCESUB_TXT = """**♦️ READ THIS INSTRUCTION ♦️**

__🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately 🙈__

**👇 JOIN THIS CHANNEL & TRY AGAIN 👇**"""

    MEMES_TXT = """Help: <b>Fun</b>

<b>Commands and Usage:</b>

• /throw or /dart - t𝗈 m𝖺𝗄𝖾 drat 
• /roll or /dice - roll the dice 
• /goal or /shoot - to make a goal or shoot
• /luck or /cownd - Spin the Lucky
• /runs strings

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    URL_SHORTNER_TXT = """Help: <b>URL Shortner</b>

Some URLs is Shortner

<b>Commands and Usage:</b>
• /short <code>(link)</code> - I will send the shorted links.

<b>Example:</b>
<code>/short https://t.me/josprojects</code>

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    TTS_TXT = """Help: <b>Text to Speech</b>

A module to convert text to voice with language support.

<b>Commands and Usage:</b>
• /tts - Reply to any text message with language code to convert as audio.

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    MUSIC_TXT = """Help: <b>Music</b>

Music download modules, for those who love music.

<b>Commands and Usage:</b>
• /song or /mp3 (songname) - download song from yt servers.
• /video or /mp4 (songname) - download video from yt servers.

<b>YouTube Thumbnail Download</b>
• /ytthumb (youtube link)
<b>Example:</b> <code>/ytthumb https://youtu.be/h6PtzFYaMxQ</code>

<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    PASSWORD_GEN_TXT = """Help: <b>Password Generator</b>

There Is Nothing To Know More. Send Me The Limit Of Your Password.
- I Will Give The Password Of That Limit.

<b>Commands and Usage:</b>
• /genpassword or /genpw <code>20</code>

<b>NOTE:</b>
• Only Digits Are Allowed
• Maximum Allowed Digits Till 84 
(I Can't Generate Passwords Above The Length 84)
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """❗You have to be the group creator to do that."""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """🚮 Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """❗I am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
