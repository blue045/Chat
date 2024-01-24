from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
ᴛʜᴇsᴇ ᴀʀᴇ sᴏᴍᴇ ᴀɪ ᴄᴏᴍᴍᴀɴᴅs

 ➻ /mahadev : ɢᴇɴᴇʀᴀᴛᴇ Mᴀʜᴀᴅᴇᴠ ɪᴍᴀɢᴇ
 ➻ /fakegen : ɢᴇɴᴇʀᴀᴛᴇs ғᴀᴋᴇ Iɴғᴏʀᴍᴀᴛɪᴏɴ
 ➻ /picgen : ɢᴇɴᴇʀᴀᴛᴇ ᴀ ғᴀᴋᴇ ᴘɪᴄ
 ➻ /eval : ᴛᴏ ᴇᴠᴀʟᴜᴀᴛᴇ sɪᴍᴘʟᴇ ᴄᴏᴅᴇ
 ➻ /ask : ʀᴇᴘʟʏ ᴛo ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ
 ➻ /draw : ᴄʀᴇᴀᴛᴇ ɪᴍᴀɢᴇs
 ➻ /upscale : ᴜᴘsᴄᴀʟᴇ ʏᴏᴜʀ ɪᴍᴀɢᴇs
 ➻ /gpt : ᴄʜᴀᴛɢᴘᴛ
 ➻ /bard : ʙᴀʀᴅ ᴀɪ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /mistral : ᴍɪsᴛʀᴀʟ ᴀɪ
 ➻ /llama : ʟʟᴀᴍᴀ ʙʏ ᴍᴇᴛᴀ ᴀɪ
 ➻ /palm : ᴘᴀʟᴍ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /reverse : ʀᴇᴠᴇʀsᴇ ɪᴍᴀɢᴇ sᴇᴀʀᴄʜ
 ➻ /gemini : ɢᴇᴍɪɴɪ ʙʏ ɢᴏᴏɢʟᴇ
 ➻ /imagine : ᴄʀᴇᴀᴛᴇ ᴀɪ ɪᴍᴀɢᴇs
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="ᴊᴏɪɴ ᴍy ᴜᴩᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ",url="https://codeflix_bots")
                ]
            ]
        )
    )
