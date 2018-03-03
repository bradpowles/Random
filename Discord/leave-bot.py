from discord.ext.commands import Bot
import datetime

client = Bot(description="How long someone was on the server before they left.", command_prefix="!", pm_help=False)

TOKEN = ''
CHANNEL_ID = ''

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_remove(member):
    since_joined = (datetime.datetime.now() - member.joined_at).days
    msg = "And now its time to say goodbye to out friend {}, they had only been with us {} days.".format(member.name, since_joined)
    print(msg)
    await client.send_message(client.get_channel(CHANNEL_ID), msg)

client.run(TOKEN)
