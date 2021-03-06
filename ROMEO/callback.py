from CFC.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)







@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\nĀ» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("š” only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"āļø **settings of** {query.message.chat.title}\n\nāø : pause stream\nā¶ļø : resume stream\nš : mute userbot\nš : unmute userbot\nā¹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("ā¢", callback_data="cbstop"),
                      InlineKeyboardButton("II", callback_data="cbpause"),
                      InlineKeyboardButton("ā£ā£", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("š", callback_data="cbmute"),
                      InlineKeyboardButton("š", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("š« Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("ā nothing is currently streaming", show_alert=True)
        
        
#start



@Client.on_callback_query(filters.regex("cb_start"))
async def cb_start(_, query: CallbackQuery):
    await query.edit_message_text(
       f"""Hello[,](https://telegra.ph/file/f82c6c960be3f8471fb0a.jpg) **Welcome** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})**\n
 I am powerful easy to use TeleGram Super Bot. I can play high quality and unbreakable music Ć video in your group voice chat. Just add me and promote with needed powers.

Use Inline buttons for more !!
For Help : @StrayCoderSupport""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ā Add me in your Group",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(
                    "āCommands", callback_data="cb_cmd"),],
                [
                    InlineKeyboardButton("š¤ Bot Owner", url=f"https://t.me/{OWNER_NAME}"),
                    InlineKeyboardButton("šØāš» Developer", url=f"https://t.me/ABOUT_DADDY"),
                ],
                [
                    InlineKeyboardButton(
                        "šØ Support", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "šØ Updates", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "ā Source Code", url="https://github.com/TheStrayCoder/MusicVideo-Stream"
                    )
                ],
            ]
        ),
    )

    
    
    
    #Help command
    
    
@Client.on_callback_query(filters.regex("cb_cmd"))
async def cb_cmd(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Heyy** [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Check out the menu below to read the module information & see the list of available Commands !!

Developed By : @Its_romeoo""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Basicāļø", callback_data="cb_basic"),
                    InlineKeyboardButton("Advance š¹", callback_data="cb_advance"),
                ],
               
                [InlineKeyboardButton("ā¬ļø Back", callback_data="cb_start")],
            ]
        ),
    )
    
@Client.on_callback_query(filters.regex("cb_basic"))
async def cb_basic(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""š¤ Normal Bot Commands :-

Ā» /play - (song name) 
Ā» /vplay - play video 
Ā» /vstream - link or name
Ā» /skip - Skip the Song
Ā» /end - Stop Playing Music
Ā» /pause - Pause the track
Ā» /resume - Resumes the Track
Ā» /mute - Mute the Assistant 
Ā» /search - (song name)
Ā» /song - Download Song File
Ā» /lyrics - Get Lyrics of the Song

š Powered By : @StrayCoder""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ā¬ļø Back", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_advance"))
async def cb_advance(_, query: CallbackQuery):
    await query.edit_message_text(    
      f"""ā Some Extra Commands :-

Ā» /ping - Shows the Ping Status
Ā» /alive - Shows the Alive Status
Ā» /start - Starts the Bot
Ā» /id - Get the ID
Ā» /repo - Get the source code 
Ā» /rmd - Clean all the downloads
Ā» /clean - Clean the Storage
Ā» /gcast - broadcast your message

š Powered By : @StrayCoder""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ā¬ļø Back", callback_data="cb_cmd")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cb_fun"))
async def cb_fun(_, query: CallbackQuery):
    await query.edit_message_text(  
        f"""ššŖš£ š¾š¤š¢š¢šš£ššØ
ā¢ `/lawda` 
ā¢ `/lassan`  
ā¢ `/randi`    
ā¢ `/lund`   
ā¢ `/chut`    
ā”""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ā¬ļø Back", callback_data="cb_cmd")]]
        ),
    )
        

    
    
    
        


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Sorry !! You are not a admin in this Group.", show_alert=True)
    await query.message.delete()
