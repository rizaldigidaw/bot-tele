import telebot
from telebot import types,util
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot('5675916411:AAHUpune1WGyJqdCEePo_GVlgHe0NxygURA')

@bot.message_handler()
async def msg(message):
    text = message.text.lower()
    await bot.reply_to(message,text)
bot.add_custom_filter(telebot.asyncio_filters.TextStartsFilter())
import asyncio
asyncio.run(bot.polling(allowed_updates=util.update_types))
