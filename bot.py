from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 22811974
API_HASH = "13ae06fd677982c1c28a1a73924230cc"
BOT_TOKEN = "8028994012:AAFxsjjgOULkX57XdnutnqCRo9ktYR-R0Mc"

bot = Client("music-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply_text("🎵 سلام! من Blue Music Bot هستم. دستور /play رو بفرست تا آهنگ پخش کنم.")

@bot.on_message(filters.command("play"))
async def play(client, message: Message):
    await message.reply_text("🎧 ویژگی پخش آهنگ به‌زودی فعال می‌شود...")

bot.run()
