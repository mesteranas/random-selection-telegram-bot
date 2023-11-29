import random
import telepot
from telepot.loop import MessageLoop
names=[]
stip=0
counts=0
def message(msg):
    global names,stip,counts
    content_type,chat_type,chat_id=telepot.glance(msg)
    if content_type == 'text':
        if msg["text"]=="/start":
            bot.sendMessage(chat_id, f"Welcome {msg['from']['first_name']} to this bot. This bot allows you to choose names. Please send me the names Divided by commas, and I'll choose random 1 or many.")
        else:
            if stip==0:
                bot.sendMessage(chat_id,"OK now send the names count")
                stip=1
                names=msg["text"].split(",")
            elif stip==1:
                stip=0
                try:
                    counts=int(msg["text"])
                    re=random.sample(names,counts)
                    bot.sendMessage(chat_id,"result=" + ",".join(re))
                except Exception as e:
                    bot.sendMessage(chat_id,"error " + str(e))
    else:
        bot.sendMessage(chat_id,"please send text messages only")

bot=telepot.Bot("")
bot.deleteWebhook()
MessageLoop(bot,{"chat":message}).run_as_thread()
print("runing")
while True:
    pass