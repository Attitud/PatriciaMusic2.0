
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
import os
import sys


HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nā¢ Iam A Bot Project by @TGBOTZXD\nā¢ I Can Manage Group VC's\n\nā¢ Hit /help to know about available commands.</b>"
HELP = """
š§ <b>I Can Play Musics On VoiceChats š¤Ŗ</b>

š¶ **Common Commands**:
ā¢ `/song` __Download Song from youtube__
ā¢ `/play`  __Play song you requested__
ā¢ `/help` __Show help for commands__
ā¢ `/dplay` __Play song you requested via deezer__
ā¢ `splay` __Play song you requested via jio saavn__
ā¢ `/ytplay` __Play song directly from youtube server__
ā¢ `/search` __Search video songs links__
ā¢ `/current` __Show now playing__
ā¢ `/playlist` __Show now playing list__
ā¢ `/video` __Downloads video song quickly__
š¶ **Admin Commands**:
ā¢ `/player`  __Open music player settings panel__
ā¢ `/pause` __Pause song play__
ā¢ `/skip` __Skip next song__
ā¢ `/resume`  __Resume song play__
ā¢ `/userbotjoin`  __Invites assistant to your chat__
ā¢ `/end` __Stops music play__
ā¢ `/admincache` __Refresh list of admins with vc power__
Ā© Powered By 
[ __@tgbotsXD || @tgbotzXD__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
       [
                InlineKeyboardButton('š¢ Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('š¬ Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('š¤ Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('š§ Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('š Source Code š', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('š¢ Updates', url='https://t.me/TGBOTZXD'),
                InlineKeyboardButton('š¬ Support', url='https://t.me/TGBOTSXD')
                ],[
                InlineKeyboardButton('š¤ Developer', url='https://t.me/piroXpower'),
                InlineKeyboardButton('š§ Chats', url='https://t.me/frndsXworld')
                ],[
                InlineKeyboardButton('š Source Code š', url='https://github.com/TEAM-PATRICIA/PatriciaMusic2.0'),
       ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo="https://telegra.ph/file/33cc1aeaf934f19943bdc.jpg", caption=HELP, reply_markup=reply_markup)
    await message.delete()
