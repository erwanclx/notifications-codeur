import asyncio
import datetime

import requests
from discord import Webhook, Embed
import aiohttp

from request import get_messages

import os
from dotenv import load_dotenv

load_dotenv()

user_id = os.getenv("CODEUR_USER_ID")
discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

async def send_discord(content):
    message = content[0]
    async with aiohttp.ClientSession() as session:
        discord_webhook = Webhook.from_url(discord_webhook_url, session=session)

        embed = Embed(title="Voir les messages",
                      url=f"https://www.codeur.com/users/{user_id}/messages",
                      colour=0x8080ff,
                      timestamp=datetime.datetime.now())

        embed.set_author(name="Nouveau message sur Codeur",
                         url=f'https://www.codeur.com{message["offer_link"]}')

        embed.add_field(name="Interlocuteur:",
                        value=message['author'],
                        inline=True)
        embed.add_field(name="Titre:",
                        value=message['title'],
                        inline=True)
        embed.add_field(name="Date:",
                        value=datetime.datetime.now().strftime("%d %b."),
                        inline=True)
        embed.add_field(name="Message:",
                        value=message['content'],
                        inline=True)

        embed.set_footer(text="Nouveau message",
                         icon_url="https://scontent.fcdg3-1.fna.fbcdn.net/v/t39.30808-1/327331963_727950938665271_162625617760328204_n.jpg?stp=dst-jpg_p200x200&_nc_cat=104&ccb=1-7&_nc_sid=5f2048&_nc_ohc=PxqbzBBYTU8AX9j44gc&_nc_ht=scontent.fcdg3-1.fna&oh=00_AfCpz-IM2wEncWIoOrIykLC0639H6sRx_QA5kxOK3YtBGw&oe=6538B105")

        await discord_webhook.send(embed=embed, username='Codeur Messages')


async def send_ifttt(content):
    message = content[0]
    ifttt_webhook_url = os.getenv("IFTTT_WEBHOOK_URL")
    data = {
        "author": message['author'],
        "title": message['title'],
        "content": message['content']
    }
    requests.post(ifttt_webhook_url, data=data)


async def main():
    old_messages = []
    while True:
        messages = get_messages()
        if messages != old_messages:
            if not messages[0]['written_by_me']:
                if os.getenv("DISCORD_WEBHOOK_URL"):
                    await send_discord(messages)
                else:
                    print("No DISCORD_WEBHOOK_URL env var found")

                if os.getenv("IFTTT_WEBHOOK_URL"):
                    await send_ifttt(messages)
                else:
                    print("No IFTTT_WEBHOOK_URL env var found")

            old_messages = messages
            print(messages)
            print('New messages, sending to discord..')
            print('Waiting 4 minutes..')
        else:
            print('No new messages')
        await asyncio.sleep(240)


if __name__ == "__main__":
    asyncio.run(main())
