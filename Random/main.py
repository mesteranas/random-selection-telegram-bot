import random
import message,app
import telegram
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import CommandHandler,MessageHandler,filters,ApplicationBuilder
names=[]
stip=0
counts=0

with open("token.bot","r",encoding="utf-8") as file:
    bot=ApplicationBuilder().token(file.read()).build()
async def start(update,contextt):
    info=update.effective_user
    await message.Sendmessage(chat_id=info.id,text="welcome " + str(info.first_name) + "to this bot. This bot allows you to choose names. Please send me the names Divided by commas, and I'll choose random 1 or many.")
async def helb(update,contextt):
    links="""<a href="https://t.me/mesteranasm">telegram</a>

<a href="https://t.me/tprogrammers">telegram channel</a>

<a href="https://x.com/mesteranasm">x</a>

<a href="https://Github.com/mesteranas">Github</a>

email:
anasformohammed@gmail.com

<a href="https://Github.com/mesteranas/random-selection-telegram-bot">visite project on Github</a>
"""
    info=update.effective_user
    await message.Sendmessage(info.id,"""name: {}\nversion: {}\ndescription: {}\n developer: {}\n contect us {}""".format(app.name,str(app.version),app.description,app.developer,links))
print("running")
async def rand(update,contextt):
    global names,stip,counts
    info=update.effective_user
    if stip==0:
        await message.Sendmessage(info.id,"OK now send the names count")
        stip=1
        names=update.message.text.split(",")
    elif stip==1:
        stip=0
        try:
            counts=int(update.message.text)
            re=random.sample(names,counts)
            await message.Sendmessage(info.id,"result=" + ",".join(re))
        except Exception as e:
            await message.Sendmessage(info.id,"error " + str(e))

bot.add_handler(CommandHandler("start",start))
bot.add_handler(CommandHandler("help",helb))
bot.add_handler(MessageHandler(filters.TEXT,rand))
bot.run_polling()