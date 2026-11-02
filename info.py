import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ' '))
API_HASH = environ.get('API_HASH', ' ')
BOT_TOKEN = environ.get('BOT_TOKEN',  ')

DATABASE_URI = environ.get('DATABASE_URI', " ")
DATABASE_NAME = environ.get('DATABASE_NAME', " ")
COLLECTION_NAME = environ.get('COLLECTION_NAME', ' ')

CAPTION_INDEX_CHANNEL = int(environ.get('CAPTION_INDEX_CHANNEL', ' '))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', ' ').split()] + [CAPTION_INDEX_CHANNEL]

PICS = environ.get("PICS", "https://te.legra.ph/file/d6a23f16e002e86381656.jpg")
FORCE = " "
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', ' ').split()]


auth_channel = environ.get('AUTH_CHANNEL', ' ')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

SHORT1_URL = environ.get('SHORT1_URL', ' ')
SHORT1_API = environ.get('SHORT1_API', ' ')
SHORT2_URL = environ.get('SHORT2_URL', ' ')
SHORT2_API = environ.get('SHORT2_API', ' ')
IS_SHORTLINK = is_enabled(environ.get("IS_SHORTLINK", "True"), True)
PORT = environ.get("PORT", "8080")
CHNL_LNK = environ.get('CHNL_LNK', 'HEROFLiX')
TUTORIAL = environ.get('TUTORIAL', ' ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ' '))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'herofeedbot')
 

# ==================== BOT TEXT ====================
START_TXT = """<b>🌀 Unlimited Movies, Series, Anime
🔆 New Releases Upload Every Day
♻️ 24 x 7 Service 📆 Daily Updates</b>"""

STATUS_TXT = """<b>★ Tᴏᴛᴀʟ Fɪʟᴇs: <code>{}</code>
★ Tᴏᴛᴀʟ Usᴇʀs: <code>{}</code>
★ Tᴏᴛᴀʟ Cʜᴀᴛs: <code>{}</code>
★ Usᴇᴅ Sᴛᴏʀᴀɢᴇ: <code>{}</code>
★ Fʀᴇᴇ Sᴛᴏʀᴀɢᴇ: <code>{}</code></b>"""

LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Nᴀᴍᴇ - {}"""



NO_RESULTS = """💢 No Results For Your Search❗️"""

CAPTION = '<a href="https://telegram.me/HeroFlix"><b>{file_name}</b></a>'

RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code></b>"""

LOGO = '🔆彡[ HEROFLiX ]彡🔆'

 
 
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
 
 
