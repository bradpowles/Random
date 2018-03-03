from discord.ext.commands import Bot

client = Bot(description="Logs when a person joins/leaves/is moved into/from a voice channel.", command_prefix="!", pm_help=False)

TOKEN = ''
CHANNEL_ID = ''


@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_voice_state_update(before, after):
    log_channel = client.get_channel(CHANNEL_ID)
    vc_before = before.voice_channel
    vc_after = after.voice_channel

    if vc_before == vc_after: return

    if vc_before is None:
        msg = "**{}** joined **{}**".format(after.name, vc_after.name)
    elif vc_after is None:
        msg = "**{}** left **{}**".format(after.name, vc_before.name)
    else:
        msg = "**{}** moved into **{}** from **{}**".format(after.name, vc_before.name, vc_after.name)

    await client.send_message(log_channel, msg)


client.run(TOKEN)
