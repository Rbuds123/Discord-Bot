import discord
from discord.ext import commands
import os
import tracemalloc
from config import BOT_TOKEN

tracemalloc.start()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            try:
                bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Successfully loaded {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    await load_extensions()  # Await loading of extensions here

# Add error handling for commands
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Missing required argument.')
    else:
        await ctx.send('An error occurred.')
        raise error

# Define a simple command
@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(BOT_TOKEN)
