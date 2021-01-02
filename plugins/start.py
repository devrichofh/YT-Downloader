from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel Update", url="https://t.me/devrichoproject")],
        [InlineKeyboardButton(
            "Lapor Bug 😊", url="https://t.me/devrichofh")]
    
    ])
    welcomed = f"Halooo <b>{message.from_user.first_name}</b>\nketik /help untuk melihat cara penggunaan\nDibuat oleh @devrichofh"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
