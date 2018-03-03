import discord
from discord.ext.commands import Bot

client = Bot(description="Allows users to add their own roles.", command_prefix="!", pm_help=False)

TOKEN = ''
SELFROLES_IDS = []


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(no_pm=True, pass_context=True)
async def selfrole(ctx, role: discord.Role):
    user = ctx.message.author
    for serverrole in ctx.message.server.roles:
        if serverrole.name == role.name:
            if role.id in SELFROLES_IDS:
                try:
                    await client.add_roles(user, role)
                    await client.say("You now have the " + role.name + " role.")
                except discord.Forbidden:
                    await client.say("There was an error setting that role. Contact and Admin.")
            else:
                await client.say("That's not a role which you can assign to yourself.")

client.run(TOKEN)
