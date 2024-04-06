from discord.ext import commands
import discord

from db import DB

import time
import random

db = DB()
table = db.db

BOT_TOKEN = "BOT TOKEN"
CHANNEL_ID = "CHANNEL ID AS INT"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Bot is Ready!")
  channel = bot.get_channel(CHANNEL_ID)
  await channel.send("Hello! I am the Currency Bot!")
  await channel.send("I keep track of your money!")
  await channel.send("Type '!curhelp' for a list of commands")



@bot.command()
async def curhelp(ctx):
  await ctx.send("Commands:")
  await ctx.send("!register - Register for the Currency Bot")
  await ctx.send("!balance - Check your balance")
  await ctx.send("!job <job> - Work as a Fisher, Miner, Farmer, or Trader")
  await ctx.send("!quit - Quit your job")
  await ctx.send("!myjob - Check your job")
  await ctx.send("!work - Work as your job")
  await ctx.send("!curhelp - Get help")


@bot.command()
async def register(ctx):
  if ctx.author.id in table:
    await ctx.send("You are already registered!")
  else:
    boolean = db.__setitem__(str(ctx.author.id), {"money": 25, "job": None, "pay": 0})
    if boolean:
      await ctx.send("You are now registered!")
      db.__save__()


@bot.command()
async def balance(ctx):
  if str(ctx.author.id) not in table:
    await ctx.send("You are not registered!")
  else:
    await ctx.send(f"You have ${table[str(ctx.author.id)]["money"]}!")
    db.__save__()


@bot.command()
async def job(ctx, job):
  if str(ctx.author.id) not in table:
    await ctx.send("You are not registered!")
  elif table[str(ctx.author.id)]["job"] != None:
    await ctx.send("You already have a job!")
  else:
    if job.lower() == "fisher":
      table[str(ctx.author.id)]["job"] = "Fisher"
      table[str(ctx.author.id)]["pay"] = random.randint(8, 12)
      await ctx.send("You have chosen to be a Fisher!")
      await ctx.send(f"You will get paid ${table[str(ctx.author.id)]['pay']} per work day!")
    elif job.lower() == "miner":
      table[str(ctx.author.id)]["job"] = "Miner"
      table[str(ctx.author.id)]["pay"] = random.randint(10, 14)
      await ctx.send("You have chosen to be a Miner!")
      await ctx.send(f"You will get paid ${table[str(ctx.author.id)]['pay']} per work day!")
    elif job.lower() == "farmer":
      table[str(ctx.author.id)]["job"] = "Farmer"
      table[str(ctx.author.id)]["pay"] = random.randint(12, 16)
      await ctx.send("You have chosen to be a Farmer!")
      await ctx.send(f"You will get paid ${table[str(ctx.author.id)]['pay']} per work day!")
    elif job.lower() == "trader":
      table[str(ctx.author.id)]["job"] = "Trader"
      table[str(ctx.author.id)]["pay"] = random.randint(14, 18)
      await ctx.send("You have chosen to be a Trader!")
      await ctx.send(f"You will get paid ${table[str(ctx.author.id)]['pay']} per work day!")
    elif job.lower() == "banker":
      table[str(ctx.author.id)]["job"] = "Banker"
      table[str(ctx.author.id)]["pay"] = random.randint(16, 20)
      await ctx.send("You have chosen to be a Banker!")
      await ctx.send(f"You will get paid ${table[str(ctx.author.id)]['pay']} per work day!")
    else:
      await ctx.send("Invalid Input!")
      await ctx.send("Job options are:")
      await ctx.send("Fisher")
      await ctx.send("Miner")
      await ctx.send("Farmer")
      await ctx.send("Trader")
      await ctx.send("Banker")

    db.__save__()


@bot.command()
async def quit(ctx):
  if str(ctx.author.id) not in table:
    await ctx.send("You are not registered!")
  elif table[str(ctx.author.id)]["job"] == None:
    await ctx.send("You are not working!")
  else:
    table[str(ctx.author.id)]["job"] = None
    table[str(ctx.author.id)]["pay"] = 0
    await ctx.send("You have quit your job!")
    db.__save__()


@bot.command()
async def myjob(ctx):
  if str(ctx.author.id) not in table:
    await ctx.send("You are not registered!")
  elif table[str(ctx.author.id)]["job"] == None:
    await ctx.send("You are not working!")
  else:
    await ctx.send(f"Your Job is {table[str(ctx.author.id)]['job']}")
    db.__save__()


@bot.command()
async def work(ctx):
  if str(ctx.author.id) not in table:
    await ctx.send("You are not registered!")
  elif table[str(ctx.author.id)]["job"] == None:
    await ctx.send("You are not working!")
  else:
    if table[str(ctx.author.id)]["job"] == "Fisher":
      await ctx.send("You have worked as a Fisher!")
      table[str(ctx.author.id)]["money"] += table[str(ctx.author.id)]["pay"]
      db.__save__()
    elif table[str(ctx.author.id)]["job"] == "Miner":
      await ctx.send("You have worked as a Miner!")
      table[str(ctx.author.id)]["money"] += table[str(ctx.author.id)]["pay"]
      db.__save__()
    elif table[str(ctx.author.id)]["job"] == "Farmer":
      await ctx.send("You have worked as a Farmer!")
      table[str(ctx.author.id)]["money"] += table[str(ctx.author.id)]["pay"]
      db.__save__()
    elif table[str(ctx.author.id)]["job"] == "Trader":
      await ctx.send("You have worked as a Trader!")
      table[str(ctx.author.id)]["money"] += table[str(ctx.author.id)]["pay"]
      db.__save__()
    elif table[str(ctx.author.id)]["job"] == "Banker":
      await ctx.send("You have worked as a Banker!")
      table[str(ctx.author.id)]["money"] += table[str(ctx.author.id)]["pay"]
      db.__save__()


bot.run(BOT_TOKEN)
