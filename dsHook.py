from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(
    url='YOUR HOOK LINK')


def hookSend(subject, text, textFrom, textTo, date):
    embed = DiscordEmbed(title=f'{subject}, ({textTo})', description=text, color=0, author={"name": textFrom}, footer={"text": "mailPareser (created by gaiko)", "icon_url": "https://sun9-26.userapi.com/impg/IiLEU3r2F7tPrxKjSCeK4Gyu826ss7U0LMAw-A/duzbkIHVx3E.jpg?size=2160x2160&quality=95&sign=8e7977ee7c4527ed40a4b3d056a5f66d&type=album"}, timestamp=date)
    webhook.add_embed(embed)
    webhook.execute()