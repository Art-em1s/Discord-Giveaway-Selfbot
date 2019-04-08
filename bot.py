"""
    Copyright (c) Artemis
"""
import discord, datetime, random, time, logging, asyncio, sys
from discord.ext import commands
bot = commands.Bot(command_prefix='>', self_bot=True)
logging.basicConfig(filename='/home/bot/selfbots/client/logs/orthia-{}-bot.log'.format(int(time.time())), level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#
#
#

#Variables for easy bot changes

replies = ["this is a generic reply", "another generic reply"]
#input the replies to choose from here, one will randomly chosen

min_wait = 3
#minimum time to wait to reply, in seconds

max_wait = 5
#maxiumum time to wait to reply, in seconds

send_writing_min = 1
send_writing_max = 5
#upper and lower limits to send to chat that the client is typing a message

server_id = "564607959187849227"
#server ID to check

reaction_giveaway_bot = "312557888486899713"
#id for the bot to react to (https://cdn.discordapp.com/attachments/564502488938709002/564555862153363486/unknown.png)

reply_giveaway_bot = "312557888486899713"
#id for the bot to reply to (https://cdn.discordapp.com/attachments/564502488938709002/564504179171917839/unknown.png)

#
#
#

@bot.event
async def on_ready():
    print("Bot started at {}".format(datetime.datetime.now()))
    
@bot.event
async def on_message(message):
    if message.server.id == server_id:
        if message.author.id == reaction_giveaway_bot:
            if message.embeds and not message.content:
                if emb_author == "Jackpot" and "rs3 in the next 60 seconds!" in emb_description.lower():
                    await add_reaction(message)
        
        if message.author.id == reply_giveaway_bot:
            if message.embeds and not message.content:
                embed = message.embeds[0]
                emb_author = embed['author']['name']
                emb_description = embed['description']
                if emb_author == "Jackpot" and "rs3 in the next 60 seconds!" in emb_description.lower():
                    await write_reply(message)
                    
async def add_reaction(message):
    random_delay = random.uniform(min_wait, max_wait)
    await asyncio.sleep(random_delay)
    await self.bot.add_reaction(message, "🎉")

async def write_reply(message):
    random_delay = random.uniform(min_wait, max_wait)
    random_typing_delay = random.uniform(send_writing_min, send_writing_max)
    random_msg = random.choice(replies)
    
    await asyncio.sleep(random_delay)
    await self.bot.send_typing(message.channel)
    await asyncio.sleep(random_typing_delay)
    await self.bot.send_message(message.channel, random_msg)
    
if __name__ == '__main__':
    bot.run(sys.argv[1], bot=False)