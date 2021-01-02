from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Untuk saat ini hanya Support link single (Bukan Playlist) silahkan kirim url YouTube"
    await message.reply_text(helptxt)
