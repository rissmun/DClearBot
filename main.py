import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def clear(ctx, amount: int = None):
    if amount is None:
        await ctx.channel.purge(limit=None)
        await ctx.send('Успешно очищен весь канал.', delete_after=2)
    elif amount > 0:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Успешно очищено {amount} сообщений.', delete_after=2)
    else:
        await ctx.send('Укажите положительное целое число для количества сообщений которые необходимо очистить.', delete_after=2)

bot.run('token')
